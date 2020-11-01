Title: SQLAlchemy Cascade Delete: Clarity through Examples
Date: 2020-06-20 18:00
Modified: 2020-10-31 21:42
Author: Eric
Category: How It Works
Tags: Python, Database
Slug: sqlalchemy-cascade-delete
Status: published

Since there is overlapping "cascade delete" functionality supported by
SQLAlchemy -- with the ORM handling some deletes and the database itself
handling others -- it can be hard to know the right way to set it up. Here are
some examples to help clarify how it all works.

## Starting Example

Here we have a couple of models: A `Project` which can have several `Tasks`
associated with it. For now, we don't have any kind of cascades set up.

```py
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    tasks = relationship("Task", back_populates="project")


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="tasks")


engine = create_engine("postgresql:///cascade")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

project = Project(tasks=[Task(), Task()])
session.add(project)
session.commit()
session.delete(project)
session.commit()
```

Note: To run this code, you'll need a database. I'm using
[PostgreSQL](https://www.postgresql.org/), so I first ran `createdb cascade`
from the shell.

When the code deletes `project`, SQLAlchmemy's default behavior is to
explicitly set `task.project_id` to `None` (or `NULL`) for each task that
belongs to the project:

```text
UPDATE task SET project_id=%(project_id)s WHERE task.id = %(task_id)s
({'project_id': None, 'task_id': 1}, {'project_id': None, 'task_id': 2})
DELETE FROM project WHERE project.id = %(id)s
{'id': 1}
```

If we don't want tasks unassociated with a project floating around, we'll
require that a `project_id` be set by adding `nullable=False`:

```py
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
```

Note: If you're following along, remember that to change the schema, you'll
want to re-create the database by running `dropdb cascade; createdb cascade`.
Or you could put in a call to `Base.metadata.drop_all(engine)`.

Running the updated code results in an exception:

```text
psycopg2.errors.NotNullViolation: null value in column "project_id"
violates not-null constraint
```

This is a **good** thing. It means that the database is enforcing the integrity
of the data by preventing a task without a project. So how do we delete a
project?

You *could* do this (but **don't**):

```py
for task in project.tasks:
    session.delete(task)
session.delete(project)
session.commit()
```

```text
DELETE FROM task WHERE task.id = %(id)s
({'id': 3}, {'id': 4})
DELETE FROM project WHERE project.id = %(id)s
{'id': 2}
COMMIT
```

That works, but using a cascade removes the tasks consistently without the
extra code.

## ORM Cascades

The ORM can do the same task deletions automatically if we add a
`cascade="delete"` to the right `relationship`. But we've got two relationships
-- which is the right one? Answer: It goes on the `tasks` relationship in the
`Project` model:

```py
class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    tasks = relationship(
        "Task", back_populates="project", cascade="delete, merge, save-update"
    )
```

```text
DELETE FROM task WHERE task.id = %(id)s
({'id': 1}, {'id': 2})
DELETE FROM project WHERE project.id = %(id)s
{'id': 1}
COMMIT
```

What if you accidentally put the `cascade="delete"` on the wrong relation? The
cascade wouldn't work when deleting the `Task` object, so you'd get the
`NotNullViolation` again when there are left-over tasks with no project.

### Gotcha: merge, save-update

You probably noticed that I set the cascade parameter to `"delete, merge,
save-update"` rather than just `"delete"`. This is because the ORM has other
cascade behaviors aside from `"delete"`, and `"merge, save-update"` are the
ones that are on by default. If you set `cascade="delete"`, you're *turning
off* some of the default behavior of the ORM.

Using "save-update" as an example, you may know that with SQLAlchemy you don't
normally have to explicitly call `session.add()` on every single object to add
it to the database. If you had to do that, it would look like this:

```py
task1 = Task()
session.add(task1)
task2 = Task()
session.add(task2)
project = Project(tasks=[task1, task2])
session.add(project)
session.commit()
```

Instead, since there is a relationship from a project to its tasks, we can do
the simpler:

```py
project = Project(tasks=[Task(), Task()])
session.add(project)
session.commit()
```

It is "save-update" on the relationship that enables this. If you remove
"save-update" from the cascade and run the second code block, the INSERTs won't
happen and SQLAlchemy will emit a warning:

```text
SAWarning: Object of type <Task> not in session, add operation along
'Project.tasks' will not proceed
```

You might also want to look at the shorthand "all" value for cascade (which,
I'm assuming for some backward compatibility reason, isn't actually *all* the
allowed values), since "all, delete-orphan" is a common value when you want to
do cascade deletes.

You can read more about what all the values mean in the [Cascades section of
the documentation](https://docs.sqlalchemy.org/en/13/orm/cascades.html).

## Database Cascades

To have the database delete the tasks itself, we can add `ondelete="CASCADE"`
to `Task.project_id` foreign key. This changes the DDL of the foreign key,
which we can see with a shell into the database:

```text
cascade> \d task
+------------+---------+----------------------------------------------------+
| Column     | Type    | Modifiers                                          |
|------------+---------+----------------------------------------------------|
| id         | integer |  not null default nextval('task_id_seq'::regclass) |
| project_id | integer |  not null                                          |
+------------+---------+----------------------------------------------------+
Indexes:
    "task_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "task_project_id_fkey" FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE

Time: 0.020s
```

If we only add `ondelete="CASCADE"`, however, we get another 'NotNullViolation'
when running the code:

```text
sqlalchemy.exc.IntegrityError: (psycopg2.errors.NotNullViolation) null value
in column "project_id" violates not-null constraint
```

This is a situation where some real confusion can set in, and what I and some
of my colleagues have done in the past is flail around a while until we end up
turning ORM-level cascades back on, declare victory and move on. The
`ondelete="CASCADE"` might remain, but it is never used since the ORM will have
done the deletions before the database gets a chance.

The integrity error happens because the ORM still sets the `project_id` of each
task to `None`:

```text
UPDATE task SET project_id=%(project_id)s WHERE task.id = %(task_id)s
({'project_id': None, 'task_id': 1}, {'project_id': None, 'task_id': 2})
```

The key is that, we need to additionally set
[`passive_deletes=True`](https://docs.sqlalchemy.org/en/13/orm/relationship_api.html#sqlalchemy.orm.relationship.params.passive_deletes)
on the `Project.tasks` relationship, which disables the ORM from loading each
related task and setting `project_id` to None.

```py
class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    tasks = relationship("Task", back_populates="project", passive_deletes=True)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    project_id = Column(
        Integer, ForeignKey("project.id", ondelete="CASCADE"), nullable=False
    )
    project = relationship("Project", back_populates="tasks")
```

Now the ORM only emits a delete for the `project` row:

```text
DELETE FROM project WHERE project.id = %(id)s
{'id': 1}
COMMIT
```

The database took care of deleting the tasks itself:

```text
cascade> SELECT * from task;
+------+--------------+
| id   | project_id   |
|------+--------------|
+------+--------------+
SELECT 0
Time: 0.020s
```

## Which to Use?

The SQLAlchemy [documentation
says](https://docs.sqlalchemy.org/en/13/orm/cascades.html#delete):

> Database level ON DELETE cascade is **vastly more efficient** than that of
> SQLAlchemy.

Which is totally fine since, as the documentation continues to point out,
taking advantage of database cascades within SQLAlchemy is pretty smooth.

Another reason to choose database cascades is that they still happen even if
you want to break out into some raw SQL at some point.

Those reasons are compelling. Why did SQLAlchemy even bother to implement ORM
cascades? A few reasons I thought of are:

1. Maybe you have an existing schema that you're not free to change for some
   reason, but you still want automatic cascade deletes in your code.
2. One of the models you'd like to cascade uses [joined table
   inheritance](https://docs.sqlalchemy.org/en/13/orm/inheritance.html#joined-table-inheritance)
   and you want to avoid a "half deleted" object.
3. Some databases don't support (or don't support by default) FOREIGN KEY, and
   therefore ON DELETE CASCADE.
4. Maybe delete was added for completeness along with the other cascade
   behaviors that only make sense in the context of an ORM.
5. Other ORMs do it, so there is precedence.

## Summary

Database-level cascade deletes are set on `ForeignKey`:

```py
project_id = Column(
    Integer, ForeignKey("project.id", ondelete="CASCADE"), nullable=False
)
```

This says: *ON DELETE of the row I'm referencing CASCADE and delete this row
too.* Remember `passive_deletes=True`!

ORM-level cascade deletes are set on `relationship`:

```py
tasks = relationship(
    "Task", back_populates="project", cascade="all, delete-orphan"
)
```

This says: *Cascade the deletion of this object to these related objects.*

Here is the final code example:

```py
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    tasks = relationship("Task", back_populates="project", passive_deletes=True)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    project_id = Column(
        Integer, ForeignKey("project.id", ondelete="CASCADE"), nullable=False
    )
    project = relationship("Project", back_populates="tasks")


engine = create_engine("postgresql:///cascade")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

project = Project(tasks=[Task(), Task()])
session.add(project)
session.commit()
session.delete(project)
session.commit()
```

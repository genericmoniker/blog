from peewee import *

database = SqliteDatabase('esmithy-comments.db', threadlocals=True)


class BaseModel(Model):
    class Meta:
        database = database


class Comment(BaseModel):
    article = CharField()
    created = DateTimeField()
    author = CharField()
    email = CharField()
    website = CharField()
    approved = BooleanField()

    class Meta:
        order_by = ('-created', )


def initialize():
    database.connect()
    database.create_table(Comment, True)
    database.close()

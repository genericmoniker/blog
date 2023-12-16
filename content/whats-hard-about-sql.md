Title: What's hard about SQL
Date: 2023-12-15 19:25
Author: Eric
Category: Opinion
Slug: sql-hard
Status: published

These are some things that I find difficult about SQL.

## Leaky abstraction

SQL is the poster-child for [leaky
abstractions](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/).

> The SQL language is meant to abstract away the procedural steps that are needed to
> query a database, instead allowing you to define merely what you want and let the
> database figure out the procedural steps to query it. But in some cases, certain SQL
> queries are thousands of times slower than other logically equivalent queries.

[This post](https://explainextended.com/2009/07/12/double-thinking-in-sql/) goes
further, saying:

> SQL abstraction leaks like a sieve filled with superfluid helium. And this is not
> because RDBMS developers are dumb. This is because the thing they are trying to
> abstract is way too complex to do it efficiently.

If your query is slow or the CPU usage of your database server is too high, you need to
delve into the art of reading query plans, at which point you need to understand the
algorithms used to find data (What is a "Nested Loop Anti Join" and is it OK that it is
being used?) as well as various indexing strategies and the abstraction starts to
disappear.

If you don't care at all about performance, you'll be *fine*.

The recommendation is to realize that you have to live with the abstraction leak and not
rail against it.

## Multiple ways to do it

There are often several logically equivalent ways to query. So you figure out some
complex query and it works! Yay! But now you have to check the performance to see if
your query is usable, and if not, find a different way to do it. And often it isn't just
"tweak this part", it is "rethink your whole strategy".

Some things are "known" to be slower in advance:

* Cross joins
* Correlated subqueries
* Subqueries generally?

But it is hard to know for sure since database technology continues to evolve, and
performance is engine-specific.

## Performance tests are hard

Query plans depend on the existing data in the database, so require that you have
production-like data to be valid.

Timing the wall-clock speed of queries (like if you're measuring response time in a web
app, which is what you really care about) requires you to have production-like data,
production-like load on the database engine and production-like networking to be valid.

I do wonder what good processes developers have in place to make that feasible when
they're writing database code.

## Normalization is vague

With the math-like theory behind relational databases, you'd expect the normal forms to
be defined with absolute precision, but there is actually a fair amount of disagreement
about what they mean among various sources.

It may be better to get a general sense of what normalization is and how violations can
result in anomalies than to get too caught up in what exactly is first or third normal
form.

## Questions about principles get answered with a query

People ask questions that should be answered with an explanation of how you do something
well generally, and instead are answered with "This query does what you want."

For example, [this
question](https://stackoverflow.com/questions/2909758/how-can-i-factor-out-repeated-expressions-in-an-sql-query-column-aliases-dont)
is asking about factoring out repeated expressions. One of the answers was a copy/paste
of the original query with a slight modification to make it work, no explanation
provided (though I did edit the answer to at least point out the tiny difference).

Another
[example](https://stackoverflow.com/questions/5578918/reducing-redundancy-duplication-in-sql-code)
for a similar question has three separate answers by the really high reputation asker,
two of which provide zero explanation and are just different queries. The one that does
have a little explanation is more about giving credit to someone else for the idea (I
think??) rather than explaining anything.

Of course, the other side of this is that people will ask questions about their exact,
verbose query rather than something minimal that shows the problem, so maybe that's what
some askers want anyway -- for someone to fix their query rather than teach them
something.

## Object relational impedance mismatch

Adding an ORM can make programming easier, which is great... until you have to translate
complex SQL into the ORM syntax, which is like having to figure out your queries twice.

ORMs tend to be among the most complex libraries I've ever used.

## Warnings anyone?

A common mistake will just silently fail because returning something other than the
result or an error is generally not done.

An example:

```sql
SELECT * FROM foo where bar = NULL;
```

This query will never return any rows because NULL is not comparable (though the
database engine [*might be* configured](https://stackoverflow.com/a/1843460/86356) such
that it is).

Some will say "NULL isn't a real value, it just means 'unknown' and of course you can't
meaningfully compare two unknowns." To which I respond:

1. Then why can you configure the engine such that `NULL = NULL` returns true?
2. Why doesn't the engine tell you you're probably doing something wrong?

The right way is:

```sql
SELECT * FROM foo where bar IS NULL;
```

But how many times have I accidentally done the first one and been baffled by the
result?

## It can be tool-unfriendly

Auto-completion is great, but it is hard to auto-complete a language where you have to
specify the fields you want before specifying where they come from.

```sql
SELECT uuid, name, last_modified ...
```

If you're in an interactive shell and accidentally hit enter too soon, you could destroy
all the data in a table.

```sql
DELETE from foo
```

Oops. I was going to add a `WHERE`...

Hopefully you've got some kind of destructive statement confirmation turned on.

## How do you know if your query is right?

You have to know enough about your data to have a rough idea of what the result *should*
be. If you get back an answer and don't know much about the expected result, then what?
Is the answer right or did I screw up the query? You can test a query against a smaller
dataset so long as it is a correct representation of the larger data.

There's some advice [in this Reddit post](
https://www.reddit.com/r/SQL/comments/qea1ny/how_to_tell_if_a_query_is_correct/)

## What is great about SQL

It's certainly not all bad, otherwise SQL wouldn't be behind such a vast array of
applications.

- SQL is usually more concise than equivalent imperative code
- Algorithms can improve without breaking existing queries
- There is the potential for increased parallelism

See _Designing Data-Intensive Applications_, p. 43

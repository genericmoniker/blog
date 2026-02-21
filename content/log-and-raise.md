Title: The Log-and-Raise Anti-Pattern
Date: 2026-02-20 21:50
Author: Eric
Category: Opinion
Slug: log-and-raise
Status: published

In its simplest form, the log-and-raise pattern looks like this:

```python
def my_function() -> None:
    try:
        do_something()
    except Exception:
        logger.exception("My function failed!")
        raise
```

What's wrong with that? Even the [official Python
documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
says:

> The most common pattern for handling Exception is to print or log the
> exception and then re-raise it (allowing a caller to handle the exception as
> well).

These are the reasons that I don't think this is a good pattern.

## It muddles the responsibilities of the function and the caller

The function's job is to do something or tell the caller that it couldn't by
raising an exception. The caller's job is to decide what to do with an
exception, which might be:

1. to log or print it
2. let it pass up to a higher level
3. suppress it as unimportant
4. etc.

## It leads to spurious log entries

If the caller decides a failure is unimportant but the function has already
logged, then that log message is misleading. Maybe the caller expects failures
and has a way to deal with them, but the function, in its panic that it failed,
litters logs with messages that may not be errors in a broader context.

## It leads to duplicate log entries for a single issue

Going back to the original code example above, the log-and-raise pattern
suggests that the `do_something` function would *also* log-and-raise:

```python
def my_function() -> None:
    try:
        do_something()
    except Exception:
        logger.exception("My function failed!")
        raise


def do_something() -> None:
    try:
        do_something_else()
    except Exception:
        logger.exception("Do something failed!")
        raise
```

The result of following this pattern is a wall of highly redundant tracebacks in
the logs that make it seem like the system is burning to the ground when it was
just a single deep function call that failed.

Furthermore, what should the top-level caller do when it ultimately gets the
exception? It can:

1. make no comment about exceptions assuming that all the lower levels have
   already logged the problem
2. potentially throw one more log message on the pile

Neither of those seems great.

## It makes the code more complicated

Again returning to the code examples above, I'm assuming that in a real system
there is more to the functions than what is in the trivial examples (otherwise
just call `do_something_else` directly and be done with it). But taking the
`try`/`except` out entirely will simplify the code and still allow any
exceptions to propagate up to the level where a decision can be made about what
to do.

With a still-pretty-trivial example, before:

```python
def fetch_some_random_quote() -> Quote:
    count = Database.count("quotes")
    row = randint(0, count)
    try:
        return Database.get_nth(row)
    except DatabaseError:
        logger.exception("Failed!")
        raise
```

And after:

```python
def fetch_some_random_quote() -> Quote:
    count = Database.count("quotes")
    row = randint(0, count)
    return Database.get_nth(row)
```

## Summary

Avoid the log-and-raise pattern in lower-level functions and prefer logging at a
higher-level handling boundary.

## FAQ

**What if there is some extra context inside my function that is important?
Shouldn't I log so that it isn't lost?**

For example:

```python
def fetch_some_random_quote() -> Quote:
    count = Database.count("quotes")
    row = randint(0, count)
    try:
        return Database.get_nth(row)
    except DatabaseError:
        logger.exception("Failed! And the row was %s", row)
        raise
```

I need to log here so that the row isn't lost because that's important!

There are a couple of ways to handle this situation more cleanly:

1. exception chaining
2. exception notes

With exception chaining, we'd create a new exception type in which we can store
the extra interesting data:

```python
class RandomQuoteError(Exception):
    def __init__(self, row: int) -> None:
        super().__init__(f"Failed random quote at row {row}.")
        self.row = row
```

Then we'd use `raise from` to chain the exceptions together:

```python
def fetch_some_random_quote() -> Quote:
    count = Database.count("quotes")
    row = randint(0, count)
    try:
        return Database.get_nth(row)
    except DatabaseError as e:
        raise RandomQuoteError(row) from e
```

A `logger.exception()` call higher up the stack will display information about
both of the exceptions. Or the caller can use attributes of the exceptions if
that is more appropriate for deciding how to handle them.

The other way to handle this is with exception notes, which were added to Python
3.11 with [PEP 678](https://peps.python.org/pep-0678/). This can work well if
you don't want to change the original exception type, just add some commentary.

```python
def fetch_some_random_quote() -> Quote:
    count = Database.count("quotes")
    row = randint(0, count)
    try:
        return Database.get_nth(row)
    except DatabaseError as e:
        e.add_note(f"The row was {row}")
        raise
```

You can add as many notes as you want to an exception. They're all gathered in
the `__notes__` attribute of the exception instance and get displayed right
below the exception message when a traceback is formatted.

**What if I just like to be really verbose so I don't accidentally miss
including something important?**

When I'm troubleshooting a problem, I'd much rather have a single,
information-rich log message for each occurrence of the problem than a dozen log
messages with bits and pieces of the information scattered through them. The
needle is a lot easier to find if you don't dump a haystack on top of it.

Instead put as much information in the exception as might be useful and log it
in just one log statement.

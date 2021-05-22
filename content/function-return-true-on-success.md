Title: Functions Returning True on Success
Date: 2021-05-22 08:20
Author: Eric
Category: Opinion
Tags: Error Handling
Slug: function-return-true-on-success
Status: published

Many beginning programmers latch on to the idea of having functions return
`True` if they succeed and `False` if they fail so that you have code like
this:

```py
if do_something():
    # It worked!
    do_some_other_stuff()
else:
    logger.error("Something didn't work!")
```

For me, I think it was when I saw some code a teaching assistant wrote in my
university operating systems class this way, and it seemed so elegant. But:

* That was using C, for which error handling options are few
* Who really cares that much about *good* error handling for a school project?

This boolean success/fail is actually not such a great idea. Instead, follow
this pattern:

**A function succeeds or raises an exception. If it raises an exception, make
that exception information-rich.**

Some of the reasons are in [Why Exceptions Are Better Than
Returned Error Codes]({filename}/exceptions-vs-returned-error-codes.md), but
there are others for this particular boolean success/fail variation.

What if I have a function that can't fail? Should I do this?

```py
def do_something():
    # do the thing
    return True
```

Consistency is a good thing, right? So shouldn't all my functions work the same
way?

Except that there's now a pointless line of code in this function, and the
contract for it implies that at any time I could start returning `False` and
the caller ought to have realized this and added a previously pointless check
that it returned successfully. The code bloats, and it is too easy to
accidentally miss the return value.

More problematic is the `False` return value when a function can and does fail.
As the caller I'm probably interested in knowing *why* it failed, but `False`
doesn't give me that. "Oh, that's easy," one might say. "Just do the logging
*inside* the function instead of at the call level."

```py
def do_something():
    if do_some_internal_thing():
        return True
    else:
        logger.error("Something failed because of the internal thing!")
        return False
```

This is also not a great idea because it blurs the distinction between:

1. Indicating that something went wrong, which is the function's
   responsibility, and
2. What to do about it, which is the caller's responsibility

Consider this situation:

```py
def some_use_case():
   if not do_something():
        # No worries, fall back...
        do_something_else_instead():
```

The `do_something` function assumes that because *it* failed, that must be an
error that the application should report. But from the caller's perspective, it
isn't an error at all, and now the application log is littered with misleading
errors:

```
ERROR Something failed because of the internal thing!
```

Note that even when using exceptions, the same problem of confused
responsibilities still exists if `do_something` logs itself:

```py
def do_something():
    try:
        do_some_internal_thing()
    except Exception:
        logger.error("Something failed because of the internal thing!")
        raise
```

If `do_something` can add valuable information to the exception raised by
`do_some_internal_thing`, then it can catch it and *put the valuable
information into a new exception* so that it is available to the caller should
it choose to log it. Otherwise, just let the underlying exception through.

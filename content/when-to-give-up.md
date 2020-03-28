Title: When to Give Up
Date: 2020-03-28 09:16
Author: Eric
Category: How-To
Tags: Design
Slug: when-to-give-up
Status: published

When we programmers find an aspect of software that fails intermittently,
we sometimes follow the impulse to add retries with a Churchillian insistence
that we will "Never give in — never, never, never, never"! But sometimes the
right thing is to give up.

One might ask, why retry at all? Didn't Albert Einstein say, “Insanity is doing
the same thing over and over again and expecting different results”? Actually,
[he probably didn't](https://quoteinvestigator.com/2017/03/23/same/), and I've
always found that quote kind of dumb, because doing *exactly* the same
thing over and over again is *really* difficult.

Try this: Get a basketball and shoot a free throw. If it goes in, just do
the same thing you did that time for all your subsequent attempts, and you'll
never miss another free throw! You'd be insane not to believe this!

OK, sure, but we're talking about software here (weren't we at some point?),
where the rigid progression of a program counter through machine instructions
removes a lot of the messy non-determinism you get throwing a ball at a hoop.
Er, so long as the program isn't multi-threaded. Or it's not using a variable
filled with computational detritus because someone forgot to initialize it. Or
the stack hasn't been trashed, or some other process isn't hammering the disk
or eating all the RAM, or the host your VM is running on doesn't have a
hardware malfunction, or the program isn't trying to talk to some other program
in the same sorry state, heaven forbid over a *network*.

So understanding that retrying is sometimes appropriate, my rule of thumb is:

Only retry an operation if you can explain why it is intermittent and why
retrying will help, and retry *only* for that situation.

Here is a bad example:

```py
def get_some_data():
    while True:
        try:
            return get_the_data_somehow()
        except:
            log.error('Failed to get data!')
```

This function is really tenacious. It will loop forever until the call to the
inner `get_the_data_somehow` function returns without raising an exception. It
provokes some questions:

## Why is an exception being raised and what is it?

If it is a SyntaxError, retrying isn't going to help. If it is an IOError,
retrying might help. Likewise blasting repeated HTTP requests to a server
responding with `400 Bad Request` isn't likely to start succeeding.

Only retry on the specific exception, not every possible exception.

If "something weird" just happens sometimes, maybe there is a bug to track
down. If it isn't within your power to fix a known bug, it may make sense to
try again.

## How quickly is it appropriate to retry?

If a network connection is dropped, it might work to retry immediately, or it
could take hours to recover. [Exponential
backoff](https://en.wikipedia.org/wiki/Exponential_backoff) can be a good
strategy, where the program retries quickly after the first error but slows
down as errors continue. It is rarely a good idea to constantly retry without
some kind of delay (sleep) between attempts.

In some situations retrying, or retrying too quickly can make a problem worse.
If the program is calling an HTTP service and gets a `503 Service Unavailable`
response because the service is overloaded, blindly retrying is
counter-productive.

## Does it make sense to retry forever?

It depends.

If the code is handling an HTTP request in a web application, then definitely
not. If it even takes a few seconds to retry that is probably too long, or the
finite number of workers handling requests can get bogged down in retry loops
while the application slows to a crawl, possibly not finishing requests until
the client has timed out and won't see the result even if it were ready
sometime later.

On the other hand, if a program with a hard dependency on another service is
starting up, and that service isn't available, it can log the fact (maybe just
once rather than on every attempt) and patiently wait for it to become
available.

## What's the alternative to retrying?

Fail. With a good error message if possible. Sometimes it is the best choice.


As a final note, if you do need retries, I'd suggest having a shared mechanism
for doing them rather than a bunch of hand-rolled loops scattered through the
code. If you're using Python,
[Tenacity](https://tenacity.readthedocs.io/en/latest/) is a cool package to
consider.

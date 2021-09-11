Title: *Architecture Patterns with Python* Review
Date: 2021-09-11 15:42
Author: Eric
Category: Review
Tags: Python, Design
Slug: architecture-patterns-with-python-review
Status: published

![Architecture Patterns with Python]({static}/images/architecture-patterns.jpg)

*Architecture Patterns with Python* by Harry Percival and Bob Gregory

I learned about this book by watching Harry Percival's 2020 PyCon talk [Stop
Using Mocks (for a while)](https://www.youtube.com/watch?v=rk-f3B-eMkI&t=19s).
In the past, I was pretty enthusiastic about mocks, especially in Python
because they, along with patching, let me test just about anything, often
without needing to alter the structure of my code to do so. Mocks can certainly
be a useful tool, but in recent years, I've become a bit disillusioned by mocks
for being brittle and ugly:

* Patches that "miss" their targets as code changes, sometimes without the test
  failing but with undesirable side-effects like being slow while a real
  network request times out (paying attention to run times can help some).
* Mocks that are overly dependent on implementation details, even to the point
  of how a function is called or how it is imported (non-strict mocking can
  help some).
* Mocks that happily allow the application to call non-existent functions
  (autospec can help some).
* Tests with large numbers of mocks that seem to get copy and pasted between
  tests because nobody wants to bother figuring out which mocks are actually
  necessary (not being lazy or in a hurry can help some).

So how do you test your code without mocks? Trying to answer this has led me
into reading about "Clean Architecture", "Hexagonal Architecture", "Ports and
Adapters", and "Functional Core, Imperative Shell". The book mentions these as
well, summarizing all of them as variations on the dependency inversion
principle, or in short, decoupling your business logic from the technical
details necessary to build an application.

## Part 1

The first part of the book uses a fairly simple domain problem to build up an
architecture to support that simple case and also greater complexity where the
trade-offs of the architecture make more sense. And the authors try to be clear
about what the trade-offs are, and when it is appropriate to use the techniques
presented.

> If your app is essentially a simple CRUD wrapper around a database and isn't
> likely to be anything more than that in the foreseeable future, you don't
> need these patterns. Go ahead and use Django, and save yourself a lot of
> bother.

That isn't being dismissive of Django as some kind of framework for lesser
developers -- it is a recognition that Django is really awesome at CRUD apps,
but can get in the way for different kinds of apps. The authors also include an
appendix specifically for applying some of the patterns when using Django.

The technologies used in the examples happen to align with those used in my
current project at work such as Flask, SQLAlchemy and PostgreSQL. This is great
as some of the specific technical advice is directly applicable for me, but the
book is ultimately about more than using popular technologies of today.

An important take-away for me from the first part of the book is the sweet spot
for testing: at the service layer, which implements the use cases of your
application and that could be called from an HTTP endpoint or a gRPC or a CLI.
I had thought that the core domain model was where you should focus on testing,
but the authors said:

> Tests are supposed to help us change our system fearlessly, but often we see
> teams writing too many tests against their domain model. This causes problems
> when they come to change their codebase and find that they need to update
> tens or even hundreds of unit tests.

I just did a refactoring of some of our database tables at work. The API for
the application, did not change. But it took me more than a month to fix all of
the broken tests caused by the change. It is clear that our architecture and
testing strategy are sometimes a hinderance to change rather than a help.

## Part 2

The second part of the book is about event-driven architecture. It doesn't go
much down the event sourcing road, but rather as a way of decoupling parts of
the application, even if storage is used in a more "traditional" way.

One surprise here was seeing events used as essentially control flow with a
really simple event bus implementation rather than being asynchronous. I'm not
totally sure if you can get away with that if you're writing a web application
and some of the event handlers could take a while to execute, but it made me
realize that the decoupling is still possible even with synchronous handling.
Later on they use Redis as an event broker for some asynchronous events, but
the techniques are not mutually exclusive.

Another surprise was the chapter on CQRS (Command-Query Responsibility
Segregation) where the authors suggest using raw SQL to produce views of data
(a section title is even "Hold On to Your Lunch, Folks"). Having worked with
people who despise ORMs, I can understand that doing complex queries with an
ORM sometimes feels like suffering twice: Once to figure out the query and
again to figure out how to translate the SQL to the ORM. This is an aspect of
the book that I still need to wrap my head around.

## Summary

I find it is kind of hard to practice architecture. If you work on a project
for a long time, you don't get a lot of chances to see different systems. If
you move quickly between projects you don't see the long-term consequences of
your decisions. As a result, I really appreciate when people are willing to
share their experiences. *Architecture Patterns with Python* has given me a lot
to think about and proposed solutions to some of the very problems I'm facing
right now. For me it has been a great read.

If you'd like to read it, you can do so for free
[here](http://www.cosmicpython.com/book/preface.html). Another free option is
the [GitHub repo](https://github.com/cosmicpython/book) for the book, where the
issues section includes some questions from readers and authors' responses.
Personally, I bought the [DRM-free edition from
ebooks.com](https://www.ebooks.com/en-us/book/209971850/architecture-patterns-with-python/harry-percival/)
because I knew I'd want to make some annotations while I read. That met my
needs, but there were times when the text of the book implied a hyperlink that
wasn't present, and one of the figures (9-1) was wrong. The online
versions fix that.

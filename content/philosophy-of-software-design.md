Title: Thoughts on *A Philosophy of Software Design*
Date: 2024-04-20 10:54
Modified: 2025-03-01 16:35
Author: Eric
Category: Review
Slug: philosophy-of-software-design
Status: published

![Book Cover]({static}/images/philosophy-software-design.jpg)

John Ousterhout's *A Philosophy of Software Design* sometimes aligned with and
other times challenged my opinions about building software. The overall theme
could be summarized with a Ray Ozzie quote: "Complexity kills. It sucks the life
out of developers, it makes products difficult to plan, build and test, it
introduces security challenges, and it causes end-user and administrator
frustration."

Reading John's book at the precise time when I was coming off of a failed
software project emphasized that one of the large contributing factors to the
failure was unmitigated complexity. In particular, the book's description of
"tactical programming" hit very close to home.

> Before long, some of the complexities will start causing problems, and you
> will begin to wish you hadn't taken those early shortcuts. But you will tell
> yourself that it's more important to get the next feature working than to go
> back and refactor existing code. Refactoring may help out in the long run, but
> it will definitely slow down the current task. So, you look for quick patches
> to work around any problems you encounter. This just creates more complexity,
> which then requires more patches. Pretty soon the code is a mess, but by this
> point things are so bad that it would take months of work to clean it up.
> There's no way your schedule can tolerate that kind of delay and fixing one or
> two of the problems doesn't seem like it will make much difference, so you
> just keep programming tactically.

## Patching over design flaws

In my project, after hard work to get a v1 of the product out, I breathed a sigh
of relief that we'd finally have a little time to go back and fix some things.
Unfortunately, and inexplicably, we were somehow already late on the next
version of the product and it became suddenly clear that we were going to have
to live with what we had.

One example was a deliberate shortcut of assuming that all nodes in a
distributed system would be able to directly address each other and we built a
bunch of gRPC services that called each other. But it turned out that the
majority of environments where the system would be deployed would have NAT and
firewalls between the nodes. We could have switched to using bidirectional gRPC
streaming, such that only "outbound" connections needed to be made, but there
was already so much code that would have to be changed that we instead built a
tunneling system that allowed services to still mostly act like everything was
local.

The tunneling code was some impressive engineering, and crisis averted. Never
mind that some communication channels had to be double encrypted, that we had to
store a bunch of nodes' IP addresses in a database and try to keep that
up-to-date with changing address assignments. And there were only about 2.5
people in the company that could troubleshoot it when things went wrong. It is
extremely uncomfortable when you end up on a phone call with a customer for an
escalated support case and you don't have the tools to trouble-shoot because the
ticket you put into the backlog to create such tools was deferred to the release
right after "hell freezes over".

Some relevant advice from the book:

"...you should not think of 'working code' as your primary goal, though of
course your code must work. Your primary goal must be to produce a great design,
which also happens to work. This is *strategic programming*." (p.15)

"Ideally, when you have finished with each change, the system will have the
structure it would have had if you had designed it from the start with that
change in mind." (p.138)

I'm pretty sure we wouldn't have started out saying, "What we really need is
a custom tunneling system!"

One other that I didn't fully get:

"One of the risks of agile development is that it can lead to tactical
programming. Agile development tends to focus developers on features.... The
increments of development should be abstractions, not features." (p.155-156)

In my project, we *were* doing agile development, and I agree with the feature
emphasis, but I don't understand what it means to do increments of abstractions.
I'd love to understand that better.

## Low effort changes

Another example from my failed project relates to the developer mindset the book
describes as "what is the smallest possible change I can make that does what I
need?" (p.137) That mindset is not presented as a virtue, by the way, but some
developers feel like it is.

We had a gRPC service that handled events by dispatching them to various handler
functions. This service ran in its own process and the code for it was grouped
together reasonably well, meaning it was all in the same directory. At some
point it was decided that it would be better to inject the events into Redis
where they would be handled by Celery workers. The event handling code would be
the same, but it would be called in a completely different context. There was a
tiny change made to create a Celery task that would receive the event and
dispatch to the existing handlers. The problem was that all of the handler code
was left in that original directory so that while it seemed to be part of the
gRPC service, it no longer had a relationship whatsoever except that it *used*
to be part of it.

## Naming things

The book has a whole chapter dedicated to choosing names. I love a good name and
the "ubiquitous language" idea from Domain Driven Design. In the failed project,
I created and tried to maintain a glossary when domain concepts needed naming.
But it was hard. A lot of people didn't have the patience to think about and
discuss good names, and were even less interested in changing the off-the-cuff
names in existing code to match the glossary. One naming failure was a component
that had a customer-facing name. The name was incredibly ambiguous such that I
mischievously created a three page document with pictures to clarify what it
might mean in various contexts.

In some cases our naming was a home-run and facilitated discussion and
understanding. "Names are a form of abstraction: they provide a simplified way
of thinking about a more complex underlying entity. Like other forms of
abstraction, the best names are those that focus attention on what is most
important about the underlying entity while omitting details that are less
important." (p.123)

## Consistency

In the chapter on consistency, this part hurt a bit:

> Don't change existing conventions. Resist the urge to "improve" on existing
> conventions. Having a "better idea" is not a sufficient excuse to introduce
> inconsistencies. Your new idea may indeed be better, but the value of
> consistency over inconsistency is almost always greater than the value of one
> approach over another.

We had a GraphQL API, and the implementation of the mutations (akin to non-GET
endpoints in a REST API) was a mix of GraphQL-isms and business logic in a
multi-thousands line module. The only way to test the business logic was to send
GraphQL queries through (which, by the way, do not count concision among their
strengths) and parse JSON in return. This made me unhappy, so when I needed to
create a set of new mutations, I found a way to write them with the business
logic cleanly separated from anything to do with GraphQL. The tests were simple.
I figured this would be the new way forward for the team.

On this, the book asks, "...is the new approach so much better that it is worth
taking the time to update all of the old uses?" Hrm... that's a lot of code to
rewrite. Is there a process that can be applied to improve the design
incrementally rather than being all or nothing? It would have been great to
catch the issue early so that there wouldn't be as much to correct, but when
there is so much going on in the early stages of a project it is hard to turn a
sense of "this doesn't seem quite right" into a clear design that should replace
it. I think we even had conversations among the team about it, but some people
didn't feel like it was a big deal, making it even harder to put on the brakes
and get to a better design.

## Comments

The book has two entire chapters devoted to code comments, and I realize how
influenced I've been by Kent Beck, Robert Martin, and others with a deprecatory
view of comments. The book even quotes Robert Martin as a "different opinion"
from that which the author is trying to present: "Comments are always failures.
We must have them because we can't always figure out how to express ourselves
without them, but their use is not a cause for celebration." (p.99) The book
argues that comments are, on the contrary, essential and that the reasons for
not writing them are mostly bogus.

One excuse given for not writing comments is that they're worthless. I know I've
seen function documentation that looks something like this:

```py
def load_data(file):
    """Load the data.

    @param file The file
    @return The data
    """
    ...
```

Yeah, pretty worthless. But a bad comment doesn't mean comments are bad. The
book gives other examples of poor comments and how they can be improved to give
information that isn't obvious from the code.

A type of comment I've felt the lack of recently is a module/file level comment
that just says what this thing is. That might be me going back to a personal
side project trying to remember how it works, or looking at a shell script that
even has a usage comment listing the parameters but doesn't ever say what the
script **does**. In both cases you just have to read through all the code to
figure it out.

One of the book's strongest assertions about comments is:

> Recall... that an abstraction is a simplified view of an entity, which
> preserves essential information but omits details that can safely be ignored.
> Code isn't suitable for describing abstractions: it's too low level and it
> includes implementation details that shouldn't be visible in the abstraction.
> The only way to describe an abstraction is with comments. **If you want code
> that presents good abstractions, you must document those abstractions with
> comments.** (p.110)

## Method factoring

Another area where the book challenged my opinion is on breaking up methods. It
says:

> Long methods aren't always bad. For example, suppose a method contains five
> 20-line blocks of code that are executed in order. If the blocks are
> relatively independent, then the methods can be read and understood one block
> at a time; there is not much benefit in moving each of the blocks into a
> separate method. If the blocks have complex interactions, it's even more
> important to keep them together so readers can see all of the code at once; if
> each block is in a separate method, readers will have to flip back and forth
> between these spread-out methods in order to understand how they work
> together. Methods containing hundreds of lines of code are fine if they have a
> simple signature and are easy to read. These methods are deep (lots of
> functionality, simple interface), which is good. (p.73)

While I like the idea of "lots of functionality, simple interface", I *do* have
a preference for splitting a large method out into separate, usually "private",
methods.

The first reason I like to do this is that I find a few simple methods to be
overall less complex than one, more complex, method. Cyclomatic complexity is
one of the few metrics of code complexity that we have, and that can be reduced
by breaking a deeply nested method apart. One of the things I like about
Python's [preference for a relatively narrow line
width]({filename}/your-right-margin-is-telling-you-something.md) is that it
gives me an "as-you-code" proxy for cyclomatic complexity.

The second reason I like to split methods is that it is another example of
abstraction. I can see the overall structure of the "parent" method without
getting bogged down in all of the details. When I want to know a detail, I can
go to the "child" method. In my experience, I haven't had to constantly flip
back and forth between parent and child to understand either the parent or the
child.

The book does say that splitting out a fairly general-purpose subtask method is
appropriate if the overall complexity of the system is reduced as a result, so
I'm not *entirely* sure if I'm disagreeing with the author's opinion here.

## Conclusion

To wrap up, I found the book very thought provoking and well worth the read. The
last few sentences were relevant to both my recent project failure and my
[previous blog post]({filename}/happy-coder.md):

> Poor designers spend most of their time chasing bugs in complicated and
> brittle code. If you improve your design skills, not only will you produce
> higher quality software more quickly, but the software development process
> will be more enjoyable. (p.176)

## Addendum - March 1, 2025

John Osterhout recently sent a message to his mailing list saying:

> As many of you may know, I have significant disagreements with the software
> design advice given by Robert "Uncle Bob" Martin in his book "Clean Code".
> Over the last several months he and I have been discussing our disagreements
> and we have recorded the discussion in a document on GitHub:
>
> https://github.com/johnousterhout/aposd-vs-clean-code/blob/main/README.md

That is, in the face of disagreement, they talked to each other. In doing so
they found areas where they could agree, but also stood firm on where they
disagree.
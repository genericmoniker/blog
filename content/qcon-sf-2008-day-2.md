Title: QCon SF 2008 Day 2
Date: 2008-11-20 23:04
Author: Eric
Category: Event
Slug: qcon-sf-2008-day-2
Status: published

It's another day of industry stand-outs at QCon.

![San Francisco]({static}/images/qcon-4.jpg)

Shifting Storage (Tim Bray)
---------------------------

The day started with a keynote from Tim Bray, of XML fame. Tim spoke
about the application stack from this perspective:

-   Application code
-   Object-relational mapping
-   SQL engine
-   Operating system/file system
-   Cache/disks

He mainly focused on the O/R mapping layer and the SQL engine, where
technology, to quote Tim, "sucks". O/R mapping is really hard, and it's
too bad that object databases never really got commercial success
(Martin Fowler in the front row nods in agreement). SQL engines are too
slow, driving people to distributed hash tables like
[memcached](http://en.wikipedia.org/wiki/Memcached) instead, or even
skipping the database engine entirely to go to the file system. SQL
engines are also complex and laden with features that never get used.
This is inspiring projects like
[Drizzle](https://launchpad.net/drizzle), a database forked from MySQL
in an attempt to slim things down.

Tim also had good things to say about
[CouchDB](http://incubator.apache.org/couchdb/), a document-oriented
database that is accessible only via HTTP. I don't know anything about
this project, but Tim's exact words were, "I'm infatuated with this" and
"frighteningly elegant".

Another topic was comparing the relative speeds of the storage stack,
from CPU registers down to hard drives. The interesting technology
coming into this area is solid state drives. His benchmarks show that
write speeds are about that of a middling hard drive, but read speeds
are really, really good.

Given that most web applications are I/O limited, it can really pay off
to keep your eyes on up and coming technologies like alternate data
strategies and solid state drives.

HTTP Status Report (Mark Nottingham)
------------------------------------

I went over to the REST track for a little bit, chaired by Jim Webber, a
[noted expert on man
boobs](http://www.infoq.com/presentations/soa-without-esb). The speaker
for this session, though, was Mark Nottingham, the chair of the HTTPbis
working group. They are essentially rewriting the HTTP 1.1 spec, but not
trying to add any new features. Why bother? Mark explained that the
existing spec is ambiguous, not well organized, not very approachable,
and occasionally requires consultation with one of the authors to
understand. As a result, everybody pretty much gets the main parts
right, but there are a bunch of other things that are not very
interoperable between implementations. HTTPbis, targeted for completion
in about six months, will hopefully clarify the spec enough to eliminate
incompatibilities.

Mark also spoke briefly about what might be expected for the future of
HTTP, like a standard set of conformance tests, better authentication,
transport over SCTP instead of TCP, and others.

![Moscone]({static}/images/qcon-5.jpg)

Joys and Pains of Long-Lived Code (Jeremy Miller)
-------------------------------------------------

I had just read Jeremy's [Cohesion and
Coupling](http://msdn.microsoft.com/en-us/magazine/cc947917.aspx) article
in MSDN last week, so it was nice to put a name to the face. Jeremy gave
a retrospective of StructureMap, an IoC container he has been writing
and maintaining over the past five years. He talked about the changes
that have happened over the life of the project, both in the .NET
community and the .NET platform itself, and how things he had done with
StructureMap made adapting to those changes easy or hard.

These are some of the lessons he learned.

-   Good design at the class level is crucial.
-   Bad tests make it harder to change the code rather than easier.
-   TDD as refined to [BDD](http://behaviour-driven.org/) is best (I
    need to learn more about this).
-   Getting abstractions right not only improves the code, it opens up
    new possibilities.
-   DRY - even a little duplication is bad.

I also appreciated a comment he made when answering a question: don't
use an IoC container when writing tests. I've seen people do that in the
past: they have a constructor injected set of dependencies and try to
reconfigure the container to inject mocks. Just pass the mocks in the
constructor!

![San Francisco]({static}/images/qcon-6.jpg)

F\# (Don Syme)
--------------

While I have heard a bit about F\#, I've not really spent much time
trying to understand it. What better opportunity could you have than to
get the designer to provide an introduction? Of course learning a
language is best done by writing code, not hearing a presentation. Still
it was interesting to get a high-level overview and to see a few
examples. One of Don's favorite things was to show the difference in
lines of code between functionally equivalent bits of C\# and F\#. An
asynchronous I/O example had three pages of C\# code to a dozen lines of
F\#.

Don said that F\# is well-suited to problems dealing with data
transformation, but not so great for building user interfaces (even
though all the .NET UI libraries are accessible from F\#).

TDD and DbC (Greg Young)
------------------------

I've posted about design by contract in the past ([part
1]({filename}/design-by-contract.md), [part
2]({filename}/design-by-contract-part-2.md)), and sort of intended to talk
about unit testing and DbC at some point, but never got around to it. So I was
interested to hear what Greg had to say. The first part of his talk was an
overview of DbC, showing some spec\# code to demonstrate the concepts and
letting the code verifier find the problems. I noticed that Microsoft had
announced a contracts library at PDC, so the exploratory work of spec\# will be
incorporated into the framework instead of as language extensions.

The main point of Greg's presentation is that tests and contracts are
complimentary. Tests should focus on the behavior (another reference to
BDD) while contracts focus on constraints. Having contracts means fewer
tests to write because you don't have to write all the dumb tests that
check that an argument exception is thrown when parameter x is null. In
fact, not only do you not *need* to write those tests, if you try anyway
the code verifier will complain. So you almost *can't* write those
tests, and therefore contracts push you toward testing the meaningful
behavior of the code.

![Statue]({static}/images/qcon-7.jpg)

Democratizing the Cloud - MS Volta (Erik Meijer)
------------------------------------------------

I'm again impressed with the caliber of speakers here. Eric Meijer is
the guy who designed LINQ, among other things. Currently he is working
on Volta, which put bluntly, is GWT for .NET. Volta allows translation
of MSIL to Javascript so that you can build client apps writing .NET
code. If you happen to have Silverlight on the client, you can also
target that as the runtime environment instead of going to Javascript.

There is also a development work flow in which you write a single tiered
.NET application, then split it into client and server tiers by simply
annotating the code -- saying which bits should execute on the server
and which on the client. Greg Young, from the previous presentation,
immediately started pushing back citing the [8 fallacies of distributed
computing](http://michael.toren.net/mirrors/eight-fallacies-of-distributed-computing/).
Erik simply skipped ahead a little to a slide showing the 8 fallacies,
and assured the audience that programmers would still be in control
enough to avoid the pain.

Erik's description of the translation of IL to Javascript was
interesting. They are not making any attempt to produce Javascript that
follows typical Javascript style. Instead they use it like an assembly
language, and focus on preserving the precise semantics of the .NET
code. This gets a little tricky in some cases, such as jumps. Javascript
has no goto, but IL, being very low-level, uses them extensively. Erik
showed how they used switch statements to get the same behavior. It's
not pretty Javascript, but that's not really the point.

The presentation went down a little bit of a rat-hole when Erik talked
about some security issues. There was quite a bit of debate from some
folks the audience about whether they were doing it right. While it's
neat to see that kind of interaction, I'm not sure it is a good use of
time for people seeing this for the first time to try to give informed
design criticism.

Volta is still a work-in-progress. It will be interesting to see if it
can mature into something that will give as great a development
experience as Alex Moffat [described
yesterday]({filename}/qcon-sf-2008-day-1.md) with GWT.

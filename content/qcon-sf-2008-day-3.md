Title: QCon SF 2008 Day 3
Date: 2008-11-22 15:04
Author: Eric
Category: Event
Slug: qcon-sf-2008-day-3
Status: published

Friday was the third and final day of the QCon conference.

![Cable car]({filename}/images/qcon-11.jpg)

Frameworks and DDD (Tim McCarthy)
---------------------------------

On Friday, I spent most of the day in the Domain Driven Design track,
hosted by Eric Evans. The first speaker was Tim McCarthy, who has
recently written a book on using DDD with.NET and C\#. Tim raised an
interesting question with his talk: How do you keep your domain code
clean when working with frameworks? By frameworks, Tim meant broad
frameworks like ASP.NET as well as more narrow, application frameworks
like SharePoint. The challenge is that with frameworks, and especially
the wizard/designer approaches to coding sometimes advocated by
Microsoft, it can be really easy to become inappropriately coupled to
persistence, specific APIs, etc.

Unfortunately, Tim had a couple of problems in his presentation that
made it less valuable to me than it might have been. The first problem
was being sort of backward in terms of audience (for me at least). He
worried about whether people knew what SharePoint was, but breezed over
DDD terminology. The second problem was getting bogged down in details
of code from a real-world system. I'm sure that there were good ideas in
there, but they were hard to see because of the context that needed to
explained. There's always something nice about real code for
demonstrating a point, but in a presentation, maybe simple examples
would be better.

Ultimately the point was that DDD provided strategies for a decoupled
system.

Rebuilding guardian.co.uk with DDD (Phil Wills)
-----------------------------------------------

I met Phil on Tuesday over lunch, so I was looking forward to
hearing his presentation. It got off to a rocky start due to technical
difficulties. The number of Macbooks at this conference really drove
home the point that this wasn't a Microsoft conference, but after a
couple of failed attempts to get the presentation going with different
Macs, Martin Fowler (whose machine was one of them) quipped that Macs
being so superior is bullox.

Once the presentation got underway, Phil gave a little background about
the Guardian. The newspaper has its roots in the 18th century, and is
now the largest online newspaper in Europe. They put their first web
site up in 1996, but over the years the system became problematic:

-   Editors had to do a bunch of tedious manual work
-   There were multiple URLs for the same resource
-   New developers were hard to recruit because of the outdated
    technologies in use
-   There was a lot of technical debt preventing big new features

To rebuild the site such that it would be "of the web, not just on the
web" and ready for the future, they took an ambitious strategy of going
agile, using new technologies and different design approaches (DDD).
They got some help from ThoughtWorks to make it up the steep learning
curve involved in such radical change.

Phil shared a few things they learned along the way. One thing was the
importance of using the language of the problem domain everywhere, which
allowed even the non-technical people on the team to contribute in
unexpected ways. An example of this was a big breakthrough in terms of
object composition. Phil showed an original object hierarchy and a much
cleaner one. He said that of course, big breakthroughs always seem
obvious and trivial in hindsight, but it was a non-engineer that came up
with it. Another example he cited was a time when one of the users came
over to a developer's machine for a feature demo. While the develper was
getting things set up, the user looked over his shoulder at the code and
commented, "Does this do what I think it's doing? If so, that's not
right." Because the code used the domain language for object names and
methods, he was able to understand it well enough to spot a bug.

Another thing Phil and his team learned is that the database schema is
**not** the model. The model is the code -- even though sometimes people
get a false sense that if something isn't in the database, it isn't
*really* the model.

He also talked about the utility of "value" objects. In Domain Driven
Design, "entities" are the big stars, representing the main business
objects. But it can be really valuable to have small, simple objects as
helpers to the entities. These are objects that might just be
represented as a string or an int, but if you discover some logic
associated with that particular kind of string or int, encapsulating
that logic into a slightly more specialized object can result in simpler
entities.

![Skyline]({filename}/images/qcon-9.jpg)

Facebook Architecture (Aditya Agarwal)
--------------------------------------

I took a break from the DDD track to hear a little about the
architecture of Facebook. Aditya is the director of engineering at
Facebook, and after hearing his presentation, I came to a couple of
conclusions:

1.  I haven't ever had to worry about scalability anywhere near this,
    and
2.  I'm kind of glad about that.

Facebook is built on the LAMP stack, but pretty much every component has
been customized and optimized for their particular application. They
also use memcached, which Aditya said was a huge factor in the
performance of the site. This agreed nicely with Tim Bray's talk from
the other day: databases are too slow for this kind of scalability.
Aditya said their memcache distributed hash table consumes 25
*terabytes* of RAM.

When asked if they intend to submit their changes to LAMP components
back into the main projects, Aditya said, "I don't think they'd accept
our hacks," which got a chuckle from the audience. The slightly cynical
part of me thought, that'd be an interesting way to keep from having to
share GPL changes: saying, "Naw, you wouldn't really want this hacked up
stuff..."

![Fountain]({filename}/images/qcon-8.jpg)

Strategic Design (Eric Evans)
-----------------------------

Back to the DDD track, to hear "Mr. Domain Driven Design" himself. His
premise for this talk was:

> Not all of a large system will be well-designed.

We wish it isn't so, but it just seems to be a fact of life. He then
talked about the oh so common situation that a development team finds
itself in. We've got this legacy system, and it has all the problems
that typically make us unhappy with legacy systems: poor design, old
technologies, accidental complexity, etc. So what do we do?

**Plan A**: Scrap it and start over. Eric had a diagram showing the big
ball of mud becoming this beautiful pyramid of a system. What ends up
really happening? Everything seems fabulous at first as a solid base
gets built up. Then, at the point where parity with the legacy system is
supposed to appear, panic sets in. The is the classic case [documented
by Joel
Spolsky](http://www.joelonsoftware.com/articles/fog0000000069.html)
where you suddenly realize that all that seemingly pointless cruft was
actually important. So you finally end up with a system, two years
later, that does exactly what the original system did, and that final
phase of "add cool new features" never seems to happen.

**Plan B**: Refactor. Eric argued that this approach doesn't really work
either. There aren't enough tests to really work something over, and
while you're trying, other people are continuing to hack the code base
and mess up your perfect plans. He joked that the hackers are
irresistibly drawn to the code that you just cleaned up.

**Plan C**: Plan to hack, since that seems like what will happen anyway.

Leaving behind the plans for a while, Eric talked about the different
parts of the domain. He said that this is covered in chapter 15 of his
book, but I'll try to summarize as I understood it from the talk.

The biggest part is the generic subdomain. This is all the framework and
code that is pretty generic and applicable across the whole software
development practise. Next is the supporting subdomain, which is code
that starts to be more specific to the problem domain you're working in,
but could still be applied somewhat generically in a specific industry.
Finally, the smallest bit, is the core domain. This is what makes your
system worth building in the first place. This is what gives you your
competitive advantage. This is why people will buy your stuff. Another
perspective of the three levels is stuff you buy, stuff you outsource,
and stuff you build, respectively.

Next, a question: Why do irresponsible programmers become heroes? It's
largely due to mistakes that **responsible** programmers make. What do
responsible programmers do? They build frameworks because they don't
trust that the hackers can build something without some kind of
scaffolding. They go around cleaning up other people's messes. As a
result of these, they don't produce the sexy new features, and shield
the hackers from the consequences of their poor practices. The key,
though, is that the heroes are working in the core domain.

**Plan D**: Distill the core domain from the ball of mud. Instead of
considering the legacy system a liability, look for the assets. Build
what Eric calls an Anti-Corruption Layer, which sounded kind of like the
façade pattern to me. Instead of transforming the ball of mud into a
beautiful pyramid, focus on building the very cap of the pyramid (the
core domain) and making that beautiful, while connecting to the ball of
mud as necessary, but with a clear insulating layer.

This topic is really intriguing to me, but I can't say that I understand
how to apply it. Eric remarked that all of this stuff is in his book,
but being toward the end, some people don't, uh, quite make it that far.
Guilty as charged. Well, although I've got the book, I haven't really
made a serious effort to read it yet. Maybe it's time to fix that.

![Buildings]({filename}/images/qcon-10.jpg)

Publishing and Protecting the Model (David Laribee)
---------------------------------------------------

Since Eric Evans' talk was so good, I thought I'd finish out the day
with the last talk in the DDD track. This was by David Laribee, who is
billed as the [ALT.NET](http://altdotnet.org/) ring leader. ALT.NET is a
community that I'll unfairly and over simply summarize as "I can
write C\# on a Mac".

Dave's talk was about keeping the model clean, given that it has to be
exposed to the unwashed masses to be useful. Or something like that.
Maybe after three full days of presentations I was just full, or maybe
Dave wanted a cool presentation more than a pragmatic one, but I had a
hard time following this one. It started out at a high philosophical
level, and by philosophical I mean classically so: Plato and Aristotle.
It ended with C\# 3.0 extension methods. I'm sure I'm not doing it
justice.

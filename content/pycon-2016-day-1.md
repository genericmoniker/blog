Title: PyCon 2016 - Day 1
Date: 2016-05-30 23:56
Author: Eric
Category: Event
Slug: pycon-2016-day-1
Status: published

PyCon is in Portland, Oregon this year, which is not only more
accessible to me than eastern Canada (the previous location), but also
the area where most of my extended family lives. Those facts combined to
make it a great time to attend for the first time.

![Willamette River]({static}/images/pycon-willamette.jpg)

In a way, I feel like I've been to PyCon already. At work, we've been
watching videos from previous years in a weekly "lunch and learn", so I
recognize some people from their talks. Oh, that's Brandon Rhodes
opening the conference. Hey, there's Raymond Hettinger sitting a few
rows up in the audience.

It raises the question of why even go to PyCon if all the talks are
online? I'm getting a sense for that still, but a few reasons are:

-   Pre-conference tutorials
-   The expo hall with sponsor booths
-   Open spaces, which are self-organizing get-togethers on some topic
-   The poster session, where people put up posters and talk about
    something for small groups
-   Startup row, which showcases brand new tech companies
-   Post-conference sprints to work on open source projects
-   Chances to meet people from a variety of places and hear what they
    work on

There's also the fact that all those video talks wouldn't be available
if nobody came to the conference in the first place.

With that, to the talks...

Keynote, Lorena Barba
---------------------

Dr. Barba talked about programming education as part of a general
literacy for the modern world, likening the current cs4all (computer
science for all) initiative to a previous cp4e (computer programming for
everyone) initiative from 1999 headed up by none other than Python
creator Guido van Rossum.

She also talked about the work of Seymour Paper (did you know the
original turtle graphics was a robot that drew on paper because that was
easier than doing computer graphics?) Fernando Flores and Terry
Winograd, showing that a GitHub pull request is the realization of ideas
they had had decades ago. In a world where so much information is
instantly available, what is important to *know* is perhaps their
language action models of making and fulfilling committments.

Seriously Strong Security on a Shoestring - Kelsey Gilmore-Innis
----------------------------------------------------------------

Kelsey is the sole developer of Callisto, a system for reporting college
sexual assault. Given the sensitive nature of the site, the security
needed to be top-notch, despite her not being any kind of security
expert.

She talked about some of her strategies, which include building on the
solid work of others (time-tested frameworks and security libraries,
expert pen-testers) while making decisions based on her deep
understanding of her application. As an example of the latter, she
decided that reports of incidents would be encrypted, and only the
reporter would have the key. That way, even a court order wouldn't
reveal anything a victim didn't want to disclose.

Refactoring Python: Why and how to restructure your code - Brett Slarkin
------------------------------------------------------------------------

Brett is the author of *[Effective
Python](https://www.goodreads.com/book/show/23020812-effective-python)*,
a book I've had on my To Read list after hearing an interview with him
on a Podcast.

Step one is writing code -- just getting it to work. Step 2 is
refactoring until the code is obvious to a new reader. Great programmers
spend about equal time on each parts. We tend to think that we don't
have time to do more after the code works, but refactoring is really a
good investment -- meaning that it pays for itself and more.

He referenced Martin Fowler's [canonical
book](https://www.goodreads.com/book/show/44936.Refactoring), but said
that it unfortunately is too Java-centric. Some general principles still
apply, though.

In addition to the need for thorough and fast tests, I like that Brett
said, "Don't be afraid to make mistakes." Sometimes we let fear of
breaking something prevent us from making the code great.

He then covered some specific refactoring techniques, including ways of
making changes without having to break all the existing callers.

![Steel Bridge]({static}/images/pycon-steel-bridge.jpg)


Code Unto Others - Nathaniel Manista, Augie Fackler
---------------------------------------------------

This talk was about making life easier on future maintainers of code. I
thought they had some good points, like keeping things small to take
advantage of working memory (human memory, that is), consistent levels
of abstraction, using intermediate abstractions, and not overusing
classes (like [Jack Diederich's "Stop Writing Classes"
talk](https://www.youtube.com/watch?v=o9pEzgHorH0)).

I disagreed with their advice that code should be sorted such that
functions are all defined before they are used. I've always preferred
sorting by level of abstraction so that reading from top to bottom gives
you the big picture first, followed by the details. You don't put your
module docstring at the end of the file as the big reveal of what the
module is about, right? It seems like the code should follow the same
princple.

Awaken your home: Python and the Internet of Things - Paulus Schoutsen
----------------------------------------------------------------------

This talk was mainly about a project called
[home-assistant](https://home-assistant.io/), which serves as a hub for
a multitude of incompatible home automation devices. The architecture
was kind of interesting, and I'd like to look into a few things
mentioned (like "entity tracking") when I've got some time.

The cobbler's children have no shoes, or building better tools for ourselves - Alex Gaynor
------------------------------------------------------------------------------------------

Alex is a director of the Python Software Foundation, and works for the
U.S. Government. He talked in general about writing simple tools that
can make developers' lives easier, then gave some specific examples of
ideas for this. One such example is having a script fetch HTTPS
certificates to check their expiration and automatically log an issue
when they're approaching time to be renewed.

This talk brought to mind the idea from *[The Phoenix
Project](https://www.goodreads.com/book/show/17255186-the-phoenix-project)*
that improving daily work is more important than doing daily work.

Interlude - Live captioning
---------------------------

New to me in terms of tech conferences is that the talks are being
professionally captioned in real-time. That is, there is a stenographer
typing what the speaker is saying, projected on an alternate screen.
That way deaf people and those for whom English is a challenge can
follow along more easily. In this room the stenographer was typing even
the pre-talk moderator telling folks that they're horrible people if
they don't slide in to the centers of chair rows to make room for others
coming in. When he noticed this, he said, "Hey, they're typing
everything I say!"

HEY, THEY'RE TYPING EVERYTHING I SAY.

"Python!"

PYTHON

"Sesquipedelian!"

\[pause\] (SORRY)

That got some laughs.

![Pendulum]({static}/images/pycon-pendulum.jpg)

Pythons in a container - Lessons learned Dockerizing Python micro-services - Dorian Pula
----------------------------------------------------------------------------------------

Dorian works for a company that provides support for loyalty programs,
and he says they use lots of Flask REST micro-services that each get
their own Docker container. Several of the lessons learned were things I
had learned myself Dockerizing my
[chorebot](https://github.com/genericmoniker/chorebot) project, though I
still consider myself a Docker noob. I appreciate that he pointed out
"docker-compose logs \$SERVICE". I've kind of wondered about the right
way to check on application health.

To mock, or not to mock, that is the question - Ana Balica
----------------------------------------------------------

I was very interested in this talk since I often worry about the right
level of mocking in tests. It seems like an essential tool for true unit
testing, but there are certainly times that it can actually subvert your
testing efforts and test maintainability.

Ana showed examples of using mocks in tests from open source projects,
and explained why they were "good" mocks. They mocked system state,
streams, networking, time, and unpredictable things. When covering "bad"
mocks, the issues were more focused on accidents using the mock library
(of which I've done them all, I think). I kind of wish there had been
more detail about ways in which mistake-free mocking can still be bad.

One interesting piece of advice was to only mock types you own. This was
from the book *[Growing Object-Oriented Software, Guided by
Tests](https://www.goodreads.com/book/show/4268826-growing-object-oriented-software-guided-by-tests)*.
That seems counter-intuitive to me. Don't you want to mock third-party
stuff? I guess the issue is the danger of pulling implementation details
of that third-party dependency into your tests, and that there ought to
be an abstraction in your own code that you mock instead. I need to dig
into that more.

Let's read the code: the requests library - Susan Tan
-----------------------------------------------------

This talk was about strategies for reading code generally, using Kenneth
Reitz's requests library as the specific example. In summary, get the
code into an editor/IDE for quick navigation, get it running so you can
use a debugger, and start small. Maybe just figure out how one
particular unit test works, then keep asking questions and digging
deeper to find the answers.

Lightning Talks
---------------

The final event of the day was the lightning talks. People sign up at
the conference to give these brief talks about nearly anything, but with
some sort of selection process. Some talks were funny. I especially
liked Travis Morton's ["compromise"
library](https://github.com/TravisJMorton/Compromise). Can't decide
whether to start indexing at 0 or 1? How about a list where the first
element is the perfect compromise, at .5? Or there's the semi-immutable
collection. The first time you try to change it, you get an exception.
But if you really insist (by trying again), then OK, it works.

Some talks were serious, like Russell Keith-Magee who talked about
battling depression, and the stigma associated with it that prevents
people from seeking treatment.

I can understand why some people rank the lightning talks as their
favorite part of the conference.

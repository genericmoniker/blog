Title: PyCon US 2022
Date: 2022-05-01 19:35
Author: Eric
Category: Event
Slug: pycon-2022
Status: published

![Welcome to PyCon!]({static}/images/pycon-2022-welcome.jpg)

I wrapped up my participation in this year's PyCon last night. Being in Salt
Lake City was great, since that's just a half-hour drive from my house, but it
also means that I don't have the "completely focused on this" experience that
traveling to a conference gives you. For example, I was on the verge of signing
up for the PyLadies auction when registering for the conference, but then I
thought I should probably just go home to my own ladies (wife and daughter)
instead. And church and family commitments made it hard to attend anything
today (Sunday).

Attending PyCon is a chance to learn, meet people, and feel the sense of
community from a shared enthusiasm for a programming language... odd as that
may seem. The Salt Palace Convention Center was simultaneously hosting a
gymnastics competition, and a mom walking down the concourse with her gymnast
children wondered aloud, "What is PyCon???" I considered stopping to answer her
question, but I wasn't sure she really wanted to be accosted by a tech nerd.

![Registration]({static}/images/pycon-2022-registration.jpg)

*The registration desk, where I volunteered for a couple of hours.*

## Keynotes

The first keynote was from Łukasz Langa, the Python Software Foundation's
Developer in Residence, and who is also known for creating the code formatting
tool [Black](https://github.com/psf/black). His talk was pretty technical for
a keynote, covering type annotations and how they make reading a codebase
easier. Some people argue that type annotations are ugly and obscure the code,
but Łukasz argued that if the annotations are ugly, that is an indication that
the code may be ugly too. He gave some tips on making annotations (and the
code) better such as by avoiding primitive obsession (everything is a str!)
applying Postel's [robustness
principle](https://en.wikipedia.org/wiki/Robustness_principle) and using more
recent Python versions where simpler annotation syntax has been introduced.

Sara Issaoun, a NASA Einstein Fellow and astronomer spoke about imaging a
super-massive black hole as part of the Event Horizon Telescope project. The
image became famous when dozens of major news agencies put it on their front
pages (or digital equivalents) in 2019. I had watched the Netflix documentary
about this, *Black Holes, The Edge of All We Know* so was familiar with the
project. Sara said that Python is a pillar of modern science, and enabled much
of the data analysis. She also teased that there will be an announcement from
the project on May 12 related to our own Milky Way galaxy.

Peter Wang, from Anaconda, announced an alpha release of
[pyscript](https://pyscript.net/), a Python distribution targeting the browser.
It is built on top of [Pyodide](https://pyodide.org). The goal is to make
Python programming accessible to as many people as possible by building
applications in a browser. Favorite random quote from the talk: "If you bash
your head into the wall enough it will eventually turn into a pile of yaml."

![Wildflowers on the Ensign Peak
Trail]({static}/images/pycon-2022-ensign-peak-trail.jpg)

*Wildflowers on the Ensign Peak Trail.*

## Talks

I went to a bunch of talks, but I'll just mention some favorites.

Brandt Bucher talked about structural pattern matching, which is a new language
feature as of Python 3.10. As co-author of the
[PEP](https://peps.python.org/pep-0634/) (along with Guido) and implementor, he
was able to talk authoritatively on the subject. A couple of his main points:
It is not a switch statement! And please read the [tutorial
PEP](https://peps.python.org/pep-0636/) which introduces the concepts by
writing a text-based adventure game.

John Reese, who builds developer tools for Meta, titled his talk "Open Source
on Easy Mode", but had lots of good suggestions for *any* project in terms of
tools and project configuration. Since he is the maintainer of
[μsort](https://github.com/facebookexperimental/usort), I asked for his take on
why we bother sorting imports at all. He gave a couple of reasons: Sorted
imports are easier to find by visual scanning, and having an automated
consistent ordering discourages developers from wasting time micromanaging
their imports by hand.

Based on the title alone, Jason Fried's talk "If an asyncio.Task fails in the
woods and nobody is around to see it, does it still page you at 3am?" you can
tell there's some humor involved. He gave some practical advice on alternatives
to asyncio anti-patterns he's seen (use `asyncio.run()`!), along with a sliding
scale of the probability of something breaking vs. how inconvenient it is to
the person who has to fix it. For example, probability of something breaking on
your dev machine: 0. Probability of something breaking in production when
you're on vacation during a major holiday: almost guaranteed.

I [mentioned meeting Bruce Eckel]({filename}/pycon-2016-day-2.md) at the last
PyCon I attended six years ago. He spoke about dataclasses, and how their use
can tidy up some awkward code, especially in the context of verifying pre- and
post- conditions. I've been stuck on Python 3.6 at work, so I haven't had much
opportunity to use dataclasses yet, so it was nice to learn from his
experiences.

As a side note, there was generally not a Q&A time after any of the talks.
Presenters were instead encouraged to meet with people in the hallway to answer
questions. I think that is a great format and I hope they keep it that way in
future PyCons. Bruce *did* ask if people had questions at the end of his talk,
and it was just evidence for why it isn't awesome as he got stuck trying to
hear and understand a question from a non-native English speaker and failing to
communicate. Having lived in a country where I was not a native speaker, I
appreciate and sympathize with them, but the likelihood of meaningful discourse
is much higher one-on-one than trying to shout across a large conference hall.

I coincidentally had lunch with Roman Yurchak and Hood Chatham before their
talk on Pyodide (thanks for the apple, Hood!). After Peter Wang's keynote about
pyscript, I was curious about some of the underlying details. What makes it
possible is compiling CPython to WebAssembly. In addition to loading Python
script files, they also have the ability to install pure Python packages via
"micropip", as well as some popular packages that rely on extensions, such as
NumPy and SQLAlchemy. There is also a foreign function interface with
Javascript. I haven't dug into WebAssembly, but I sort of imagined that
becoming the universal runtime with Javascript as one of many possible sources.
I don't think that's reality (?). My impression is that the Pyodide project has
taken on a huge challenge, and I hope it works out.

I think I would listen to A. Jesse Jiryu Davis on about any subject. His talks
are always well-prepared and polished. This one was about async vs. threads,
and that subject reminds me of [this YouTube
video](https://www.youtube.com/watch?v=bzkRVzciAZg) (which is hilarious but
has a few F-bombs). Yes, async is hip, and it is great for some situations, but
sometimes its proponents fall into the trap of saying "new thing Y" is in all
ways superior to "old thing X" rather than conceding that there are nearly
always trade-offs. Jesse said that locks and events *are* kind of ugly, but
showed how using `ThreadPoolExecutor` and `Future` can lead to beautiful and
simple threaded code.

The last talk I want to call out is Anthony Shaw's, on writing faster Python
code. He recommended the [Austin](https://github.com/P403n1x87/austin) and
[Scalene](https://github.com/plasma-umass/scalene) profilers for measurement,
and then gave some specific examples of performance differences coding the same
thing in different ways. A lot of Python devs are aware that comprehensions are
faster than `for` loops, but it was a surprise to nearly all of us in the room
that custom classes are generally faster than named tuples.

![Salt Palace Convention Center]({static}/images/pycon-2022-salt-palace.jpg)

*Inside the Salt Palace Convention Center.*

## Hallway track

Getting the chance to meet people is a pleasant bonus for attending PyCon. I'm
very much an introvert, but push myself to sit with and talk to people I don't
know at meal times. Sometimes conversations are bumpy at the start ("How's your
PyCon going?") but then you find something to connect on and the initial
awkwardness is worth it. Among many people and conversations, I met a woman
who had traveled from Nigeria to the conference, talked to a guy who had done a
tutorial on network analysis, heard a discussion about working in academia vs.
industry, got a lead on potential job opportunities for my son who just got a
C.S. degree this week.

In the conference opening, Emily Morehouse talked about being inviting and
welcoming, specifically by always leaving an opening in a circle of
conversation for someone else to join. I got to take advantage of such an
opening when I stepped in for a few minutes of conversation with Guido van
Rossum, Barry Warsaw, Łukasz Langa and a few others while they talked about the
keynotes from Saturday morning. I didn't volunteer much (I'm an introvert,
remember?) but it was still fun to be an average guy in that circle of really
smart and distinguished people.

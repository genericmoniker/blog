Title: QCon SF 2008 Day 1
Date: 2008-11-19 23:22
Author: Eric
Category: Event
Slug: qcon-sf-2008-day-1
Status: published

QCon is a software development conference sponsored by the
[InfoQ](http://www.infoq.com/) site and software consultancy
[Trifork](http://www.trifork.com/). I am in San Francisco attending it,
and here is a summary and some thoughts on the first day's sessions I
was able to attend.

![San Francisco Buildings]({static}/images/qcon-3.jpg)

Agilists and Architects (Martin Fowler & Rebecca Parsons)
---------------------------------------------------------

As much of Martin Fowler's stuff as I've read, I hadn't ever heard him
speak in person. He and Rebecca talked about software architects,
including some of the stereotypical ivory tower thinkers that come up
with beautiful, elegant systems that have no possibility of actually
working in the real world. A video clip from *The Matrix Reloaded* set
the tone: the architect of the matrix considers Neo to be an aberration
in his otherwise mathematically perfect construct.

Part of the problem with architecture is that it is hard to define. It
may be simply design when we want to make it sound more important. I
remember a guy I used to work with for whom everything was architecture.
"If you think about the architecture of these two classes..." Martin
liked Ralph Johnson's definition of an architect as the person who
thinks about the hard stuff -- whatever that happens to be for a
particular organization.

Another problem is that architects have a hard time defining success for
their role, and an even harder time attaining it. Sometimes that's
because of organizational dysfunction, like companies that insist that
architects not write any code. Other times it is through poor practices,
like inventing frameworks in anticipation of a yet unproven need.

The speakers emphasized, however, that architecture has a useful role in
spite of some of the difficulties with having it filled effectively. The
architect is the one who worries about supportability, rampant
proliferation of tools, and keeps in mind the grand vision of the
product. They are also responsible for the quality of the code, which is
*not* just an abstract, academic thing once the code works. The quality
of the code has a real cost that is realized when new features need to
be added. It can be hard to make that cost visible to people, but one
approach suggested might be to give two estimates: one for the new
feature built into the mess we've currently got and one for the
imaginary clean system we wish we had. I don't know, that still sounds
kind of hard.

Web as Platform (John Musser)
-----------------------------

John is the founder of
[Programmableweb.com](http://www.programmableweb.com), a sort of catalog
site for various APIs available over the Internet. In his presentation,
he talked about trends in web APIs. Some trends are technical such as
the rising use of REST vs. SOAP (though since REST is more a philosophy
than a standard, it can be hard to classify something as REST as opposed
to REST-ish). Other trends are around the ubiquity of APIs -- it is now
expected that if you put useful functionality on the web that it will
have an API, and not just a user interface. Even media producers like
[The New York
Times](http://blog.programmableweb.com/2008/06/10/the-new-york-times-api-all-the-news-thats-fit-to-mix/)
and
[NPR](http://www.npr.org/blogs/inside/2008/07/npr_api_is_live_on_nprorg.html) have
APIs.

What makes a good web API? First and foremost, the underlying service
has to be valuable. Beyond that, the API should support the business
model of the provider (eBay wants to optimize adding listings since
that's how they make money) and should be easy to access both in terms
of openness and the developer support provided.

![San Francisco Buildings]({static}/images/qcon-1.jpg)

Hard Rock: Silverlight 2 (Scott Stanfield)
------------------------------------------

Scott is the CEO of [Vertigo](http://vertigo.com), a consulting firm
that was named Microsoft partner of the year for 2008. It was nice to
have some Microsoft technical representation since the conference so far
seems heavier on the Java side. Scott spoke about building the [Hard
Rock Memorabilia](http://memorabilia.hardrock.com/) site working with
marketing firm Duncan/Channon. Duncan/Channon originally intended that
the site be done using Flash, but Deep Zoom turned out to be the killer
feature that made Silverlight the clear choice.

Scott said that the Silverlight story of independent graphic design and
programming is completely playing out as advertised. He showed a little
demo of an Etch-A-Sketch app that Vertigo programmer Michael Moser
quickly coded up, but was then beautifully skinned by a graphic artist.

Scott also asserted that the adaptive streaming of video in Silverlight
gives the best video on the web.

One interesting tidbit on the Hard Rock site is that Vertigo spent some
significant effort getting a set of different sized pictures to line up
in such a way that the final arrangement creates a nice rectangle. This
looks like possibly a variation of the [packing
problem](http://en.wikipedia.org/wiki/Packing_problem) to me.

Also interesting was that Scott was using a Mac with Vista running in a
VM. Come to think of it, all the presenters in the RIA track seemed to
have Macs.

Flex and AIR in the Trenches (Scott Delap)
------------------------------------------

Scott Delap gave a presentation about using Adobe tools to build some
online components of a video game, [League of
Legends](http://www.leagueoflegends.com/). His perspective was
comparing Flash/Flex to doing Java UI development with Swing. He seemed
reasonably happy with the platform and development tools, but thought
that things felt sort of like Java year 2000. That is, not quite up to
state-of-the art. He is, however, a convert to declarative UI
specification. Like the Java UI developers I've known, he never really
trusted visual designers for Swing, but says the designer experience
with Flash is great.

Scott talked about evaluating a lot of frameworks for various things
(dependency injection, remoting, unit testing, functional testing, etc.)
which is a typical exercise for open source development stacks.

10 Ways to Improve Your Code (Neal Ford)
----------------------------------------

This talk covers some of the same material that is in Neal's book *[The
Productive
Programmer](http://www.amazon.com/Productive-Programmer-Theory-Practice-OReilly/dp/0596519788)*.
I sort of got the impression that maybe after writing a book and
giving this presentation who knows how many times that Neal might have
lost some of the passion associated with this topic. That's not to say
that the presentation was dull, it just seemed a little like, "OK, here
we go again..."

Neal's 10 points were mostly things I know (and even *do* successfully
at times) such as TDD, using static analysis, YAGNI, etc. There was an
interesting point on polyglot programming. He said that polyglot
programming ideally doesn't mean multiple platforms, but multiple
languages on a single platform. Java and .NET are both multilingual
platforms, so take advantage of that to use the best language for the
problem at hand while still keeping the benefits of a common runtime
environment.

As an intermission, Neal talked about 10 bad smells, my favorite of
which was "Our lawyers say we can't use any open source software", which
led to Neal having to buy a "license" for CruiseControl (written by
Neal's employer, ThoughtWorks) so he could use it with a client.

![San Francisco]({static}/images/qcon-2.jpg)

Real World GWT (Alex Moffat)
----------------------------

In short, Alex and his team *love* GWT. And I have to say that seeing
[Blueprint](http://blueprint.lombardi.com/index.html) in action was
pretty spectacular. It really looked like a desktop application, but
done entirely with HTML and Javascript. GWT is the magic behind it all,
which is Google's toolkit for compiling Java to Javascript.

If you work in a Java shop, it seems like a great development story: use
all your familiar tools and write Java code and you get a great web app.

Just You Wait (Kent Beck)
-------------------------

Kent Beck, like Martin Fowler, is another industry heavyweight that I
first heard speak today. He got started a little late because his talk
came right after the break in which beer was served, and I guess it's
hard to compete with that. Being a non-drinker, I had a seat right up
front.

His talk was as an amateur futurist, looking at trends and imagining
where they might go, and unintended consequences. For example, what
happens if you extend the trend of releasing software more frequently?
Maybe releasing software with every keystroke? Well, OK, editing a live
web site would almost be that (if your editor saved continuously).

Some other trends he expects are the end of "free" stuff on the web, and
a decrease in status for programmers as other people begin to understand
technology more and programming seems less mystical. Even if that latter
point proves true, he says that we can still make a difference in the
world with what we build, and how we build it.

Thinking of the Brazilians that were recognized in attendance, I
flinched a little during the talk when Kent digressed slightly about how
his son says "cool", but to be really cool leaves off the 'L'. There's
another unintended consequence for you, riffing on a word that is vulgar
in Portuguese.

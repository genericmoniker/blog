Title: PyCon 2016 - Day 2
Date: 2016-06-01 00:30
Author: Eric
Category: Uncategorized
Slug: pycon-2016-day-2
Status: published

Today's PyCon was a lot about meeting people. I hadn't really
anticipated that, but it was a nice surprise nonetheless. But first
things first...

![Convention Center]({filename}/images/pycon-conv-center.jpg)

Lightning talks (AM)
--------------------

There were two sets of lightning talks today, book-ending the rest of
the events. One interesting one was about using Minecraft to teach
Python. That could definitely be a way to approach my kids about
programming.

There was also a talk about operator overloading, and language
designers' alternation between operator overloading being OK (C++,
Python), then having a backlash against crazy operator overloading such
that it isn't allowed at all (Java, Go). The speaker came up with some
guidelines for non-crazy overloading, such as not doing I/O in an
overload operator.

Keynote - Guido van Rossum
--------------------------

Guido gave a small "state of the language" talk in which he shared some
of the new things that are out in Python 3.5 (better coroutine support,
matrix multiplication, new unpacking syntax and gradual typing). Things
coming in 3.6 are yet [another way of formatting
strings](https://www.python.org/dev/peps/pep-0498/) (which actually
looks pretty cool), a protocol just for [file system
paths](https://www.python.org/dev/peps/pep-0519/), and a cryptographic
random number module called secrets.py.

He also said that Python's source repository will be moving to GitHub
later this year. It wasn't too long ago that Python moved from
Subversion to Mercurial. The thought was that Mercurial seemed more
similar to Subversion when compared with Git, and nobody could figure
out Git's branching. But times change, and Guido said, "Everybody knows
Git branching, and somehow everyone is born with a GitHub account." So
Git it will be.

The future beyond 3.6? Who knows? Maybe the GIL will be removed. Ha.

He also acknowledged a typo of "femail" in his last year's keynote, and
despite spelling errors, is still trying to find women who want to be
core contributors to the language.

The rest of Guido's talk was taken from a speech he had given to Dutch
officials in a "King's Day" event, and was mostly autobiographical and
about the history of Python and the community that has led to its
success.

Keynote - Parisa Tabriz
-----------------------

Parisa works for Google on the Chrome project, and has the title
"Security Princess". She talked about hacking as a skill set and mind
set. Whereas the engineering mentality is to figure out how to make
something that works, the hacker mindset is to push boundaries and use
things in unintended ways. She feels like developers should foster the
hacker mind set in order to make things better.

The bulk of her talk was about what motivates hackers, such as the
challenge of breaking something, wanting to say something, wanting
money, and wanting information.

She shared the site <http://xss-game.appspot.com>, which is a game
created by Google to teach you how to find cross-site scripting bugs,
which looks like fun.

Click: A pleasure to write, a pleasure to use - Sebastian Vetter
----------------------------------------------------------------

[Click](http://click.pocoo.org/) is a library for creating CLIs written
by Armin Ronacher, the creator of the [Flask](http://flask.pocoo.org/)
framework. It looks pretty cool, using a decorator approach to parsing
and validating arguments. While not a focus of the talk, there was
mention (and some strong audience support) for
[docopt](http://docopt.org/), which is yet another alternative to the
standard ArgParse module. I'm interested in taking a look at that as
well.

![Roses]({filename}/images/pycon-roses.jpg)


Podcast Open Space
------------------

I've been listening to a couple of Python podcasts for a while: *[Talk
Python to Me](https://talkpython.fm/)* and
*[Podcast.\_\_init\_\_](http://podcastinit.com/)*. The hosts, Michael
Kennedy and Tobias Macey, held an open space that I attended with dozen
or so other people to meet them and chat about their shows.

It was kind of fun to attach real people to the voices I've heard, and
hear some details about the process of getting guests and recording
their shows.

Shipping software to users with Python - Glyph
----------------------------------------------

This is one of the talks I was most interested in going to. Getting
applications shipped to users is certainly an area of weakness for
Python, and something we struggle with at work. Furthermore, the talk
was given by Glyph, the creator of the Twisted library, and when you
have such a cool first name as Glyph, you can just go by that.

I had hoped that the talk would focus most on shipping applications to
end-users, but he covered the whole gamut of getting Python code into
"production". It was all good stuff, though, including dispelling the
myth that if you're using Docker you don't need to worry about isolating
your Python environment from the container.

He did mention [cx\_Freeze](http://cx-freeze.readthedocs.io/en/latest/),
which I've been investigating, as well as some other projects like it
that I'm aware of and decided not to pursue because of lack of
cross-platform support or Python cross-version support. I fully agreed
with his statement of application developers' goal: to make our users
not care about Python. Shipping a Python application should be like
shipping any native application. He said that it really isn't that hard,
and we shouldn't go out and rewrite our apps in Go because of a few
bumps.

Daniel (my coworker also attending the conference), my son Ethan and I
literally chased Glyph down after his talk to ask some more questions.
Mostly, is what we're doing -- namely shipping Python apps to Windows
and Linux -- so unusual that the tooling can be so rough? He didn't
think our situation was rare, but pointed out the realities of open
source software projects. Sometimes someone has a need that they meet
with some code, and share it to the world. Then tons of people start
using it and it becomes overwhelming, and a mostly thankless job.

He (and Augie Fackler, who also joined in the discussion) pointed out
the great strides recently with the Python Packaging Authority, but
they're mostly ignoring the cx\_Freeze scenario for now. I guess maybe
it is a situation where if I want improvement, I need to pitch in.

People
------

After the conversation with Glyph, we'd already missed much of the next
talk we planned to attend, so Ethan and I wandered toward the exhibit
hall. We happened upon Guido chatting with a small group of conference
attendees. He was wearing a shirt that said, "Python is for girls" in
support of his desire for greater diversity in the community. I asked
him if I could take a picture of it, since my 10 year old daughter tends
to think programming is kind of a boy thing. Guido said that what I
needed to do was to absolutely forbid her from doing any programming,
and that would pretty much seal the deal of her getting interested.

![Guido van Rossum]({filename}/images/pycon-guido.jpg)

Also in that little group of people was Luciano Ramalho, author of
*[Fluent
Python](https://www.goodreads.com/book/show/22800567-fluent-python)*,
which I happen to be reading right now. He gave some advice about
reading strategy since it is such a thick book -- to kind of treat it
like several separate books. I told him I was reading the ebook version,
so I hadn't realized that I should be intimidated by it's length. I also
got to speak a little Portuguese since Luciano is from Brazil, where I
was a missionary for a couple of years.

I was also delighted to meet another author who appeared there, Bruce
Eckel. I told him about reading his *[Thinking in
Java](https://www.goodreads.com/book/show/71672.Thinking_in_Java)* book
years and years ago, and we had a nice chat about the fact that he's
also a Python enthusiast, and that he hopes to write a book on Python
concurrency soon.

I've also passed people in the halls and done double-takes because
they're speakers whose talks we've watched at work. It somehow feels
like encountering a TV star, even if celebrity in the Python community
isn't quite on the same level :-)

From developer to manager - Sean O'Connor
-----------------------------------------

I went to this talk because of a more formal leadership role I've been
playing at work. Sean made the comment right up front that there might
be a couple of animated GIFs in his slide, which turned out to be an
understatement. The talk was fun and approachable.

One key bit of advice he gave: Think about what makes you happy at work,
and get more of that. That can help you decide if pursuing management is
even a good idea compared to staying purely on the technical side.

The computer science of marking computer science assignments - Katie Bell
-------------------------------------------------------------------------

Katie works for an Australian company that develops educational software
for school kids. The software uses the [turtle graphics
module](https://docs.python.org/2/library/turtle.html) from Python, and
then has an automated way of giving feedback on the assignments based on
whether the finished drawing matches the assigned drawing.

She talked about the challenges and algorithms of doing vector graphics
diffing, and trying to optimize performance. In a twist on the
conventional wisdom of optimization, she said that changing to different
algorithms didn't help, just writing a critical piece in C did.

Dispelling the "genius programmer" myth through code review - Ashwini Oruganti
------------------------------------------------------------------------------

This talk had smatterings of the fixed vs. growth mindset ideas, but
went down the path of contribution to open source projects. It is really
a clever idea: If there is a programmer that you admire and want to
learn from, what better way than to contribute to their project and
learn from the feedback you get on pull requests?

Lightning talks (PM)
--------------------

The evening lightning talks were fun. José Castro posed the question,
"What if you did 'chmod -x chmod'? How could you fix it?" Then he showed
various crazy ideas of how to change file permissions when you can't run
the primary tool for doing so.

There happened to be two Nathaniel Smiths that spoke, and one talked
about generative poetry with a project called
[prosaic](https://github.com/nathanielksmith/prosaic). It was fairly
entertaining to see poetry generated from the scripts of movies.

Ian Lee, the maintainer of the pep8 tool, let us know that it is being
renamed to be "[pycodestyle](https://github.com/PyCQA/pycodestyle)" at
[Guido's request](https://github.com/PyCQA/pycodestyle/issues/466).

There was even a talk about pythons the snakes rather than the language.
Takeaway? "Punch bite" would be an awesome project name for something...

The most entertaining talk was by Larry Hastings, "My life as a meme".
Apparently there is this thing called "speed running" where people play
classic video games to get through levels as quickly as possible, and
they broadcast people doing this so that a hundred thousand bored
teenagers can watch. Larry happened to go to one of these events as a
spectator, and between plays, the camera was turned toward the audience.
Larry was sitting there playing a video game in the front row, and these
hundred thousand bored teenagers dubbed him \#dsdad and turned him into
a minor celebrity.

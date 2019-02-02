Title: I'm concerned about using Python
Date: 2017-06-03 07:48
Author: Eric
Category:Opinion
Tags: Python
Slug: im-concerned-about-using-python
Status: published

![xkcd Python](https://imgs.xkcd.com/comics/python.png)

But...
------

**Python is slow**

* Is the CPU the bounding factor for the project's performance?
* How much time has been spent trying to optimize performance?
* Which is currently more important, raw execution speed or time to create features?
* Is Python fast enough for the project?
* It is an often used strategy to write performance critical code in C or
  Cython -- and no, that's not cheating, it's how the language is meant to be
  used. 
* Maybe PyPy?
* [It really doesn't matter](https://hackernoon.com/yes-python-is-slow-and-i-dont-care-13763980b5a1)

**Significant whitespace? Seriously?**

"Oddly enough, Python's use of whitespace stopped feeling unnatural after about
twenty minutes. I just indented code, pretty much as I would have done in a C
program anyway, and it worked." -- [Eric Raymond](http://www.linuxjournal.com/article/3882)

**Python doesn't really have threads**

* Python threads are real, operating system threads
* The GIL limits thread effectiveness (see the item about multiple cores)
* Multiprocessing and bits of native code are some work-arounds
* [Threads are evil anyway](https://www.google.com/search?q=threads+are+evil) ;-)

**Python can't take advantage of multiple cores**

* This is true for a single-process, multi-threaded application
* Multiprocessing can be a way to address that, if needed
* Does it matter for the project?

**Python is big**

* The Python interpreter itself is < 3 MB
* The standard library .pyc files, frozen, for a fair sized project is < 5 MB
  as a zip file (not counting .pyd -- native compiled library files)
* The Visual C++ 2013 runtime shows as 17.1 MB on my machine
* Throw in some Qt DLLs and you've got several more MB
* JREs tend to be 30+ MB
* .NET frameworks even bigger

**Python uses too much memory**

* Maybe? How much is too much?
* Compared to what? What are the other tradeoffs of said other thing?

**Python is hard to deploy as installed software**

* Agreed that this has not been a focus of Python
* To the point that some companies that do it consider how they do it a trade
  secret (Dropbox)
* Freezing helps address this, but because of the lack of focus, solutions are
  a little crufty
* Glyph Lefkowitz [argues](https://www.youtube.com/watch?v=5BqAeN-F9Qs) that
  it is not hard, just confusing, and those aren't the same thing

**Python has errors at runtime that other languages detect at compile time**

* Yes
* You'll need good test coverage 
* You could look into type annotations if you want (but duck typing is pretty
  cool)
* If you want to know about problems as soon as possible… In some situations it
  can take less time to run a comprehensive Python unit test suite than it
  would to *compile* equivalent code in a different language
	
**Python code reveals its implementation**

* All executable code reveals its implementation (by definition), it is just a
  question of ease/readability
* DropBox went to lengths to protect their Python code, raising the bar, but a
  determined attacker will get it
* Java/C#/Ruby all have the same problem of being on the easier end of the
  spectrum

**Python isn't very popular, it is hard to find engineers**

* Python is #2 on the PopulariY of Programming Language index ([PYPL](http://pypl.github.io/PYPL.html))
* Python is #4 on the TIOBE index, up from #8 in 2015
  ([TIOBE](http://www.tiobe.com/tiobe_index))
* Python is the most popular introductory language at top U.S. Universities ([ACM, 2014](http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext))
	
**There isn't much user-installed software using Python**

* This is true, probably for deployment reasons, but there are some notable
  applications:
    * Dropbox client (400 million registered users)
    * Sublime Text
    * BitTorrent
    * Anki
    * Mercurial
    * Blender

**I want to debug the full stack, even if there's native code**

* Python Tools for Visual Studio supports mixed Python/C++ debugging
* You can also attach a debugger to a Python process and debug native code it
  calls

**I don't feel like a real programmer unless I'm writing native code**

* I like understanding complicated things because it proves I'm smart
* "Real programmers don't need abstract concepts to get their jobs done: they
  are perfectly happy with a keypunch, a FORTRAN IV compiler, and a beer." From
  <http://www.ee.ryerson.ca/~elf/hack/realmen.html>

![xkcd Real Programmers](https://imgs.xkcd.com/comics/real_programmers.png)

Counter
=======

Every programming language has its strengths and weaknesses. You need to
consider the characteristics of the alternatives, not just pretend like there
is a magic language that has no downsides. For example:

**C++**

* Manual memory management can be error prone (leaks, double-free, dangling
  pointer, mismatch allocator / deallocator)
* No runtime checks of things like buffer overruns, array bounds, bad pointer
  dereference (resulting in undefined behavior)
* Hard to get a good stack trace on error / crash "Unless you are a total
  assembler programming guru, you are dead in the water without some form of
  debug symbols when trying to figure out where an application crashed." From
  <https://www.microsoft.com/msj/0498/bugslayer0498.aspx>
* Exceptions are implemented such that they have a significant performance
  penalty
* Bugs often result in security exploits
* Complex build environment
* Redundancy of header and source files -- but not complete -- you still have
  to read both files to understand a type
* Slower edit/run cycle due to slow compilation/linking
* Requires explicit recompilation per platform
* Inscrutable template error messages
* Drastic style forks with Qt, Boost/STL, pre-STL
* STL design emphasizes performance over readability
* Can be hard to debug third-party code
* Have to put semi-colons at the end of every line? Seriously? ;-)
* Eternal arguments about where to put the braces
* [C++ quotes](http://harmful.cat-v.org/software/c++/)

![xkcd Compiling](https://imgs.xkcd.com/comics/compiling.png)

>I often think of C++ as my own personal Pit of Despair Programming Language.
Unmanaged C++ makes it so easy to fall into traps. Think buffer overruns,
memory leaks, double frees, mismatch between allocator and deallocator, using
freed memory, umpteen dozen ways to trash the stack or heap – and those are
just some of the memory issues. There are lots more "gotchas" in C++. C++ often
throws you into the Pit of Despair and you have to climb your way up the Hill
of Quality. (Not to be confused with scaling the Cliffs of Insanity. That's
different.)

-- [Eric Lippert](http://blog.codinghorror.com/falling-into-the-pit-of-success/)


**Why Python is awesome**

* All the downsides for C++ above are in relation to Python, so that is a
  starting point
* Rapid development
* Good testing capabilities 
* Good multi-paradigm support - OO, imperative, functional 
* Community - and w/o the pollution you get for things like JavaScript and PHP,
  where there are so many non-programmers that there is garbage all over the
  internet
* PyPI packages
* Ease of learning, tons of educational material (books, sites, etc.)
* Economy of expression
* Readability and beauty
* Interactive prompt
* Batteries included
* High-level protocols - iterator, wsgi, dbapi, 
* Whitespace - formatting matches the logic, it cannot lie
* List comprehensions (and set, dict, genexps)
* Generators with send(), throw() and close()
* Decorators
* Context managers - resource control, template method pattern
* BDFL - keeper of the vision, but lots of smart people involved
* Fun
    * Monty Python, after all
    * `import this`
    * `import antigravity`
    * `from __future__ import braces`
    * `import __hello__`
* "I haven’t yet found a language that manages to be easy for beginners,
  practical for professionals, and exciting for hackers in the way that Python
  is." -- Luciano Ramahlo

Some of the above from [Raymond Hettinger's PyCon 2013 talk](http://pyvideo.org/pycon-us-2013/keynote-3.html).

>When you're writing working code early as fast as you can type and your
misstep rate is near zero, it generally means you've achieved mastery of the
language. But that didn't make sense, because it was still day one and I was
regularly pausing to look up new language and library features!

>This was my first clue that, in Python, I was actually dealing with an
exceptionally good design. Most languages have so much friction and awkwardness
built into their design that you learn most of their feature set long before
your misstep rate drops anywhere near zero. Python was the first
general-purpose language I'd ever used that reversed this process.

--[Eric Raymond](http://www.linuxjournal.com/article/3882)


**What sucks about Python?**

* Slow (by itself) for CPU-intensive processing compared to things like C/C++
* `if __name__ == '__main__':`
* Standard library naming inconsistencies
* No constants
* Shipping an application that includes the interpreter
* The GIL
* Overly complex internal string representation in Python 3?

Other Resources
===============

**Execution speed**

>The argument is that the development speed benefits greatly outweigh the
additional processing time + server costs, especially when the company is
small. There are plenty of startups that will have great cost optimization from
the beginning, but if they get out-maneuvered by a faster-moving competitor, it
doesn't matter: the parameters of success don't matter if the magnitude is
zero.

>So we couldn't have afforded to *not* start with Python, I would say. At this
point, we potentially can't afford to switch away from Python given how much we
already have written in it. That said, the costs are being felt; there are
people experimenting with using other languages (Go, typically) for new
projects, and there are efforts like Pyston to try to bring the cost of Python
down.

>Also, I don't think t's right to say "Dropbox is IO bound". Any particular
request might be IO-bound, but if that's the case you simply turn up the
concurrency until the server as a whole is at the target utilization in some
metric. For some services that will end up being network bandwidth or disk IO,
but for many it's CPU. So at any given time, Dropbox does in fact have a large
number of cores running Python code.

--[Kevin Modzelewski, Dropbox Cofounder](https://www.quora.com/How-can-some-really-large-services-like-Dropbox-afford-to-use-Python-as-a-primary-language-if-its-one-to-two-orders-of-magnitude-slower-than-other-compiled-languages)

**Protecting code from reverse engineering**

"Is there a good way to handle this problem?" No. Nothing can be protected
against reverse engineering. Even the firmware on DVD machines has been reverse
engineered and
[AACS Encryption key](https://en.wikipedia.org/wiki/AACS_encryption_key_controversy)
exposed. And that's in spite of the DMCA making that a criminal offense.
Since no technical method can stop your customers from reading your code, you
have to apply ordinary commercial methods.

1. Licenses. Contracts. Terms and Conditions. This still works even when people
   can read the code. Note that some of your Python-based components may
   require that you pay fees before you sell software using those components.
   Also, some open-source licenses prohibit you from concealing the source or
   origins of that component.
2. Offer significant value. If your stuff is so good -- at a price that is hard
   to refuse -- there's no incentive to waste time and money reverse
   engineering anything. Reverse engineering is expensive. Make your product
   slightly less expensive.
3. Offer upgrades and enhancements that make any reverse engineering a bad
   idea. When the next release breaks their reverse engineering, there's no
   point. This can be carried to absurd extremes, but you should offer new
   features that make the next release more valuable than reverse engineering.
4. Offer customization at rates so attractive that they'd rather pay you do
   build and support the enhancements.
5. Use a license key which expires. This is cruel, and will give you a bad
   reputation, but it certainly makes your software stop working.
6. Offer it as a web service. SaaS involves no downloads to customers.

--[S.Lott, StackOverflow answer](https://stackoverflow.com/questions/261638/how-do-i-protect-python-code)

This doesn't really address competitors *learning* something from your code,
though.


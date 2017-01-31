Title: Python Packaging (2013 Edition)
Date: 2013-09-21 16:33
Author: Eric
Category: Uncategorized
Tags: Python
Slug: python-packaging-2013
Status: published

About a year ago, I set out to get a solid working understanding of
Python packaging, resulting in a lengthy blog post of what I learned.
There have been some significant course changes over that year such that
my original post is wrong in several regards.

Here's a summary of some of t [Python Packaging User
Guide](https://python-packaging-user-guide.readthedocs.org/en/latest/index.html)
is now *The Source of All Truth*. If you want to know what is going on, go
there. It is, however, still under construction.

* Setuptools and Distribute have now been merged, and the result is...
  Setuptools. Whereas Setuptools was "old and busted" and Distribute was the
  "new hotness", it is now the other way around -- so long as you're talking
  about the latest and greatest Setuptools (version &gt;= 0.7).

* Distutils2,
  which switched out setup.py for setup.cfg, and was on the verge of going into
  Python 3.3, was dropped.

* Pip continues as the distribution installer of choice, though, as indicated
in the [current
recommendations](https://python-packaging-user-guide.readthedocs.org/en/latest/current.html).

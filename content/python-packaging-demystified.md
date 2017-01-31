Title: Python Packaging Demystified
Date: 2012-08-25 16:43
Author: Eric
Category: Programming
Tags: Python
Slug: python-packaging-demystified
Status: published

**<span style="color: #ff0000;">IMPORTANT</span>**: Some of the
information in this post is now obsolete. Please [see
here]({filename}/python-packaging-2013.md).

Randomly take a couple of words from the following list, put them together, and
there's a decent chance you'll come up with something real involving Python
packaging.

-   setup
-   install
-   dist
-   distribute
-   tools
-   utils
-   easy
-   py

The packaging situation is kind of confusing with all the alternate
tools, libraries and methods, so I'm going to take a stab at clarifying
things -- for how it seems right now, anyway.

<!--more-->

 What is a package?
===================

Let's step back for a second to review some Python vocabulary. A single
`.py` file can be a *script* or a *module* -- the basic difference being
that a script is primarily meant to be run, while a module is primarily
meant to export useful stuff for scripts or other modules. Of course a
module can be executed too, typically with the
`if __name__ == '__main__'` pattern. A *package* is a group of modules,
providing some additional structure. In short, it's a directory with an
`__init__.py` and some other `.py` files in it.

 I don't think that's what I mean
=================================

This is where the vocabulary gets muddled. If you're familiar with
[PyPI](http://pypi.python.org) (pie-pee-eye), the Python Package Index,
you'll realize there's something more than directories with
`__init__.py` files. PyPI has what are correctly called *distributions*.
Sure, they're packages (colloquially), but include metadata,
documentation, and other stuff to make it easier to manage third-party
Python software on your machine.

Getting started
===============

The [distribute](http://packages.python.org/distribute/) page cuts
through much of the disutils, setuptools, easy\_install, soup with this
pithy graphic:

![pip distribute](http://python-distribute.org/pip_distribute.png)

OK, since the New Hotness sounds good, we just want
[*distribute*](http://packages.python.org/distribute/) and
[*pip*](http://www.pip-installer.org/en/latest/index.html). The graphic
even shows you how to get them if you're on \*nix. Observant readers
might notice that *pip* is being installed with *easy\_install* and say,
"Hey, wait a minute... *easy\_install* is on the Old and Busted list,
but we're supposed to use that first?"

It turns out that *pip *(a recursive acronym for "Pip Installs Python")
currently requires *distribute*, and *distribute* happens to include
*easy\_install*. With Python 3.3 (which, by chance, has gone to release
candidate status today), the features of the *distribute* package become
*distutils2* in the Python standard library, and *distribute* is headed
for the bit bucket. Sorry, this was supposed to be clarifying things,
but it's getting back into the realm of chaos. So for now, we'll press
forward with *distribute* as the Not-Totally-New Hotness, but workable
strategy for today.

If you're on Windows, you can just download distribute\_setup.py from
here:

<http://python-distribute.org/distribute_setup.py>

Then, as indicated above, you can run this from a command prompt:

    python distribute_setup.py

The install creates a `Scripts` subdirectory in your Python install
directory, and puts `easy_install.exe` in there. It would be a good idea
to add the `Scripts` subdirectory to your Windows `PATH`. The New
Hotness `pip.exe` goes in there too, once that's installed. If you go
the *easy\_install* route, you'll get a UAC prompt on:

    easy_install pip

Then *pip* will be installed. Alternatively, (and without the need for
UAC elevation) you can download the *pip* package directly from:

<http://pypi.python.org/pypi/pip/>

The download is way down at the bottom of the page as a `.tar.gz` file,
which isn't the most convenient format for Windows, but
[7Zip](http://www.7-zip.org/) can remedy that difficulty. Once the
archive is unpacked, you can install *pip* with this command from within
in the directory where the *pip* archive was unpacked:

    python setup.py install

Once you've done this, you may delete the contents of the unpacked
archive -- everything you need has been copied into your Python install.

Now you can use *pip* to search for packages on PyPI and install them.
For example:

    pip search tornado

This will find packages with "tornado" in their name or description,
which includes not only the package specifically named "tornado", but
related packages as well. Installing a package is, not surprisingly:

    pip install tornado

This downloads the Tornado web server and copies it into the
`site-packages` subdirectory of your Python installation
(`C:\Python27\Lib\site-packages` for example). Since `site-packages` is
in the Python `sys.path`, you can now import Tornado types from a Python
script located anywhere on your system. Uninstalling a package is
equally obvious:

    pip uninstall tornado

To see what packages you have installed, run:

    pip freeze

 Advanced pip
=============

"freeze" seems an odd verb for listing installed packages. This is
because there is more to it: You can "freeze" a set of packages with
version numbers that are all known to work peacefully together, creating
a requirements file that can be used to recreate that same environment
somewhere else. More details about this are in the pip
[documentation](http://www.pip-installer.org/en/latest/requirements.html).

Let's say you're *developing* a package and want to make that package
available to scripts on your system. I guess you could check your source
out right into `site-packages` such that it can be edited in-place, but
that seems awkward and unpleasant. Instead, you can install your package
with *pip* using "edit mode":

    pip install -e C:\Projects\Alert\dvsdriver

The path specified here is where my Python project resides from my
source control checkout. With the `-e` option, instead of copying the
package to `site-packages`, a [path configuration
file](http://docs.python.org/library/site.html) (a file with a `.pth`
extension) is created in `site-packages` instead. The `.pth` file adds
the `C:\Projects\Alert\dvsdriver` directory to the Python path, allowing
you to develop your package in its natural location while still making
it available for importing from other scripts.

You can also use *pip* to install packages from places other than PyPI,
including local files, URLs of alternate package indexes, and directly
from version control repositories.

Virtual environments
====================

If you get into the situation where you need one version of a package
for one script, and different version of the same package for another
script, you'll probably want to look into
*[virtualenv](http://www.virtualenv.org/en/latest/index.html)*. This is
a package that lets you create multiple separate Python environments
that are completely isolated, so they can have different sets of
packages installed into them. The environments set up with *virtualenv*
already come with *distribute* and *pip* in them, so they're ready to be
populated with other packages.

 Creating Distributable Packages
================================

Now that we've got a sense of what distributable packages are and how to
use them, how do you create one?

The main thing is to create a setup.py module, which looks something
like this:

```python
from distutils.core import setup

setup(name='MyProject',
      version='1.0',
      author='Eric Smith',
      packages=['myproject'],
      )
```

Notice that we're importing from `distutils`, which means Old Stuff, but
it gives us a working package that can be managed with *pip*:

    pip install -e \Users\Eric\Projects\MyProject

There's good information about project structure, useful files (like
`README.txt`), additional metadata to include in the `setup` call, and
general package building in [The Hitchhiker's Guide to
Packaging](http://guide.python-distribute.org/creation.html).

Looking forward
===============

As mentioned previously, *distutils2* is nearly upon us. With that, the
`setup.py` script will be replaced by a declarative `setup.cfg` and all
previous libraries (*distutils*, *distribute*, *setuptools*) will be
deprecated. *Pip* will stick around, though.

So there's my attempt to clarify Python packaging. If I've made
egregious errors, please let me know and I'll fix them.

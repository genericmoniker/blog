Title: Granular Profiling in PyCharm
Date: 2015-12-02 19:30
Author: Eric
Category: Programming
Tags: PyCharm, Python
Slug: granular-profiling-in-pycharm
Status: published

PyCharm added profiler integration in [version
4.5](http://blog.jetbrains.com/pycharm/2015/05/meet-pycharm-4-5-all-python-tools-in-one-place/),
which I thought was pretty cool. Used [as
documented](https://www.jetbrains.com/pycharm/help/profiler.html),
though, it hasn't been terribly useful. Here's a way to improve on that.

<!--more-->

In my case, I was interested in profiling a web service -- specifically
requests to a particular resource. I started up the server application
using the profiler button on the toolbar, made a request to that
resource, took a snapshot and prepared to analyze some data.
Unfortunately, the profiler didn't think the request handler code was
even worth including in the call graph since it didn't take enough time.
Boo.

But... PyCharm can actually open *any* profiler snapshot made with
cProfile. A [blog
post](https://zapier.com/engineering/profiling-python-boss/) I had read
suggested making a decorator for profiling, so I wrote this:

```python
import cProfile
import functools
import os


def profile(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        try:
            profiler.enable()
            ret = func(*args, **kwargs)
            profiler.disable()
            return ret
        finally:
            filename = os.path.expanduser(
                os.path.join('~', func.__name__ + '.pstat')
            )
            profiler.dump_stats(filename)
    return wrapper
```

Put this decorator on a function, and it will create a .pstat file in
your home directory named after the function it decorates. For example:

```python
@profile
def handle_get(request):
    # etc.
```

After running the function, there would be a handle\_get.pstat file in
my home directory.

Now I can use **Tools | Open CProfile snapshot** in PyCharm and analyze
timings and the call graph just for the function that I'm interested in.

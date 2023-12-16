Title: Your right margin is telling you something
Date: 2014-07-26 14:53
Modified: 2023-12-16 10:18
Author: Eric
Category: Opinion
Tags: Python
Slug: your-right-margin-is-telling-you-something
Status: published

The recommendation to keep lines widths less than 80 characters is a
surprising part of the [Python style guide (PEP
8)](http://legacy.python.org/dev/peps/pep-0008/). Really, 79 characters?
Is it still the 1980's in Python-land? Maybe it's time to upgrade that
monochrome CRT and get some screen real-estate.

<!--more-->

Acting a bit on faith, and because my IDE kept squiggling my long lines,
I decided to give it a shot.

Python places great stock in readability, so one motivation for &lt; 80
is that wide lines are hard to read. That is absolutely true if you have
to scroll horizontally, and probably generally true within certain
ranges. After all, newspapers (yes, they still exist) are big but text
is put into fairly narrow columns for readability.

The bigger win I've discovered is a subtle hint that maybe I'm doing
something wrong. These things all become uncomfortable if you're trying
to fit in a narrow space:

-   Deeply nested functions
-   Long parameter lists
-   Very complex expressions
-   Overly verbose names
-   Excessive namespacing (e.g. `job.Job.JobType.BACKGROUND_JOB_TYPE`)

Of course, it can backfire a little, too, such as by encouraging overly
short variable names when a better, longer one doesn't fit.

But when I start to run up against the margin, it makes me pause to
think if maybe the code could be written in a better way. If so, great.

If not, a little wrapping is usually OK. Or just go long if it is really
the best choice.

PEP 8 does concede:

> Some teams strongly prefer a longer line length. For code maintained exclusively or
> primarily by a team that can reach agreement on this issue, it is okay to increase the
> line length limit up to 99 characters, provided that comments and docstrings are still
> wrapped at 72 characters.

So anything between 79 and 99 can be considered to follow PEP 8 when agreement can be
reached by a project's team, including [Black's default choice of
88](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#line-length)
. I've found that, especially as I've started using more type hints, that extra 10%
reduces excessive wrapping while still maintaining benefits of having a limit.

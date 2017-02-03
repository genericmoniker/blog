Title: Your right margin is telling you something
Date: 2014-07-26 14:53
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

Of course, it can backfire a little, too, such as by encouraging overly
short variable names when a better, longer one doesn't fit.

But when I start to run up against the margin, it makes me pause to
think if maybe the code could be written in a better way. If so, great.

If not, a little wrapping is usually OK. Or just go long if it is really
the best choice.

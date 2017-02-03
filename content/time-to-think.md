Title: Time to Think
Date: 2012-10-01 19:50
Author: Eric
Category: Opinion
Slug: time-to-think
Status: published

With time drawing short before a major deployment at work, we ran into a
problem. Some people testing our application reported it timing-out on
an important function. It quickly became a high priority that I was
assigned to solve.

<!--more-->

Since most of the people on our team work remotely, a group chat became
the primary channel for the problem. There were operations people
pointing out potentially significant log entries, QA and other
interested people reporting every instance of the problem happening --
or that they could not reproduce the problem all, ideas and theories
about what could be going wrong, and my boss asking what kind of help I
needed.

From this, and other similar experiences, I've learned a couple of
things to do in situations like this:

1\. Get a bug report
--------------------

In times of panic, it can seem like a bureaucratic waste of time to file
a bug report. But it is counter-productive to go chasing after a problem
without getting the best understanding available of what the problem
actually is. This is especially true in cases like this one where some
people were seeing the problem frequently and others not at all.

2\. Go dark
-----------

Of course you can't just drop out of sight when people are counting on
you to solve something quickly, but let them know that you just need
some time to think, and barring any breakthrough discoveries, that you
don't want to be interrupted for a bit.

With all of the chat messages coming through, I spent five hours chasing
after this and that without making much progress. Finally I came to my
senses and just ignored everything and took time to *think*. After some
time deeply analyzing one instance of the problem, it occurred to me
that I had written a program a couple of years ago to test this exact
scenario. Once I dusted that off and ran it a couple of times, the
problem became painfully obvious.

Honestly, I felt kind of dumb that it took me so long to figure it out,
but it reinforces how debilitating distraction can be.

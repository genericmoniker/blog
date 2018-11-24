Title: By Chance
Date: 2005-10-20 17:00
Author: Eric
Category: Project
Slug: by-chance
Status: published

A few years ago I was reading some books about biological evolution. At
some point, probably reading something by Richard Dawkins, I was
thinking about randomness and its ability to produce apparently
non-random things. All you need is a little pressure that selects one
random thing over another. So I wrote a little program that demonstrates
the idea by transforming a black box into a picture through entirely
random steps.<!--more-->

My program, ByChance, works like this. You supply an image that
represents the ideal in survivability. Once you've done that, you click
the "Start" button. The program starts with a black image with the same
dimensions as the "fitness" image you picked. It then proceeds to pick a
pixel in the image at random (around 200,000 possibilities, depending on
the shape of the image). Then it picks a random color (24 bits, so there
are around 16.8 million possibilities) for the random pixel and tests
the survivability of the new picture. If the new picture is more like
the "fitness" picture than what was there previously, the new picture,
with its single different pixel wins. If not, what was there before
wins. The program displays the winning picture, and also keeps a running
total of the number of generations that have happened. A generation is
every time a pixel changes and the fitness test is done.

![Early Screen Shot]({static}/images/by-chance1.jpg "ByChance Screen Shot (Early)")

_Early Screen Shot_

![Later Screen Shot]({static}/images/by-chance2.jpg "ByChance Screen Shot")

_Later Screen Shot_

I'm certainly not an expert in evolutionary theory, but it seems like
the program serves as an interesting analogy. I should point out that
evolution doesn't have a perfectly ideal goal that it is shooting for
like the fitness image. Given the forces of nature around us and all the
aspects of our environment, there is pressure toward a survivable form.

Some of the choices I made in writing the program were arbitrary:

-   Why not make the image size random too?
-   Why start with black? Why not start with white or a completely
    random starting image?

Maybe something a little different would be a better analogy of our best
understanding of what really happens. This experiment is kind of related
to the [infinite monkey
theorem](http://en.wikipedia.org/wiki/Infinite_monkey_theorem), but with
not so many permutations and with pressure toward correctness.

After running the program several times, I've noticed a couple of
things.

1.  The image becomes recognizable really fast.
2.  The image becomes perfect some time later than my patience allows
    for, but I expect it would take a really, *really* long time.

If you would like to run ByChance, you can [download it from
here](http://esmithy.net/software/bychance-an-experiment-with-randomness/).

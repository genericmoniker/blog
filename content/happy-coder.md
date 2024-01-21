Title: The Happy Coder
Date: 2024-01-20 17:44
Author: Eric
Category: Opinion
Slug: happy-coder
Status: published

![Happy Coder]({static}/images/happy-coder.png){: width=500}

<small>*Image credit: Stable Diffusion*</small>

While reading an interview with Guido van Rossum a while back, I encountered the
following quote by Clive Thompson:

> When you meet a coder, you're meeting someone whose core daily experience is of
> unending failure and grinding frustration.

I chuckled and thought, *Oh, man, sometimes that is spot on...*. I've found myself
pondering the quote since, though. Is that what I signed up for? Unending failure and
grinding frustration? Is that my career, past and future?

I wanted to better understand what that quote was about. It comes from Thompson's book,
*Coders: The Making of a New Tribe and the Remaking of the World*, pp.17-18 (disclaimer,
I haven't read the whole book). Here it is, in its broader context, saying that even a
supposedly trivial "Hello, World!" program isn't without its challenges:

> More than introversion or logic, though, coding selects for people who can handle
> endless frustration. Because while computers may do whatever you tell them, you need
> to give them inhumanly precise instructions. That "Hello, World!" line of code I
> showed you earlier? Let's imagine you were typing it in a rush, and typed it this way
> accidentally...

> `print (Hello, World!)`

> ... so, whoops, you left out the quotation marks. Try to run it, and boom—it crashes.
> The computer won't run it. And the computer isn't pleasant about it; there's no "I'm
> really sorry, Clive, something went wrong." There are no niceties. It just spits out
> an error message like `SyntaxError: invalid syntax`, and it's up to you to figure out
> what you did wrong. Programming languages are languages, a method of speaking to
> machines; but to speak to a computer is to speak to the most literal-minded entity on
> the planet, a ruthlessly prissy grammarian. When we speak to humans, they put a lot of
> work into helping interpret what we say. Computers don't. They will take every single
> last one of your smallest errors and grind them in your face, until you fix them. That
> works its way into your mind and personality, too. When you meet a coder, you're
> meeting someone whose core daily experience is of unending failure and grinding
> frustration.
>
> Because code is constantly broken, screwed up, an unholy mess, filled with bugs. Even
> the stuff you just wrote two minutes ago will probably crash the first time you try to
> run it. "When you learn to program a computer, you almost never get it right the first
> time," noted the pioneering computer scientist and educator Seymour Papert, back in
> 1980. He regarded this experience as the pivot around which all coder psychology
> turns. You write some code, you try to run it; it fails; so most of your job is
> figuring out what the hell you just did wrong. Those who can handle that daily
> vexation thrive. Those who can't, flee. In June 1949, the computer scientist Maurice
> Wilkes was about to ascend the stairs when he suddenly had the epiphany that "a good
> part of the remainder of my life was going to be spent in finding errors in my own
> programs." Seventy years later, all coders live with that moment. Even more fun—and,
> these days, more common—is the task of detangling errors not in your own work but
> rather in that of a programmer who was employed by your firm four years ago and who
> wrote what programmers call "spaghetti code," filled with haphazard formatting,
> baffling variable names, and a structure as Gordian as that of *Finnegans Wake*. And
> so you dive in, and slowly, slowly, fix it. Programmers are what I've come to think of
> as "near Sisypheans." They toil for days in resigned failure, watching the boulder
> roll back down the hill ... until one day it abruptly and unexpectedly tips over the
> crest. And what do they behold on the other side? Another hill.

That is incredibly depressing, and yet I can relate to a lot of it. I'll give you a
couple of examples from my experiences.

The other day, I was working with one of my teammates trying to understand why a build
was failing on the CI server but not locally in a development environment. He had been
working on it for a good while before seeking my thoughts, and we looked at it together
for a couple of hours before discovering an errant space causing a version number to be
invalid and eventually causing the build failure.

As another example, being someone who tends to stay at a company longer than the average
developer, I get to follow behind my ex-coworkers and inherit responsibility for their
hurriedly implemented hacks that just barely manage to work sometimes.

<p><iframe width="560" height="315" src="https://www.youtube.com/embed/utuchVE_56M?si=NwmCqj32gnVOXIP6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></p>

Thompson isn't alone in his opinion of software development. [A CEO of an AI company](https://thenewstack.io/coding-sucks-anyway-matt-welsh-on-the-end-of-programming/)
is glad to have AI take over programming because by his assessment, "Coding sucks
anyway! Let the robots do it. Go and have a good life."

If I expand out from coders to include people who write for other people, I've noticed
interestingly parallel sentiments. Take the [variously attributed
quote](https://quoteinvestigator.com/2011/09/14/writing-bleed/):

> It is easy to write. Just sit in front of your typewriter and bleed.

Likewise, in a [recent Wired
article](https://www.wired.com/story/ai-detection-chat-gpt-college-students/),
Christopher Beam said:

> After almost 20 years of typing words for money, I can say from experience, writing
> sucks. Ask any professional writer and they’ll tell you, it’s the worst, and it
> doesn’t get easier with practice.... I keep it up because, for better or worse, it’s
> now who I am. I do it not for pleasure but because it feels meaningful—to me at least.
>
> Some writers romanticize the struggle. [A writer] once described lying on a picnic
> table for two weeks, trying to decide how to start an article. “The piece would
> ultimately consist of some five thousand sentences, but for those two weeks I couldn’t
> write even one,” he wrote.

I think Beam is on to something there with romanticizing the struggle--of "bleeding" and
paralysis. Is that what Thompson is doing--romanticizing the struggle of writing
software? Yes, dear coder, you're not just someone who fixes stupid errors, you are a
near-mythical [being eternally punished by the
Gods](https://en.wikipedia.org/wiki/Sisyphus)!

I also like Beam's emphasis on meaningful work. It is certainly going to help your
outlook as a coder if you're doing something worthwhile for society, vs. say, figuring
out the best way to make other people trade off doing something meaningful for a
dopamine drip.

So should you buy into the pessimism in the first place? Is Clive Thompson even right
about coders' *core experience*? Yes, sometimes programming is frustrating, and if you
are more of the "big picture" person vs. a "details" person, it probably isn't for you.
But it can also be amazing to build things! Things that are useful, that expand human
capacity, or are just fun. If you're constantly saying, "This sucks!" then it certainly
will. Or as Jeffrey R. Holland said, "No misfortune is so bad that whining about it
won’t make it worse."

It turns out that being a Software Developer is one of [the best
jobs](https://money.usnews.com/careers/best-jobs/rankings/the-100-best-jobs) in terms of
satisfaction, opportunity as well as pay. It can admittedly also be stressful, but
in my experience that comes at least as much from working in a company full of imperfect
people (that is, normal humans) as from the technical aspects of coding.

Would you rather:

- *Literally* clean up other people's crap? (janitor, nurse, day-care)
- Work outside year-round? (construction)
- Be responsible for violent criminals? (corrections & police officers)
- Get paid really poorly for dangerous and physically strenuous labor? (logger)
- Work with customers who rarely seem happy or satisfied? (restaurant & retail workers)
- Regularly put your life on the line? (firefighter, soldier, police officer)
- Be unemployed (when you can't afford to be)?

Paul Graham [said](https://paulgraham.com/gh.html):

> I know a handful of super-hackers, so I sat down and thought about what they have in
> common. Their defining quality is probably that they really love to program. Ordinary
> programmers write code to pay the bills. Great hackers think of it as something they
> do for fun, and which they're delighted to find people will pay them for.

Since coders are often analytical personality types, let me respond to the question of
whether our attitude really matters. Does how I *feel* about coding make much difference
in my skill and effectiveness? Absolutely yes.

As Chad Fowler observed (in *The Passionate Programmer*, p.95), "When we have more fun,
we do better work. So, when we have no interest in a task, we're bored, and our work
suffers as a result."

But as impairing as disinterest can be, frustration, the alleged grinding variety of
which kicked off this exploration for me, is worse. I like how V. Anton Spraul said it,
when describing techniques for problem solving in *Think Like a Programmer*:

> The final technique isn’t so much a technique, but a maxim: Don’t get frustrated. When
> you are frustrated, you won’t think as clearly, you won’t work as efficiently, and
> everything will take longer and seem harder. Even worse, frustration tends to feed on
> itself, so that what begins as mild irritation ends as outright anger.
>
> ...
>
> When you allow yourself to get frustrated--and I use the word "allow"
> deliberately--you are, in effect, giving yourself an excuse to continue to fail.

It certainly isn't all rainbows and butterflies, but building software can be
challenging, fulfilling, satisfying, and even fun.

One of the things that drew me to coding was the joy of creation. See that thing on the
screen there? I made that! Isn't it cool?

Finding and fixing bugs, which for some is a grind, can be like solving a puzzle or a
mystery. You start thinking, "What the heck is even going on here? Why am I so dumb that
I can't figure this out?" After some digging and thinking and experimentation and more
thinking, there is an epiphany. "Oh! I know what's going on! I figured it out! I'm a
freaking genius!"

Even a code base that is an "unholy mess" can have small incremental improvements, tiny
victories that eventually add up to real change for the better.

Coding can be fun. Remember that and be happy, and you'll also be at your best.

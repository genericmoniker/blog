Title: Write Your Code for Humans
Date: 2012-11-06 16:30
Author: Eric
Category: Opinion
Slug: coding-standards-and-orthography
Status: published

Sometimes when I bring up the subject of coding standards, I get an
eye-rolling, aren't-we-all-adults-here kind of reaction from my fellow
programmers -- or a fearful look anticipating endless debates about
where the braces should go. Of course, "coding standards" can cover a
gamut of subjects -- from techniques to avoid shooting yourself in the
foot to parenthesis placement -- but even the little stuff matters,
because writing code is largely about communicating with humans.

<!--more-->

The adage says, "code is read more than it is written." If this isn't
completely obvious, try this experiment:

1.  Turn off your monitor
2.  Write some code

It's pretty hard to write code without at least reading it *once*, so if
you ever read it again you've satisfied the adage's assertion. Chances
are that you or someone else will read the code many more times.

Flippancy aside, a [survey of software maintenance cost
studies](http://users.jyu.fi/~koskinen/smcosts.htm) shows that greater
than 90% of the cost of software is in maintaining and enhancing it, and
"Studies of software maintainers have shown
that approximately **50%** of their time is spent in the process
of *understanding the code* that they are to maintain."

If you accept the premise that code is a form of written communication
with people as a primary audience, then it makes sense to draw from the
ideas of similar systems with hundreds of years of experience behind
them, like say, written English.

Orthography (literally "correct writing") are the rules of writing a
language, with special emphasis on standardized spelling. There was an
[argument](http://www.wired.com/magazine/2012/01/st_essay_autocorrect/)
and
[rebuttal](http://www.wired.com/magazine/2012/01/st_essay_autocorrect_rebuttal/)
a little while back in Wired Magazine for doing away with standardized
spelling, which was also covered on
[NPR](http://www.npr.org/2012/03/01/147741215/duz-prawper-speling-mader-nemor).

In the NPR interview, Anne Trubek says:

> So my basic argument is that if you look at the history of the English
> language, a lot of people think there are sort of immutable laws that
> are, you know, God-given or laws of nature. But actually, it's a bunch
> of manmade prescriptions and guidelines that change over time.

In other words, Trubek is saying that correctness is somewhat arbitrary,
but as something becomes standardized, people start to treat right and
wrong in an almost moral sense that isn't justifiable.

Lee Simmons, a copy editor for Wired, who has the job of making sure
words are spelled correctly, responds with:

> I would say spelling rules, for what they are, they're all about
> making communication easier. If I could use an analogy, the Internet
> itself is essentially a set of standards - hardware and software
> standards - that make it possible for people with different devices to
> communicate. It creates a universal platform. And I would argue that
> our English spelling system, for all its flaws, provides just such a
> universal platform.... We can argue about whether we ought to reform
> the standards, make the system more logical, but I would argue that
> the standards themselves are something that we need to preserve.

Simply put, it's easier to read words that are spelled how we expect.

English also developed standard punctuation and good style, again with
the objective of writing to be understood, but we sometimes forget
things like that when writing code. We laugh at "The Department of
Redundancy Department", but many programmers don't see anything wrong
with code like:

```csharp
// find the customer with the id
var customer = Customers.Find(customerId);
```

or

```csharp
return (a == b) ? true : false;
```

Does it matter where braces and parentheses go? Certainly not in any
moral sense, but there are standards that are more logical than others.
If you're reading an English sentence with parentheses (like this one)
and suddenly things get a little weird( like this )then it interrupts
the communication. Or what (if I) just start) throwing unnecessary(
parentheses in?

```csharp
return (theResult);
```

Communication is actually kind of hard. Consider the fact that
professional writers, who presumably have some talent for communication,
almost never publish the first thing that shows up in the word
processor. They revise, rework, rewrite until their ideas are expressed
well. Then *someone else* comes along to fix the places where the writer
still didn't get it quite right.

Do people even notice if you make a similar effort to make your code
easy to read? Or do they just say, "Oh, that's easy," compared to
looking at some complicated mess and say, "Wow, that guy's smart"?

Coding standards are a *tool*, one of many available to programmers to
facilitate communication. Why not take advantage of it? Your future self
will thank you.

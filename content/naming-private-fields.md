Title: Naming Private Fields
Date: 2007-01-10 17:00
Author: Eric
Category: Opinion
Slug: naming-private-fields
Status: published

One of the greatest questions facing theologists is this: What should be
the naming convention for private fields? The most controversial aspect
is the use of `m_` as a prefix.<!--more-->

For many programmers, this debate has been resolved for years. My
personal history with the issue is goes like this.

**Mid 1990's in C++**: It's the Microsoft/Windows way! Use `m_` and any
other combination of weird lower case letters at the beginning of
variable/member names. The ultimate corruption of Hungarian notation to
me was when I saw some of my coworkers throwing a lower case 'z' on the
front of variables. "What's with the `z`?" I'd ask. "Well, there's not
really a standard prefix for this type, but it looks funny with nothing,
so I put `z`."

**Turn of the Millennium in Java**: `m_` is blah! All things Microsoft
are blah! Besides, if you have a *real* IDE, it will highlight member
fields in a different color. Sheesh, what were we thinking?

**Today in C\#**: Visual Studio 2005 is not bad, but it still doesn't
highlight member fields. And it is kind of nice to be able to quickly
tell if a variable is a member -- even if I print out the code for
inspection. Do I dare use `m_` again?

Microsoft's Official Position
-----------------------------

Microsoft's general [naming
guidelines](http://msdn2.microsoft.com/en-us/library/ms229045.aspx) for
the .NET Framework on MSDN say "Do not use Hungarian notation." OK, so
is `m_`*really* Hungarian, since Hungarian notation is more about type?
The guidelines also say "Do not use underscores, hyphens, or any other
nonalphanumeric characters."

The more specific [naming guidelines for
members](http://msdn2.microsoft.com/en-us/library/ms229012.aspx) also
says this about fields: "Do not use a prefix for field names. For
example, do not use g\_ or s\_ to distinguish static versus non-static
fields."

Still, you could argue that there is some wiggle room for *private*
fields, because the naming guidelines for members are said to apply
specifically to static public and protected fields. After all, private
fields are invisible to the users of the class, so why should the naming
be dictated. Further, these are the guidelines for the .NET Framework,
which must support all CLR languages. If I only write C\#, things don't
need to be so restrictive.

There are also some [internal Microsoft
guidelines](http://blogs.msdn.com/brada/articles/361363.aspx) that are
less binding than the official framework guidelines, but even more
explicit: "Do not use a prefix for member variables (\_, m\_, s\_,
etc.). If you want to distinguish between local and member variables you
should use 'this.' in C\# and 'Me.' in VB.NET."

Are they saying always use 'this.' for private member references, or
only when there is ambiguity?

Other Positions
---------------

In spite of Microsoft's fairly clear recommendations, believe it or not,
some people have other opinions.

The folks at [IDesign](http://www.idesign.net), a consulting and
training company, have a set of [coding
standards](http://www.idesign.net/idesign/download/IDesign%20CSharp%20Coding%20Standard.zip)
for C\#. They go against the apparent Microsoft recommendations and
advocate using `m_` for private member fields. They also add a twist.
I've always thought that it went without saying that the name following
an `m_` would be in camel case, like `m_wormCount`. Instead, they say to
use Pascal case: `m_WormCount`.

Pete Brown also has some [thoughts on field
naming](http://www.irritatedvowel.com/Programming/Standards.aspx),
acknowledging both Microsoft's recommendation and alleged disregard of
their own conventions. He also points out the challenge with VB not
being able to use property names and fields that differ only by case,
making you wonder what to call them. Pete finds `m_` ugly and so has
compromised with just a single leading underscore: `_wormCount`.

An example of disregard for their own conventions are code samples by
Stephen Taub, the Technical Editor for *MSDN Magazine*. [This piece of
code](http://msdn.microsoft.com/msdnmag/issues/06/12/NETMatters/default.aspx?loc=&fig=true#fig2),
for example, shows a preference for the leading underscore as well.

There's also Eric Gunnerson, [who likes either `m_` or
`_`](http://blogs.msdn.com/ericgu/archive/2005/03/09/390791.aspx) to
distinguish members from locals, and lots of comments from people
arguing for the various conventions.

Here's a summary of some of the comments from there and elsewhere:

-   If you have really short methods, there isn't much confusion.
-   Doing `_` or `m_` gives you a nice Intellisense experience,
    especially in classes derived from large bases like Form.
-   Two underscores on names is reserved for the compiler, and one
    underscore feels "compiler-ish" too.
-   ReSharper (and others) gives VS 2005 syntax highlighting
    for members.
-   Underscores at all require the shift key.
-   Delphi rocks! Prefix with f!

Conclusion
----------

Using *something* to disambiguate members from locals and parameters
seems like it can prevent some errors, like the ones below.

```csharp
// Example #1
public WormFarm(uint wormCuont)
{
    // Notice misspelled parameter makes this line a no-op:
    this.wormCount = wormCount;
} 

// Example #2
public void RecalculatePopulation(FishEngine fishEngine, float birthRate, float nominalDeathRate)
{
    // some code...    

    // Oops -- hides member:
    uint wormCount;
    fishEngine.FactorPopulation(out wormCount);    

    // more code...    

    // Oops, meant to set member, not local:
    wormCount = finalPopulation;
}
```

Given that I sometimes print code for a code inspection (and I try to
avoid printing reams of source code with the color printer), the
*something* ought to be textual as opposed to simply an IDE highlighting
difference.

Using `this.` everywhere seems kind of cumbersome, doesn't save you from
the first error above, and you'd have to rely on static analysis (as
opposed to the compiler, for example) to automatically enforce this
convention.

I guess that leaves some kind of prefix (or suffix?), which maybe
ultimately comes down to personal taste or religious affiliation.

[[follow-up posting]({filename}/naming-private-fields-addendum.md)]

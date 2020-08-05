Title: Design by Contract: Is It Worth It Without Language Support?
Date: 2006-01-29 17:00
Author: Eric
Category: Review
Tags: Design
Slug: design-by-contract-part-2
Status: published

This is a continuation of thoughts after reading *Design by Contract by
Example* by Richard Mitchell and Jim McKim. This time I want to write a
little about design by contract without direct language support. What do
you give up without language support, and is it still worth it to
struggle through defining contracts without that support?<!--more-->

[Design by Contract Part 1]({filename}/design-by-contract.md)

Benefits of Language Support
----------------------------

These are some of the benefits of having language support for design by
contract:

-   Automatic invariant checking upon exiting methods, without any extra
    effort like calling a helper routine or creating some kind of
    automatic object that checks invariants when it goes out of scope.
-   An "old" keyword that provides easy syntax for referencing the state
    of variables as they were before the current method began executing.
-   Contracts are automatically cumulative down an inheritance tree. In
    other words, if the base class has a contract, any subclasses
    automatically have that contract.
-   Related to the point above, language support can also help ensure
    that contracts on overridden methods follow the rules of contract
    inheritance: preconditions can only be the same or weaker, and
    postconditions can only be the same or stronger.
-   Contracts can be part of declarations. For example, if you are
    trying to simulate DBC in C++, you can't put the contracts in the
    header file except as comments.
-   Contracts will probably be understood by a debugger, which might be
    more convenient than debugging something like the output of a
    preprocessor in the absence of language support.

Languages Supporting Design By Contract
---------------------------------------

Obviously [Eiffel](http://www.eiffel.com/) supports design by contract.
I haven't personally used Eiffel for a programming project. There is,
though, a version of Eiffel that compiles to MSIL, so if you're a .NET
shop, maybe it's a real possibility.

Another language with contract support is the [D Programming
Language](http://www.digitalmars.com/d/). D is kind of a cool language
in its own right. It has a lot of the conveniences of "modern" languages
like Java and C\#, but it compiles to native binary code instead of an
intermediate code requiring a big run-time environment to execute. It is
still a bit immature, and lacks much industry support, but I kind of
wish it would catch on. The creator of the language, Walter Bright, has
written an [excellent essay about the design by contract
support](http://www.digitalmars.com/d/cppdbc.html), comparing it to how
one would attempt similar functionality in C++.

Preprocessors and Libraries
---------------------------

In the book, Mitchell and McKim give examples in Java using a free
preprocessor called iContract. It lets you do DBC by writing special
Javadoc comments which the preprocessor then converts to Java code. I'm
not sure what the current status of iContract is, though, since the
book's reference to iContract's source,
<http://www.reliable-system.com>, has a big for sale sign on it. Links
to the book's own web site are also broken, though if you're persistent
you can find the publisher's site for the book that has even more broken
links on it. There's an [iContract Ant
task](http://ant.apache.org/manual/OptionalTasks/icontract.html), but
I'm not sure how to get a hold of the preprocessor itself such that the
task will work. The Ant documentation points to the same broken links as
elsewhere.

For C++, the best DBC library I've come across was [posted on The Code
Project by <font class="messagetitle">Jarl
Lindrud</font>](http://www.codeproject.com/cpp/DesignByContract.asp).
I haven't had a chance to use it, but it looks promising. It makes heavy
use of the magical Boost bind and lambda modules to pretty good
effect.

Adding Language Support
-----------------------

There is research going on to add DBC facilities to existing languages.
There is a
[proposal](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2005/n1866.html)
to extend standard C++ to provide contract support. It adds
preconditions and postconditions to methods and invariants to classes
and namespaces. Here is an example from the proposal:

```cpp
int factorial( int n )
precondition
{
    0 <= n && n <= 12;
}
postcondition( result )
{
    result >= 1;
}
{
    if ( n < 2 )
        return 1;
    else
        return n * factorial( n - 1 );
}
```

The proposal also includes an `oldof` keyword to support writing
postconditions.

In addition to C++, there is also work being done to potentially add
contract support to C\#.
[Spec\#](http://research.microsoft.com/projects/specsharp/) is the name
of the extended language. The researchers claim that contracts in Spec\#
will be more robust than those in Eiffel, handling some situations that
that language didn't do so well. One really cool aspect of Spec\# is its
integration with Visual Studio. It does static contract checking on the
fly. If you type code that violates a contract, you get the red
squiggle. You can download the current implementation from the [project
page](http://research.microsoft.com/projects/specsharp/) and take it for
a spin. In my brief experience, there were some more complicated
constructs than are found in Eiffel (such as a concept known as
"exposure"), and the documentation was virtually non-existent, but I
still remain excited about the potential.

Syntactically Spec\# has some nice features. One of the most common
preconditions is that some argument is not null. Spec\# expresses this
with a single character, an exclamation point:

```csharp
public static void Clear(int[]! xs)
{
  for (int i = 0; i < xs.Length; i++)
  {
    xs[i] = 0;
  }
}
```

In this example, you can safely dereference `xs` without checking for
null because the exclamation point in the method signature guarantees
that it is non-null.

Spec\# also uses keywords `requires` and `ensures`, which feel more
natural to me than `precondition` and `postcondition`, or even Eiffel's
imperative `require` and `ensure`. Here's the C++ example from above
translated to Spec\# (possibly even correctly?):

```csharp
public static int factorial( int n )
  requires 0 <= n && n <= 12;
  ensures result >= 1;
{
    if ( n < 2 )
        return 1;
    else
        return n * factorial( n - 1 );
}
```

There was an MSDN webcast last year on Spec\# that I sat in on that gave
a good overview of where the project is going, as well as how it is
addressing problems beyond what Eiffel does. It is now [archived for
on-demand
viewing](http://msevents.microsoft.com/CUI/WebCastEventDetails.aspx?EventID=1032273351&EventCategory=5&culture=en-US&CountryCode=US).

Conclusion
----------

If you don't have language support, or some kind of library or
preprocessor, you could at the very least assert preconditions. That's
the advice of Mitchell and McKim (see p.205). Much of the benefit of
contracts comes from simply *thinking* about them. Sometimes I've
thought that the behavior of a function I'm writing is obvious until I
stop to consider what the function requires and what it ensures. It adds
a level of precision to your work to do that extra thinking.

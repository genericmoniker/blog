Title: The Best of PDC 2008
Date: 2009-01-17 21:45
Author: Eric
Category: Software Development
Tags: .NET
Slug: the-best-of-pdc-2008
Status: published

For those of us poor folk who didn't make it to PDC this past fall,
Microsoft has been taking the show to us in the form of its MSDN
Unleashed series. [Rob Bagby](http://blogs.msdn.com/bags/), developer
evangelist, came to Salt Lake City to present and give updates about new
and upcoming technologies for developers.

![Microsoft\'s Salt Lake City Office]({filename}/images/microsoft-slc.jpg "Microsoft\'s Salt Lake City Office")

<!--more-->

**The Future of C\# (AKA C\# 4)**

Rob's first presentation introduced what the C\# team is working on for
the next release of the language. A lot of the focus is around exposing
support for dynamic programming and interoperability with dynamic
languages like Python and Ruby. This is done by deferring the evaluation
of method and property calls on some objects until runtime. At compile
time, the normally strict static type checking of the C\# compiler is
relaxed when a method call doesn't seem to exist in order to allow for
the possibility that such a method will be added dynamically sometime
during program execution. To indicate that this behavior is wanted, you
use the **dynamic** keyword like this:

```csharp
dynamic customer = GetCustomer();
Console.WriteLine(customer.FirstName);
```

At run time, whatever actual object is stored in "customer" needs to
have a property "FirstName" or an exception is thrown. Otherwise, the
actual type is unimportant. This is also known as "duck typing" where
capabilities of objects are more important than actual types -- if it
looks like a duck and acts like a duck, it might as well be a duck.

Some people in attendance were confused about how the **dynamic**
keyword differs from **var**. The **var** keyword really just saves
keystrokes -- the type is still static but figured out by the compiler.
Objects that are **dynamic** however, have their method calls bound at
run time.

The ability of C\# to handle dynamic types also makes it easier to
interoperate with Javascript. Rob showed a Silverlight application that
called out to Javascript functions pretty much identically to calling
regular C\# methods.

The next version of C\# will also have default and named parameters,
which have been supported in other .NET languages, and will make COM
interop a bit nicer. I've written a bunch of calls to Office where it
seems like you're passing in ten-thousand Type.Missing parameters to
some of the methods, and that will no longer be required.

**Silverlight Toolkit**

Shawn Burke, one of the guys behind the AJAX Control Toolkit, is now
[heading a team to create Silverlight
controls](http://blogs.msdn.com/sburke/archive/2008/09/17/control-freak.aspx).
This presentation showed the controls that they are working on, and
described the distribution model.

The controls are things like AutoComplete, NumericUpDown, TreeView,
DockPanel, WrapPanel, and others that would be really useful in building
a typical modern GUI application. There is also charting support, which
Rob said comes fairly mature by virtue of Microsoft's assimilation of
Dundas code and engineers. There is also support for theming
applications.

The controls are to be released on CodePlex frequently, with some
controls eventually making it into the official Silverlight SDK or even
the Silverlight Core. The [Silverlight
Toolkit](http://www.codeplex.com/Silverlight), not to be confused with a
CodePlex project called the [Silverlight Control
Toolkit](http://www.codeplex.com/SilverlightToolkit), has a nice sample
application that shows off all the new components.

**REST with WCF**

My coworker, [Ryan Jameson](http://www.zombiecuisine.com/), went to a
Microsoft event last year where the [REST Starter Kit for
WCF](http://msdn.microsoft.com/en-us/netframework/cc950529.aspx) was one
of the topics. He came back saying with a smirk that Microsoft had
apparently *invented* REST, the way they had presented it. Rob implied
no such thing, even joking that in every presentation about REST, there
are people ranging from those who have never heard of it, to those that
know [Roy Fielding's](http://en.wikipedia.org/wiki/Roy_Fielding) middle
initial (which would be T, by the way).

REST is a philosophy for providing web services in a way that embraces
the "way of the web", such as:

-   Most everything is addressable through a URI
-   There are standard representation formats
-   Interactions are stateless
-   The HTTP protocol

Rob asked rhetorically if these principles might work OK given the
success of the web, and summed up the philosophy by saying, "If you use
GET for something other than *getting* a resource, you're Part of the
Problem." And don't even think about using POST to *get* something.

I haven't done more than play around with web services, but it seemed to
me that by using URI templates, WebGet and WebInvoke attributes, and
WebProtocolException, you could suffuse a high degree of RESTiness into
your WCF web service.

Things got pretty loose in this presentation, with Rob dodging pot shots
about IE and standards conformance, switching to a Mexican accent for a
bit of the delivery, and demonstrating that Notepad is a REST client.
Kind of fun.

**Azure**

The last presentation was a lot to grasp, as Rob warned it would be. The
denotation of "azure" is the blue of a clear or unclouded sky. But
Microsoft's Azure is about cloud computing. What does that mean?

Azure comprises a huge pile of stuff, which makes it pretty hard to talk
about in a meaningful way. Hearing the presentation reminded me of when
.NET was first announced. Everything at Microsoft was .NET then: Visual
Studio .NET, Windows .NET, Clippy .NET, etc. The short version is that
Azure combines typical operating system facilities with utility
computing. In one sense it sounds like outsourced IT, where you let
Microsoft worry about the data center, dynamically scaling resources as
needed. But it is also more than that -- an umbrella of networked stuff
covering the "Live" services, SQL, raw data storage, and much more.

Rob says that Azure is Microsoft's big bet right now. I wonder if things
will settle down a bit when Microsoft gets a more fully-formed vision,
much like they did with .NET.

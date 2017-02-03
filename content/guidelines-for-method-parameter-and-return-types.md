Title: Guidelines for Method Parameter and Return Types
Date: 2008-04-22 22:25
Author: Eric
Category: How-To
Slug: guidelines-for-method-parameter-and-return-types
Status: published

I've been reading Jeffrey Richter's [*CLR via
C\#*](http://www.amazon.com/gp/redirect.html?ie=UTF8&location=http%3A%2F%2Fwww.amazon.com%2FCLR-via-Second-Pro-Developer%2Fdp%2F0735621632%3Fie%3DUTF8%26s%3Dbooks%26qid%3D1208924595%26sr%3D8-1&tag=sparksfromthesmi&linkCode=ur2&camp=1789&creative=9325)
lately, and just read a section titled "Declaring a Method's Parameter
Types". That title doesn't exactly promise a riveting read, but it did a
nice job of articulating some guidelines for method parameter and return
types, independent of any particular programming language.

The guidelines are these:

1.  A method's parameters should be the most general type possible.
2.  A method's return value should be the most specific type possible.

As an example of the first guideline, a method should accept
`IEnumerable` rather than `IList` if `IEnumerable` is all that is
needed. The user of a method can always pass in something more specific,
but being general allows the greatest flexibility. Of course, the most
general parameter type would be `object`, but I don't think you have
to worry about this guideline suddenly causing you to write methods like
this:

```csharp
FileStream CreateFile(object fileName, object fileMode, object fileAccess);
```

Clearly you wouldn't want the method implementation down-casting all the
parameters in order to do something useful with them. If the method can
actually do something useful with  plain `object` parameters, then
that is probably the right type.

Conversely, following the second guideline suggest that you should
return a `FileStream` rather than a `Stream` (assuming that what you
actually have is a `FileStream`). The caller can always treat it as
something more general, but never something more specific. In this case,
the most specific type provides the most flexibility.

The author did provide a caveat to the second guideline, however. If you
want to allow the implementation of a method to change, you might pick a
return type that is slightly more general. The example he gives is that
even if a method happens to use a `List` internally, it may be
appropriate to return an `IList` so that the internal implementation
could change to use an array without affecting the callers.

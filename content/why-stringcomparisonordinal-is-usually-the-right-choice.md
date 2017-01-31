Title: Why StringComparison.Ordinal Is Usually the Right Choice
Date: 2007-10-15 14:54
Author: Eric
Category: Programming
Tags: .NET, Windows
Slug: why-stringcomparisonordinal-is-usually-the-right-choice
Status: published

A question that arose in response to my [previous
post](http://esmithy.net/2007/10/11/unicode-surprises/) (about how
string comparisons can produce unexpected results when done in a
culture-sensitive way) was *Which is right, StringComparison.Ordinal or
StringComparison.InvariantCulture?* The short answer:
StringComparison.Ordinal.

<!--more-->

There is a [good
article](http://msdn2.microsoft.com/en-us/library/ms973919.aspx) explaining
the differences between the StringComparison enum values on MSDN. I'll
summarize here, but without mentioning the "IgnoreCase" variations in
the enum since those are generally understood (though there are
subtleties with case conversion).

StringComparison.Ordinal is the best choice in most cases. When
specified in comparison operations, these cause a character by character
comparison based strictly on the numeric value of the characters. This
has a couple of advantages:

1.  It is very fast.
2.  It is usually what you want.

The performance benefits include not needing to do any table lookups as
well as the ability to fail fast if the two string lengths are not
equal.

It generally only makes sense to use StringComparison.CurrentCulture if
you are going to display the result of the operation to the user, such
as in a list where the items are supposed to be sorted alphabetically
according to the user's culture. Instead of a character by character
comparison, it is a "linguistic" comparison.

This leaves StringComparison.InvariantCulture. The author of the MSDN
article was hard pressed to come up with a good reason for using
StringComparison.InvariantCulture from .NET 2.0 forward. It does a
linguistic comparison, but in a way that is always the same regardless
of the current culture. In other words, it isn't a character by
character comparison, but it isn't necessarily correct for the current
culture either.

An example clarifies things:

```csharp
static void Main(string[] args)
{
  Console.WriteLine("Grüße".EndsWith("sse", StringComparison.Ordinal));
  Console.WriteLine("Grüße".EndsWith("sse", StringComparison.CurrentCulture));
  Console.WriteLine("Grüße".EndsWith("sse", StringComparison.InvariantCulture));
  Console.WriteLine("Grüße".EndsWith("sse"));
}
```

This example uses the German ess-szet or sharp s character. In German, ß
and ss are linguistically equivalent, so the results of running the
program, even using the English (United States) culture, are:

    False
    True
    True
    True

If a user searched a document for "Grüsse", it would be appropriate to
show matches for both "Grüsse" and "Grüße", and so use CurrentCulture.
But for most other day-to-day string manipulations within code, such as
comparing file names for equivalence, you should use one of the Ordinal
values.

![Both filenames are valid]({filename}/images/greetings.jpg)

Both are valid (and distinct) file names, after all, which is not
discernible using either CurrentCulture or InvariantCulture.

Title: Unicode Surprises
Date: 2007-10-11 21:15
Author: Eric
Category: Programming
Tags: .NET, Bafflers, Windows
Slug: unicode-surprises
Status: published

I got a defect from QA today saying that our product was unable to
track files in paths containing Unicode characters. I'll admit that I
was skeptical. I had just tried that myself the other day and it worked
perfectly. Trying it again today also worked perfectly, but the QA
engineer showed me otherwise.

<!--more-->

The path with the problem was something like this: `\\qa\tests\۩۩۩۩۩`

The unusual character there is the Arabic symbol "Place of Sajdah"
(U+06E9). For some reason, this path didn't work correctly.

Ultimately, I tracked the problem down to a bit of code that was trying
to test whether the path ended with a separator character, and if not,
add one. It looked like this.

```csharp
if (!path.EndsWith(Path.DirectorySeparatorChar.ToString()))
{
    path += Path.DirectorySeparatorChar;
}
```

This code wasn't working as expected, so when the path was combined
(using string concatenation) with a file name, the path separator was
missing, which lead to the final symptom described by the defect. There
are a couple of problems with this code.

1.  `System.IO.Path.Combine` is the right way to merge paths where
    possible -- you shouldn't have to worry about whether there is a
    trailing slash or not
2.  The simplest form of `EndsWith` (and `StartsWith`) doesn't work as
    expected with roughly 20% of Unicode characters

[Michael Kaplan
explains](http://blogs.msdn.com/michkap/archive/2005/01/18/355210.aspx)
that this is because many Unicode characters don't have entries in the
Windows sorting weight tables, and are therefore effectively invisible
for some comparisons.

Surprisingly, `@"\\qa\tests\۩۩۩۩۩".EndsWith(@"\")` evaluates to `true`.
All of the Place of Sajdah characters are "invisible" in terms of
weight, and once you realize that, then *obviously* the string ends with
a backslash. Also surprising is that all strings start with "۩". That
is, `"Cheese".StartsWith("۩")` evaluates to `true`. The `string.Equals`
method and operator don't have this problem, though, because they
compare lengths before ever getting to the part where the Place of
Sajdah characters would be thrown out of "۩۩۩Monkey۩۩۩" and thus become
equal to "Monkey".

The way to fix the problem is to use either `StringComparison.Ordinal`
or `StringComparison.OrdinalIgnoreCase` in the call to `StartsWith` or
`EndsWith`. So the code snippet from above would work as expected when
modified as follows:

```csharp
if (!path.EndsWith(Path.DirectorySeparatorChar.ToString(), StringComparison.OrdinalIgnoreCase))
{
    path += Path.DirectorySeparatorChar;
}
```

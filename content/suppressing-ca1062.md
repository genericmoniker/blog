Title: Suppressing CA1062 with a Helper Function
Date: 2011-03-15 22:32
Author: Eric
Category: Programming
Tags: .NET, Visual Studio Tips
Slug: suppressing-ca1062
Status: published

I think Visual Studio's static analysis warning for checking parameters
for null before they are used is generally a good idea, but the code to
check the parameters can get really tedious.

<!--more-->

Before addressing the tedium, though, why does it even matter whether
you check for null arguments and throw a ArgumentNullException? You'll
just get a NullReferenceException if you don't anyway. Is the
ArgumentNullException somehow better?

The ArgumentNullException has a couple of benefits: It clearly indicates
that the caller is to blame and by including the parameter name quickly
narrows down the problem instead of requiring you to figure out which
reference within the body of the method is null.

Although an `ArgumentNullException` is preferable, the null checking can
overwhelm a short method. Here's a contrived example:

```csharp
public static void PrintThings(string[] things)
{
  if (things == null)
  {
    throw new ArgumentNullException("things");
  }

  foreach (var thing in things)
  {
    Console.WriteLine(thing);
  }
}
```

Half the method is dedicated to checking the parameter for null. Now
imagine if a relatively short method had three parameters to check. It
would be all null checks and hardly any code.

In the spirit of conciseness, I've frequently had some kind of helper
function that does the null check:

```csharp
public static void PrintThings(string[] things)
{
  Arg.NotNull("things", things);

  foreach (var thing in things)
  {
    Console.WriteLine(thing);
  }
}
```

The trouble is, Visual Studio's static analysis doesn't recognize this
as a parameter validation of "things", so you'll get the CA1062 warning.

The work-around is to create a `ValidatedNotNullAttribute` and include it
in the helper method, which signals to static analysis that, trust me, I
really am checking the parameter. Here's a complete example:

```csharp
using System;

namespace CA1062Test
{
    public static class Program
    {
        static void Main()
        {
            PrintThings(new string[] { "one", "two" });
        }

        public static void PrintThings(string[] things)
        {
            Arg.NotNull("things", things);

            foreach (var thing in things)
            {
                Console.WriteLine(thing);
            }
        }

    }

    static class Arg
    {
        public static void NotNull(string name, [ValidatedNotNull] object value)
        {
            if (value == null)
            {
                throw new ArgumentNullException(name);
            }
        }
    }

    sealed class ValidatedNotNullAttribute : Attribute
    {
    }
}
```

Notice the trivial `ValidatedNotNullAttribute` implementation -- it
doesn't matter what it does so long as it is named
"ValidatedNotNullAttribute". The attribute is applied to the parameter
being checked in the NotNull function, so it only has to be specified
once in the helper declaration, and **not** on each use of the helper.

Title: Why Exceptions Are Better Than Returned Error Codes
Date: 2003-06-12 17:00
Author: Eric
Category: Opinion
Slug: exceptions-vs-returned-error-codes
Status: published

I'm occasionally surprised that some programmers prefer an error
handling system of returned error codes over exceptions. After spending
several years with both approaches, I've become convinced that
exceptions are a superior model. If you agree, great! If not, read on
and let me try to persuade you. I'm always up for a discussion on the
subject, too.<!--more-->

Reasons Why Exceptions Are Better
---------------------------------

**1. It's a good way to handle construction errors.** Since constructors
don't return a value that can be used as an error code, you have to
figure out another way to report errors. It's possible to return
something as an "out" parameter of a constructor, but that eliminates
the ability to use the default (no argument) constructor. If you want to
use return codes, you end up having to create separate initialization
functions (be suspicious of a method called "Construct") that *can*
return errors. This strategy makes constructors pointless except for
trivial initialization, and the desirable post condition of having a
ready-to-use object after construction is frequently impossible.

**2. You can return useful things from methods.** If the return value is
always reserved for an error code, then you have to resort to output
parameters to return anything, which leads to more complicated code.
Consider these differences:

Returning values

```cpp
RealignUniverse(errorTracker.GetRequiredAdjustment());
```

Output Parameters

```cpp
long requiredAdjustment; 
if (SUCCEEDED(errorTracker.GetRequiredAdjustment(&requiredAdjustment))) 
{ 
    RealignUniverse(requiredAdjustment); 
}
```

**3. You can isolate error handling code from the main program flow.**
In the examples above, error handling is ignored. You might think that
the second case does error handling, but it doesn't. It only does
success handling. When you do error handling with return codes, you
start to get code like this:

```cpp
if (SUCCEEDED(Operation1())) 
{ 
    if (SUCCEEDED(Operation2())) 
    { 
        if (FAILED(Operation3())) 
        { 
             Log.ReportError("Failed doing 3"); 
        } 
    } 
    else 
    { 
        Log.ReportError("Failed doing 2"); 
    } 
} 
else 
{ 
    Log.ReportError("Failed doing 1"); 
}
```

If you happen to have some resources that need to be cleaned up, this
gets worse. I know there are other ways writing the code, like the
infamous RETURNIFFAILED macro, but even with that strategy error
handling obscures the program flow compared to the exception approach:

```cpp
try 
{ 
    Operation1(); 
    Operation2(); 
    Operation3(); 
} 
catch (OperationException ex) 
{ 
    Log.ReportError(ex); 
}
```

**4. Forgetting to check an exception is easy to find.** Forgetting to
check a return code is easy to do and hard to find. If you don't catch
an exception, the program comes screeching to an obvious halt (so long
as you don't have places in the code that catch everything and do
nothing, which is very bad). If you don't notice an error return code,
your program continues on its merry way in some probably bad state.

**5. The C++, Java and C\# designers all think exceptions are
superior.** OK, this is a blatant appeal to authority, but they are
pretty good authorities.

Of course, exceptions, like virtually any programming construct, are
susceptible to abuse. They should still only be used for error
conditions (from someone's perspective) as opposed to normal program
flow. *Expected* error conditions can frequently be handled by
reasonable return values, such as returning `null` when an item isn't
found in a list.

Title: Are .NET Properties a Mistake?
Date: 2008-04-24 21:28
Author: Eric
Category: Opinion
Tags: .NET
Slug: are-net-properties-a-mistake
Status: published

As I mentioned the other day, I'm reading Jeffrey Richter's book *CLR
via C\#* right now. I was kind of surprised to read this statement by
the author: "If I had been involved in the design of the .NET Framework
and compilers, I would not have offered properties at all..." (p.
218)<!--more-->

Mr. Richter's reason for disliking properties is that they look like
fields but don't behave like them, thus confusing developers. He gives a
good list of ways in which properties are different from fields -- think
of all the ways that a zero argument method is different from a field
and you'll about have it -- saying that those differences are bound to
trip people up.

I disagree for a couple of reasons:

1.  Properties are really pretty easy to grasp.
2.  Most programmers adhere to the rule that all fields are private
    (which Mr. Richter also recommended), so there aren't really fields
    to be confused by. Expect everything to be a method and you'll
    generally be fine.

I say "generally" because there are some cases where the opposite is
true: a property can behave more like a field than a method. For
example, you can use the [postfix increment operator](http://msdn.microsoft.com/en-us/library/aa691363(VS.71).aspx)
on a property (that has both get and set accessors) and it behaves as it
would on a field. That is, the operator gets the property value and sets
the incremented value back in. \[Added June 26, 2008\]

A benefit of properties that isn't really mentioned in the book is a
more explicit (for lack of a better word) "bean-ness". Java has the bean
concept, where an object has get and set methods to create a set of
properties, but the C\# syntax is more elegant and apparent. With the
explicit properties, you can do things like XML serialization, property
editors, etc. with reasonable default behavior.

It's probably true that .NET properties get abused and overused (see the
[official guidelines](http://msdn2.microsoft.com/en-us/library/ms229006.aspx)),
but I still kind of like them.

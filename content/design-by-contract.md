Title: Design by Contract: An Alternative to Testing for Code Quality
Date: 2005-09-27 17:00
Author: Eric
Category: Review
Tags: Design
Slug: design-by-contract
Status: published

I recently finished reading *Design by Contract by Example* by Richard
Mitchell and Jim McKim. The book, as its title suggests, gives advice
about writing good contracts through a set of principles applied in
various examples. In addition to wanting to learn more about design by
contract generally, I came to this book with a couple questions: Can you
do design by contract effectively without built-in language support, and
what is the relationship between design by contract and unit testing? In
this article I'll talk about design by contract generally, and discuss
those two questions in follow-on articles.<!--more-->

Definition
----------

Design by contract (DBC) is a methodology for specifying precisely how
an object is supposed to behave. The contract relationship is between an
object and the user (or client) of the object (probably some other
object), and each party has its obligations as part of the agreement.
Like a typical contract in the legal sense, one party says to the other,
"Given that you do *x*, I agree to do *y*."

Contracts in DBC are specified as assertions. Some assertions, called
preconditions, assert that the user of the object (or client) is
fulfilling its part of the agreement. Others, called postconditions and
invariants, assert that the object is fulfilling its part of the
contract. The assertions are executable parts of the program, so running
the program ensures that the contract is being fulfilled by both
parties, and that the program is therefore correct. Any violation of the
contract produces an easy-to-notice error at runtime.

Preconditions and postconditions apply to methods, while invariants
apply to whole objects. A precondition is a prerequisite for calling a
method, and a postcondition is what is guaranteed to be true when the
method finishes. An invariant is something that, from the client's
perspective, is always true about an object.

The Book
--------

Mitchell and McKim give advice how to effectively write contracts
through a set of principles and guidelines. For example, their first
guideline is to divide object methods into two categories: queries and
commands. Queries return some value, but don't effect the visible state
of the object (like a `const` method in C++). Commands, on the other
hand, don't return a value but may change the object's state. In other
words, queries don't have side effects but commands do. This division
makes sense because when writing assertions, you call the queries, and
it would be bad if checking contracts changed the state of the object.
The authors further distinguish basic queries and derived queries.
Derived queries are expressible in terms of one or more basic queries,
and might exist for convenience or performance reasons (more on that in
a bit).

Most of the eponymous examples in the book are written in
[Eiffel](http://www.eiffel.com), the programming language developed by
Bertrand Meyer, the originator of design by contract (and author of this
book's Foreword). Even if you don't know Eiffel, though, the examples
are pretty easy to follow. There is a chapter that uses Java, which I
would recommend reading out of order if that language is more
comfortable to you, because comparing the Java and Eiffel examples
clarify some things about Eiffel that the authors don't explicitly
mention.

Here's an example of a contract for a generic "add to a list" method
using Eiffel syntax:

```eiffel
add(new_item : ITEM)
  -- Adds an item to the list
  require
    item_not_already_added:
      not has_item(new_item)

  ensure
    item_count_increased:
      count = old count + 1
    item_added:
       has_item(new_item)
```

An assertion uses the **require** (precondition) or **ensure**
(postcondition) keywords (or **invariant**, which isn't shown here).
Then there is a label that can be used to state the assertion in logical
terms. The label is displayed as part of the error message if an
assertion fails. After the label is a boolean expression that should
evaluate to true if all is working as expected. There are two queries
that are also part of the class, `has_item` and `count`, which are used
to write the contracts. Take special note of the **old** keyword. This
lets you refer to the value of something as it was before the method
started executing so that you can write postconditions in terms of how
they change the state from what it was originally.

When this method is called at runtime, the precondition is first
evaluated to verify that the caller is living up to its part of the
contract. Assuming that passes, the body of the method is executed.
Then, the postconditions are evaluated. If there were an invariant
assertion for the class (like that count can't be negative), that would
also be evaluated. An invariant is shorthand for saying that all the
methods in the class have a particular postcondition. The postconditions
and invariants verify that the object is fulfilling its part of the
contract.

The book gives examples of contracts for some common data structures,
like a queue and a dictionary among others. The authors also explain how
they arrived at the contracts by applying their guidelines and
principles. While reading, I sometimes thought, *Well sure, everybody
knows how a queue is supposed to work so that contract is easy*. I
wanted something a little more challenging. But I guess their point is
more about expressing good contracts rather than figuring out what they
should be.

An interesting concept explained in the book is that of "frame rules".
Frame rules are simply the things that *don't* change as the result of a
command. When writing software, I tend to think about what the code
*does*, but it can also be worthwhile to consider what it doesn't do.
For example, in the `add` method above, it would be undesirable if the
items previously in the list were changed as a result of calling `add`.
Frame rules would be postconditions that say that any existing list
items are still in the list and in the same order as before `add` was
called. Obviously you have to weigh the cost of extensively checking
frame rules, both in terms of run-time performance as well as
development time.

Speaking of performance, the authors give some advice about how to
minimize the impact of run-time checks. First, put all the expensive
stuff in postconditions and invariants. Then, once a class has been
fairly well tested, turn those off, leaving just the precondition
checking. This strategy is similar to what is [recommended by Sun when
using assertions in
Java](http://java.sun.com/j2se/1.4.2/docs/guide/lang/assert.html): Throw
exceptions if a precondition is violated, and assert postconditions.
Assertions can be turned off at any time to boost performance.

One trick for pushing expensive operations into postconditions is to
introduce derived queries. For example, suppose you have a method with a
precondition, and to check the precondition requires copying a large
list of items. Often you can introduce a derived query to use in the
method's precondition, where the derived query has a post condition that
does the expensive list copy instead.

One of the most important things I learned from the book is simply that
writing contracts is a realistic thing to do, once you know how. By that
I mean it's kind of like my experience with unit testing. I knew about
unit testing for a long time before I ever tried doing it. I always
thought there would be lots of things that were hard to test, but once I
started and learned the techniques, there weren't so many untestable
things as I thought. Design by contract is similar: with some practice
and knowledge of techniques, it is doable.

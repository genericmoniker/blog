Title: The First Rule of Test Code
Date: 2014-01-25 17:03
Author: Eric
Category: Opinion
Slug: the-first-rule-of-test-code
Status: published
Tags: Testing

Software is kind of cool in that you can write programs that verify that
your other programs work correctly. These testing "meta programs" tend
to get short-shrift though, because it's not like the code is actually
part of the shipping product. So who cares about cleanliness or good
style or all that stuff?

I'd propose that a good rule (or at least
[guideline](https://www.youtube.com/watch?v=jl0hMfqNQ-g)) for test code
is:

*Treat it like production code*.

That means things like:

-   Keep methods short
-   Name things appropriately
-   Avoid duplication (like copying and pasting big chunks of code)
-   Add comments if the code isn't self-explanatory for some reason
-   Readability counts
-   etc.

The main justification is that the tests need to be correct and
maintainable too, and all the things we've learned about good code
contribute to those objectives. A large body of unmaintainable tests
starts to become a liability rather than an asset. The one concession
I'd make is that tests pretty much never require their own tests,
because then you have a problem of infinite recursion.

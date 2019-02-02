Title: Testing Styles: Favor Unit Testing
Date: 2003-12-03 13:42
Author: Eric
Category: How-To
Slug: automated-testing
Status: published
Tags: Testing

Ideally, human efforts in testing should focus on building tests --
figuring out the strategies, test cases, and test data. From there, we'd
rather let the computer run the tests and verify the results. If you had
to test everything manually every day, you would either not do it, or
really start to hate your job.

There are many kinds of automated tests. Sometimes the lines between the
types blur a little, and sometimes the vocabulary varies, but I'd like
to discuss two general kinds of automated tests: functional tests and
unit tests. Each type of test has strengths and weaknesses, but together
are complementary, rather than competitive in an automated testing
strategy.

Definitions
-----------

First some simple definitions:

Functional test
:   An automated process that verifies that multiple parts of a system
    work together to correctly fulfill a user's requirements. The test
    attempts to recreate the conditions of the real system.

Unit test
:   An automated process that verifies that a small piece of software
    behaves as the programmer intended. The code being tested tends to
    be isolated from the rest of the system.

Functional Tests
----------------

Functional testing is sometimes also called integration testing, because
it is all about making sure that the smaller parts work together
correctly. In a layered architecture, a functional test may cover
modules at a certain layer and below.

### Strengths

The single greatest strength of functional tests is that they test the
software in the same environment that the software will ultimately be
used in. They test what ultimately matters, and so are vitally
important.

### Weaknesses

Functional tests do have shortcomings, though.

First, they require a working system to run. That is, the code has to be
complete enough to hook the pieces together and do something in order to
test it. This tends to push the functional tests into the later stages
of development. Sometimes engineers give optimistic estimates for
projects, and when the choice comes to ship or slip in order to add
tests, the tests usually lose.

Some parts of the system are hard to test automatically in the context
of the real system. The user interface, for example, can be particularly
thorny (see the References, below, for more on this subject). As an
extreme example, consider printing. The real system context means that
ultimately you've got a piece of paper with some output on it. I can
think of a potential way to test that output automatically (it involves
one of those all-in-one devices that can print and scan, and some
pattern matching software... and maybe a robot) but it starts to become
impractical.

Functional tests also tend to require sophisticated configuration in
order to run. Since they are testing the real system, they require real
data. When I say "real data" in this case, I don't mean that it can't be
contrived test data. I mean that if the system communicates with a
database, there has to be a real database full of data down there.

Unit Tests
----------

Unit tests are a staple of software engineering. Steve McConnell, in
*Code Complete* says, "Regardless of your integration or system-testing
strategy, you should test each unit thoroughly before you combine it
with any others." (p. 592)

### Strengths

Unit testing strategy encourages isolating the code being tested from
the rest of the system. This typically means writing stubs that
implement the same interface as the subsystems the main code will
integrate with.  It's important to realize that a stub provides a
trivial implementation -- you're not rewriting all the functionality of
the system to be stubbed out. At first thought, writing stubs seems
counterproductive, but it actually provides some great benefits.

First, having the stub means you don't need the real thing to do your
own programming. Instead of waiting for someone else to finish their
piece, you can complete your unit that is dependent on it by coding to
your stub. By taking advantage of the stub, you can write unit tests
early in the development cycle, and find and fix defects earlier (and
more inexpensively) than waiting for the integration test. The
integration test will later flush out different interpretations of the
interface between the stub and the real component.

Stubs might make some tests more practical as unit tests than as
functional tests. The printer could be "stubbed out" such that the data
sent there is easier to verify programmatically. This clearly isn't
sufficient to say that printing is working correctly, but it can uncover
a large class of bugs that would probably have required manual testing
if we always sent paper out the printer.

Unit tests can take advantage of stubs to reduce configuration. Instead
of requiring a real database, the test runs against the stub database,
and the test code can communicate with the stub directly to know the
"right answers" in advance. The stubbed version is also easier to get
failures from in order to test error conditions. If the database has a
problem when it runs out of disk space, you don't have to fill up the
disk to test that condition -- the stub database just simulates the
error.

In addition to lighter configuration, independence from the real system
means that unit tests execute very quickly -- there isn't the latency of
starting up the whole system. This quickness lets you run your unit
tests very frequently -- even every time you compile. That moves defect
discovery as early as possible in construction. If a test fails that was
previously working, you've just broken something in whatever you did
since your last compile.

If you write your unit tests very early (even before the code perhaps),
then you're maximizing their usefulness. When writing code, we usually
don't wait until integration to see if anything works. We usually try
things out as we go. That's manual testing, and it takes time and
effort. It makes the most sense to have the automated test from the
start instead of adding them to test routines we've already tested and
debugged manually.

It is easier to get complete coverage of code with unit tests, where
you're able to be "up close" to the code. It's kind of like running
wires through a wall: it's a whole lot easier when the studs are exposed
rather than with the drywall, paint, and outlet covers in place.

Unit tests can reduce unpleasant surprises in some cases. If the system
as a whole calls a unit in a particular way, a functional test might not
catch some defects in the unit -- which is OK because the functionality
isn't used. But if a new feature or bug fix changes the behavior, you
might suddenly find a rat's nest of problems. If the unit has its own
tests, though, you can be confident that changes in usage patterns will
go smoothly.

Finally, an additional benefit of testing in isolation is that it can
improve the design of the code itself. Kent Beck, one of the authors of
the JUnit testing framework, has even argued that unit testing is an
analysis and design technique, and not so much a testing technique. (See
References). The design improvements tend to be in the area of reduced
coupling (which is a huge focus of design generally), since it is hard
to isolate a tightly coupled unit in order to test it in the first
place, but it leads to other improvements as well.

### Weaknesses

One of unit testing's weaknesses is implied by the last strength. If
existing code wasn't written with a fair amount of attention given to
testing and decoupling, it can be very difficult to add unit testing
later. For example, if instantiating an object requires most of the
system to be present, you're going to have a hard time writing a unit
test. A functional test may be the only choice.

Another weakness of unit tests is that stubs are not the same as the
real system -- hence the need for functional tests to ensure that the
system as a whole hangs together correctly.

Conclusion
----------

In my opinion, the balance between effort spent creating functional
versus unit tests should be tilted toward unit tests. Unit tests have a
long list of benefits over functional tests, so focus on getting good
coverage through them. Functional tests should then be used to test
general cases to verify that the whole system hangs together.

References and Resources
------------------------

-   [Testing
    Strategies](http://esmithy.net/wp-admin/not-by-me/TestingStrategies.doc).
    This is a nice summary of different testing types, done by Chip
    Whitmer when he was trying to get things organized here at NextPage.
-   [GuiTesting](http://c2.com/cgi/wiki?GuiTesting). Cunningham &
    Cunningham XP Wiki site. Talks about the technical and sometimes
    political challenges of GUI testing.
-   [The Test/Code Cycle in XP](http://www.xp123.com/xplor/xp0002/).
    Building a GUI using JUnit for testing.
-   [Fire,
    Aim](http://computer.org/software/homepage/2001/05Design/index.htm).
    Kent Beck, *IEEE Software*. Unit testing as a design methodology
    rather than a testing methodology.
-   [Design Principles in Test First
    Coding](http://hammersmith/articles/not-by-me/TestFirstDesign.pdf).
    Erik Meade. More on how unit testing improves design.
-   [Testing, fun?
    Really?](http://www-106.ibm.com/developerworks/library/j-test.html)
    Jeff Canna. Why you need both unit and integration tests.
-   [JUnit Articles](http://www.junit.org/news/article/index.htm). Lots
    of very interesting articles about automated testing (not all
    strictly conforming to my unit test definition).
-   [Unit Testing with
    JUnit](http://esmithy.net/wp-admin/unit-testing/index.htm). My
    presentation about unit testing.
-   [Use your singletons
    wisely](http://www-106.ibm.com/developerworks/webservices/library/co-single.html). J.
    B. Rainsberger. Coupling effects of singletons on testing.
-   [Mock Objects
    Papers](http://www.mockobjects.com/wiki/MocksObjectsPaper). "Mock
    Objects" is a more formalized approach to using stubs.


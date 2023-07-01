Title: Review of "Python Testing with pytest, Second Edition"
Date: 2023-07-01 09:02
Author: Eric
Category: Review
Slug: pytest-book
Status: published
Tags: Testing, Python

![Book Cover]({static}/images/python-testing-with-pytest.png)

Even though I've been using pytest for years, being a testing enthusiast, I thought I'd
read Brian Okken's book to see what I might be able to learn from it. I was pleased to
discover not only several tidbits of the workings of pytest I hadn't known about, but
also some testing strategy advice.

Here are a few examples of the former:

- You can find where fixtures are defined using the `--fixtures` argument. PyCharm can
  locate fixtures with Ctrl+Click but VS Code hasn't implemented that yet, so the
  command line option can be handy.
- `pytest.raises`, the context manager you use when you expect code to raise an
  exception, has a `match` parameter to use a regular expression to check the exception
  message.
- "If a test results in 'Error', the failure is somewhere in a fixture." I had always
  thought that 'Error' just meant some kind of non-assertion exception.
- When parametrizing tests, you can control the test ID for the parametrized cases. It
  honestly hadn't ever occurred to me that it would be nice to do that, let alone that
  it is possible.
- Speaking of parametrization, you can provide a callable to generate the parameters
  instead of listing them statically.

My typical workflows are to run the whole test suite from the command line but jump to
an IDE when running individual tests. Brian's examples throughout the book show how
versatile running tests from the command line can be, doing things like running subsets
of tests and controlling the various output options.

For strategy, Brian provides a simple framework for figuring out what tests to write:

> - Start with a non-trivial, "happy path" test case.
> - Then look at test cases that represent
>     - interesting sets of input,
>     - interesting starting states,
>     - interesting end states, or
>     - all possible error states.

Other advice resonates with my own hard-won experience:

- "We want to focus testing effort on visible end-user behavior, instead of getting lost
  in testing implementation." And "Focusing tests on testing implementation is dangerous
  and time-consuming." Sometimes you do want to test at different levels, but a couple
  of years ago I did a fairly significant database refactor on a project. It took a few
  weeks to make the change and a couple of **months** to fix all the failing tests that
  were too tightly coupled to implementation details.
- "...if you start using monkey-patching and/or mocking more... You'll start to avoid
  mocking and monkey-patching whenever possible." This week, a co-worker, looking at the
  tests in an area where he was fixing a bug, made a comment to the effect of, "I can't
  tell where, or even *if* any application code is being tested because of all the
  mocks!"
- "We're not using Faker for random data, we're using it to avoid making up data
  ourselves." I wrote [a whole other post about
  this]({filename}/randomness-in-tests.md).

Ultimately Brian has done an impressive job giving value to both the beginner and more
experienced user of pytest. The former will want to work through all the exercises and
potentially leave some of the advanced techniques on their "mental bookshelf" until
needed, while the latter can skim the exercises and basics. The conversational tone of
book is also easy to read. After years of listening to Brian on the [Python
Bytes](https://pythonbytes.fm/) podcast, I was hearing the text in his own voice while I
read.

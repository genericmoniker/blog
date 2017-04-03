Title: The Feedback Meeting Game
Date: 2016-09-16 17:03
Author: Eric
Category: Opinion
Slug: the-feedback-meeting-game
Status: published

We hold lots of meetings with the intent to gather feedback from members of a
team. These can be architecture reviews, requirements walkthroughs, sprint or
release retrospectives, and others. How do you conduct meetings like these in
an efficient and productive way?

Some challenges that arise in meetings like these are:

1. People come unprepared, whether because they’re overloaded, forgot about the
meeting until their calendar reminded them, or for whatever reason.
2. Some people have a tendency to talk a lot and dominate the conversation.
3. Some people have a tendency to be quiet and not share potentially valuable
   feedback.
4. The meetings can run longer than seems valuable.

I think that the principles of formal code inspections can help in all kinds of
meetings. These days people often use online code review tools, but when I’ve
done formal inspection meetings, they’ve gone like this:

Initial setup
-------------

1. Participants prepare in advance and bring issues categorized as
   major/minor/other.
2. There is a designated moderator, and their first question to reviewers in
   the meeting is, “Are you ready?” Based on their answers, the meeting can
   proceed or be rescheduled rather than muddling through and wasting people’s
   time.
3. Next, the moderator gathers a count of issues by severity
   (major/minor/other) from each reviewer. This not only gives a concrete
   indicator of readiness, but can also be an interesting metric to track when
   deciding the value of reviews.

The game begins
---------------

1. The moderator goes around the table taking major issues, one per
   participant.
2. If someone doesn’t have any, or any more major issues, they pass.
3. Once all the major issues are gathered, the moderator switches to minor
   issues, then other issues, going around the table again as with major
   issues.
4. The objective is to clearly understand and record the issue, not solve it.
5. The moderator helps make it clear whose “turn” it is and encourages others
   to listen.
6. Participants don’t repeat issues that have already been raised. They
   might participate in any discussion that leads to clear understanding of the
   issue, but that’s it. This is a tough one since people want to feel like
   they’re contributing. One way to address this is to let people with the
   fewest issues go first.
7. The game stops when all issues are understood and
   noted, or the meeting time expires.

Wrap up
-------

1. If metrics are interesting, it can be good at this point to note the number
   of unique issues there were.
2. If there is still meeting time left, and the participants are interested,
   there might be some discussion about how to solve some of the issues.
3. If there isn’t time or interest in the meeting, people can still have
   smaller discussions later about how to solve issues.

This approach to meetings helps ensure that people are prepared, get fair time
to speak, that the discussion moves along efficiently, and that the most
important things are covered. It does, despite me referring to it as a “game”,
promote a more “closed” mode of thinking (see [John Cleese’s talk on
creativity](https://www.youtube.com/watch?v=9EMj_CFPHYc)), so it is more
appropriate for identifying issues rather coming up with creative solutions for
fixing them.

For something like a sprint retrospective, it can be effective to devote
the first part of the meeting to this closed mode of gathering items, then
switch to an open mode for creatively solving the issues the team decides are
most important.

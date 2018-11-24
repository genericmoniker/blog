Title: Automatic Test Cleanup in VS 2008
Date: 2008-02-14 17:43
Author: Eric
Category: Story
Tags: Visual Studio Tips
Slug: automatic-test-cleanup-in-vs-2008
Status: published

I'm working on switching from VS 2005 to VS 2008. I just tried running
some unit tests and got the following dialog:

![clean-up-tests.jpg]({static}/images/clean-up-tests.jpg)

Hooray! I've been trying to figure out how to implement automatic test
cleanup myself, but I (fortunately) hadn't had time to devote serious
effort to it. Up to this point, the TestResults directory would just
continue to grow and grow until you either went in deleted the
directory or ran an Ant target we have for ensuring any testing
left-overs get mopped up.

Title: Work Plan Editor Release
Date: 2006-02-17 17:00
Author: Eric
Category: Project
Slug: work-plan-editor-release
Status: published

A few years ago I got really frustrated trying to maintain a schedule
for my current development assignment. I personally think that having a
schedule, or work plan, is a very good thing. But it was too painful to
maintain one, so I started writing a tool that would help. The result,
now in its third major revision, is the [esmithy.net Work Plan
Editor](http://esmithy.net/software/work-plan-editor/).<!--more-->

Joel Spolsky, in his book Joel on Software (a good read and with a
really long subtitle) counts having a schedule as one of the virtues of
a good software development organization. He also devotes a
[chapter](http://www.joelonsoftware.com/printerFriendly/articles/fog0000000245.html)
to explaining why it isn't so hard to do. I generally agree with what he
has to say except for point number one: Use Microsoft Excel. His
argument is basically that Microsoft Project is too complicated, with
which I agree emphatically. He also says later that developers tend to
not use Excel for anything *other* than schedules, so... um... it makes
sense somehow. OK, Joel helped develop Excel, so maybe he doesn't loathe
it like I do.

One of the real weaknesses of Excel for keeping a schedule is that it is
hard to get a mapping from task estimates to actual dates on a calendar,
which is what my managers tend to be interested in. One of the guys I
used to work with spent hours and hours to put some script behind a
spreadsheet to do that mapping, and it still ended up being pretty
flakey. It's not horrible to do the mapping by hand once or twice, but
in my experience, schedules are highly dynamic and it gets old really
fast to recalculate everything when a few tasks get added, removed or
moved around.

In writing Work Plan Editor, I've tried to stick with the principle of
Joel's point about Excel: Keep it simple. It has the features that you'd
expect in an application (exporting, printing, recent file list and
such) but is still pretty slim. It has also been a great opportunity for
me to learn about .NET, C\# and Windows Forms. I've also learned a
little about [ClickOnce
deployment](http://msdn.microsoft.com/smartclient/understanding/windowsforms/2.0/features/clickonce.aspx),
which is how the application is distributed from the
[software](/software) section of my site.

Feel free to [take it for a
spin](http://esmithy.net/software/work-plan-editor/) to see if it can be
helpful for you.

<!-- Affiliate link --><iframe height="250" scrolling="no" width="120" frameborder="0" src="http://rcm.amazon.com/e/cm?t=sparksfromthesmi&amp;o=1&amp;p=8&amp;l=as1&amp;asins=1590593898&amp;fc1=000000&amp;=1&amp;lc1=0000ff&amp;bc1=000000&amp;lt1=_blank&amp;IS2=1&amp;f=ifr&amp;bg1=ffffff&amp;f=ifr" marginheight="0" marginwidth="0" class="affiliate"></iframe>

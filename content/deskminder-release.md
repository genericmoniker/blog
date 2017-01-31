Title: DeskMinder Release
Date: 2005-06-05 17:00
Author: Eric
Slug: deskminder-release
Status: published

I wrote DeskMinder as a Christmas gift for my family and friends. It
originated as just a bit of HTML and JavaScript as an Active Desktop
component for reminding me when special occasions were drawing near,
like family members' birthdays and anniversaries. To make it easier to
customize the events, I wrote a Windows Forms event editor that goes
along with it.<!--more-->

The most difficult bit was trying to automatically install the widget as
an Active Desktop component. My current implementation is pretty flakey,
so if anyone knows of an elegant way of getting a component on the
desktop, please let me know. Fortunately, once you *do* manage to get it
on your desktop, its pretty smooth sailing from then on.

There were other challenges that I ran into as well, such as a
mysterious movement of events from one day to the previous when data
files traveled west. That turned out to be an XML serialization problem
related to time zones, as described
[here](http://blogs.msdn.com/brada/archive/2004/04/20/117279.aspx). I've
also struggled with using the application settings paths such as
`Application.UserAppDataPath`. No, I really don't want to store my
settings per version, and if I happen to rebrand my application, I don't
want the settings directory to move. I think I got those mainly figured
out, and support for this kind of thing seems like it will be better
with .NET 2.0.

In any case, I've just finished with a new version that supports a
"quote of the day" style feature, so I thought I'd post it here on
esmithy.net. You can find it in the [software](../software) section.

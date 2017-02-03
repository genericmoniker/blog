Title: UI Gem: Android Calendar Time Picker
Date: 2013-07-21 18:39
Author: Eric
Category: Opinion
Tags: Android, User Interface
Slug: ui-gem-android-calendar-time-picker
Status: published

It's been available for a while now, but every time I use the
[new](http://officialandroid.blogspot.com/2013/05/google-calendar-update-for-android.html)
Android calendar app's time controls, I'm so impressed by their
elegance.

Previously, setting the time for a calendar event involved some simple
numeric up/down spinners. Setting the hour worked reasonably well, but
if your event happened to be on the half hour, you'd have to spin and
spin and spin the minutes to get to 30. My first thought was that maybe
they should constrain appointments to start on 5 minute intervals rather
than being able to pick any arbitrary minute. Who has appointments at
3:27 PM after all? The fewer available intervals (3:25 or 3:30, for
example) would mean less spinning.

Instead, the Android UI designers introduced a clock control that looks
like this:

![Hour Picker]({filename}/images/hour-picker.png)

After picking the hour, you're moved automatically to pick the minute:

![Minute Picker]({filename}/images/minute-picker.png)

This interaction has three huge benefits:

1.  It's very natural to pick a time using a clock.
2.  It's really fast to pick the desired time regardless of when it is.
3.  You can still pick an exact minute, so there's no sacrifice of
    time "resolution".

Fantastic.

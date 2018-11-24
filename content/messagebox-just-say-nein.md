Title: MessageBox: Just Say Nein
Date: 2010-06-14 21:28
Author: Eric
Category: How It Works
Tags: User Interface, Windows
Slug: messagebox-just-say-nein
Status: published

The Windows MessageBox is really convenient to use. A single line of
code gets you a dialog box with a caption, a message, an icon and a set
of available buttons that cover a lot of possible input scenarios.
Unfortunately, the text on the buttons is supplied by the system, so if
you're building an application that is intended to be localized, you
invariably end up with something that looks like a bug.

<!--more-->
![German messagebox with English buttons]({static}/images/messagebox.png "Semi-Translated MessageBox")

You're pretty much guaranteed to get an entry in the bug database for
this. My typical response, over many years of writing Windows apps, is
something like this:

> Dear QA engineer,
>
> This dialog's buttons are provided by the system -- we don't have
> control over the text. If you were running a localized version of
> Windows, the "Yes" and "No" buttons would be in the appropriate
> language. Thanks for the report, though!

I've written that more times than I care to admit before finally
thinking, "Why don't I just write a MessageBox where the buttons are
localized?" I'm starting to feel that just the savings in QA/development
back-and-forth time would make the little effort worth it. And if
someone wants to run your application in German, shouldn't it all be in
German regardless of the Windows settings?

Unfortunately other common dialogs, like file dialogs, suffer from the
same problem and aren't so easy to replicate.

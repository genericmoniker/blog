Title: Sleep Mode from .NET
Date: 2007-08-29 22:12
Author: Eric
Category: Programming
Tags: .NET, Windows
Slug: sleep-mode-from-net
Status: published

I have a little backup program that I wrote that includes the ability to
shut down the machine when a backup is complete. I wanted to add the
option of putting the machine to sleep instead of shutting down, but it
took me a while to figure out how to accomplish this.

After using WMI to implement the shut down code, I thought it might be
an equally painful process to enter sleep mode. Once found, however, the
solution is very simple: See
[System.Windows.Forms.Application.SetSuspendState](http://msdn2.microsoft.com/en-us/library/system.windows.forms.application.setsuspendstate.aspx).

For example:

```csharp
Application.SetSuspendState(PowerState.Suspend, true, false);
```

I guess my problem was that I was Googling for the user-centric term
"sleep" instead of searching for "suspend", and if you throw "sleep" and
"C\#" into a search, you tend to get a lot of threading results.

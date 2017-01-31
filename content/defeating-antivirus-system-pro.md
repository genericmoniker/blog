Title: Defeating Antivirus System Pro Date: 2009-12-03 22:46 Author:
Eric Category: Misc Slug: defeating-antivirus-system-pro Status:
published

Antivirus System Pro is an irksome piece of malware that holds your
computer hostage until you pay a ransom. It is nothing short of
extortion. I just spent a few evenings removing it from a friend's
computer, and the dozens of articles on the web (and even YouTube
videos) were all wrong about how to get rid of this instance.

<!--more-->
The program throws up all kinds of messages saying that the computer is
infected, and occasionally sends Internet Explorer off to a porn or
Viagra site for good measure -- I guess to make the "infection" seem
more urgent. It also prevents new processes from starting, except for
IE, since they presumably need to leave a way open for you to pay your
ransom. The program sets up a proxy server for IE, though, so you can't
get anywhere but Antivirus System Pro's site.

Usually in a situation like this, I use the [Ultimate Boot CD for
Windows](http://www.ubcd4win.com/). The scans I ran that way didn't find
anything, though.

Other information on the internet suggests booting the system in Safe
Mode and running [Malwarebytes
Anti-Malware](http://www.malwarebytes.org/mbam.php) to clean the system.
This also didn't work.

There are several sites that give [manual removal
instructions](http://www.ehow.com/how_5146071_manually-remove-antivirus-system-pro.html).
On my friend's system, none of the binaries or registry keys from the
instructions existed.

Here's what I did that appears to have worked:

 1. Get a copy of [Process
        Explorer](http://technet.microsoft.com/en-us/sysinternals/bb896653.aspx),
    probably easiest done on another machine and put on a USB flash
    drive.
 2. Boot the computer normally.
 3. Let the race begin. Start Process Explorer before Antivirus System
    Pro does.
 4. Bring up Antivirus System Pro's scan window.
 5. Use the Process Explorer's "Find Window's Process" tool by dragging
    it over the scan window.
 6. Now you know the executable that is Antivirus System Pro, which was
    bsuhsysgaurd.exe on my friend's machine.
 7. By showing the "Image Path" column in Process Explorer, you can also
    see where it is running from.
 8. Go ahead and kill the process. It feels good.
 9. Delete the executable.
10. Search the registry for references to the executable and delete
    those (such as from Start keys).
11. Get rid of the proxy in IE by going to **Tools &gt; Internet Options
    &gt; Connections** &gt; **LAN Settings** and uncheck "Use a proxy
    server for your LAN".

I also installed the newly free [Microsoft Security
Essentials](http://www.microsoft.com/Security_Essentials/) on my
friend's machine, since although there was a version of MacAfee on
there, it was FUBAR. I'm not sure if that was something Antivirus System
Pro had accomplished or if it being that way was what let the malware
through in the first place.

All seems well for now...

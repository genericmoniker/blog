Title: IIS Configuration with WiX and Appcmd 
Date: 2010-07-02 14:35
Author: Eric
Category: How-To
Slug: iis-configuration-with-wix-and-appcmd
Status: published

I recently spent some time building an install package for a web
application using WiX. There are some nice IIS extensions for WiX to
help with that, but they're missing the ability to set some advanced
properties, like an Application Pool's "Enable 32 Bit Applications"
property.

Matt Honeycutt has a [helpful
posting](http://trycatchfail.com/blog/post/WiX-Snippet-change-enable32BitAppOnWin64.aspx)
on his blog about this. The basic idea is that you use a custom action
to invoke Appcmd.exe and do whatever you need, and that can be done
entirely with WiX markup -- no separate coding required.

I did need to alter Matt's approach a little, though, because it didn't
work for me as it was. I would have just commented about this on his
blog, but comments are closed.

When I ran my installer, I got a vague error saying that the custom
action had failed. Running the MSI from the command line with the
logging switch, and looking at the MSI log file didn't help. There was
output saying that it was going to run the custom action, but no
indication that it had failed, no result code from the Appcmd process,
and nothing from stderr. It *did* show the complete command line for the
action, however, so I copied it out into a command prompt and ran it.
That failed saying I needed administrator privileges. Running in a
command prompt started with "Run as Administrator" worked just fine.

It turns out that by default, custom actions impersonate the user that
started the install, without the administrator elevation that the
installer itself runs under. This can be changed by setting the
CustomAction's Impersonate attribute to "no". That also required adding
Execute="deferred", and as a result, having the custom action run before
InstallFinalize rather than after.

Here's what it looks like:

```xml
<InstallExecuteSequence>
  <Custom Action="ConfigureAppPools" 
             Before="InstallFinalize"><![CDATA[NOT Installed AND VersionNT64 >= 600]]></Custom>
</InstallExecuteSequence>

<!-- Snip -->

<CustomAction Id="ConfigureAppPools" 
    Execute="deferred"
    Impersonate="no"
    Return="check"
    Directory="TARGETDIR"
    ExeCommand="[SystemFolder]inetsrv\appcmd set apppool /apppool.name:"[APPPOOLNAME]" /enable32BitAppOnWin64:true" />
```

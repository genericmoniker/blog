Title: Converting from Visual Studio 2005 to Visual Studio 2008
Date: 2008-02-15 18:12
Author: Eric
Tags: Visual Studio Tips
Slug: converting-from-visual-studio-2005-to-visual-studio-2008
Status: published

I've just finished switching over our development environment from
Visual Studio 2005 to Visual Studio 2008 (except for a C++ solution that
uses boost, which will take some further effort). These are the things
that I needed to do, and the gotchas I encountered.

<!--more-->

1.  **Getting installed** - Aside from being a lengthy experience,
    installing VS 2008 went pretty smoothly on our machines except for
    my own primary development box. The Web Authoring Component
    didn't install. There is a [long discussion
    thread](http://forums.microsoft.com/forums/ShowPost.aspx?PostID=2790764&SiteID=1)of
    people with the same problem, apparently caused by having
    pre-release versions of Microsoft software. In my case, I had a
    prerelease version of Expression Web on my machine, and uninstalling
    that allowed the VS 2008 install to complete normally.
2.  **Converting solutions** -When you open a VS 2005 solution in VS
    2008, the Conversion Wizard shows up automatically. It seemed like
    this was going to be an easy part, but none of the unit test
    projects converted correctly. This is apparently a bug, and a
    [byzantine workaround is
    posted](http://forums.microsoft.com/MSDN/ShowPost.aspx?PostID=2668977&SiteID=1)
    on the MSDN Forums. Fortunately, John Carneiro posted a tool that
    automatically applies the workaround (in the same forum thread as
    the workaround).
3.  **Fixing** **unit test framework references** - Part of our build
    process uses MSTest.exe to run our unit tests. When I first tried
    this, I got this error message: "The test DLL 'Common.Tests.dll' was
    built using Visual Studio 2005, and cannot be run. To resolve this
    issue please rebuild the test DLL using the current version of
    Visual Studio". Since I had just rebuilt everything with VS 2008,
    this was somewhat puzzling. Eventually I figured out that by
    "...built using Visual Studio 2005...", the error message was really
    trying to say "...built referencing the Visual Studio 2005 version
    of the unit test framework...". While the instructions for upgrading
    the unit test projects said to fix references to
    `Microsoft.VisualStudio.QualityTools.UnitTestFramework` to reference
    version 9.0.0.0 instead of 8.0.0.0, John's tool apparently didn't do
    that for me.
4.  **Finding a new strategy for Sgen** - I've written about [generating
    XML serialization
    assemblies](/2007/06/13/generating-xml-serialization-assemblies/) in
    the past, and how I came up with a command line to use as a
    post-build step. I discovered, however, that sgen.exe is not in the
    same place in the VS 2008 install. This led me to a better solution
    anyway of using the [Sgen MSBuild
    task](http://msdn2.microsoft.com/en-us/library/ms164303.aspx)
    instead, as suggested
    [here](http://blog.devstone.com/aaron/archive/2008/02/07/2778.aspx).
5.  **Removing the /Wp64 switch** - Some of my projects are C++/CLI, and
    had the /Wp64 switch on. This produces a warning now: "Command line
    warning D9035 : option 'Wp64' has been deprecated and will be
    removed in a future release". I guess the reason for deprecating the
    option is that if you want to check for 64 bit compatability issues,
    you can just run the 64 bit compiler, according to [this
    post](http://blogs.msdn.com/branbray/archive/2005/07/08/437078.aspx).
    I just turned off the "Detect 64-bit Portability Issues" in
    the project C++ options. 

There were also some miscellaneous things that are less applicable to
other development teams:

1.  We have an Ant task that builds Visual Studio solutions by invoking
    DEVENV.COM, and that needed to be updated to correlate the version
    10 solution file format with the appropriate path to DEVENV.COM.
2.  We have a test runner application (a thin wrapper over MSTest.exe)
    that needed to be updated a little.
3.  We use TeamCity for continuous builds, and that needed some
    attention as well (still working on those details).


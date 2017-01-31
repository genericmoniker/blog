Title: XP Common Controls with VC++ 2005
Date: 2006-05-09 17:00
Author: Eric
Tags: Visual Studio Tips
Slug: xp-common-controls-with-vc-2005
Status: published

This morning I was asked to enable the Windows XP visual styles for our
application. No problem -- I've done that for applications many times.
Just drop the appropriate manifest file in the right place, call
`InitCommonControls` and all should be well. When I tried that this
morning, though, I got an error message: "An application has made an
attempt to load the C runtime library incorrectly. Please contact the
application's support team for more information." I suspected our
support team wasn't going to be much help on this one. The Visual C++
2005 runtime library configuration strikes again.<!--more-->

![Runtime Error]({filename}/images/runtime-error1.jpg)

Previous versions of Visual Studio and Visual C++ let you install the
runtime libraries by simply copying them to a directory where your
application could access them. The version 8 runtime libraries, however,
must be installed in side-by-side mode, and your application must have a
manifest that references the runtime libraries. MSDN has a [Deployment
Examples](http://msdn2.microsoft.com/en-us/library/ms235285.aspx)
article that details this.

Because of this need, C++ projects in VS 2005 are already configured to
include the appropriate manifest file that specifies dependencies on the
exact versions of the runtime libraries. By dropping another manifest in
the application directory (with a name like MyApp.exe.manifest) it
overrode the manifest that was embedded within the binary itself. The
overriding manifest only included the common controls library
dependency, which caused the error mentioned above.

Embedding the manifest file as a resource in the binary seems preferable
anyway (why install two files if one will do?), so there's fortunately
an easy way to merge the common controls manifest with the
auto-generated manifest. In the project properties, go into
**Configuration Properties** &gt; **Manifest Tool** &gt; **Input and
Output** and reference your manifest file in the Additional Manifest
Files field:

![Project Settings]({filename}/images/project-settings-manifest1.jpg)

Also, don't forget to call `InitCommonControls` in your application
somewhere (preferably near the beginning!), which is declared in
commctrl.h and defined in comctl32.lib, or all the manifest business
will be in vain -- you'll still not get the XP style controls.

Here's a copy of a manifest file that is ready to use with any project:

[XPCommonControls.manifest](/content/XPCommonControls.manifest)

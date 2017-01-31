Title: File System Monitoring
Date: 2006-07-21 17:00
Author: Eric
Tags: Windows
Slug: file-system-monitoring
Status: published

At times it is useful to keep tabs on what is happening (or has
happened) in the file system. This is a brief overview of all the ways I
know of to track activity on a Windows file system.<!--more-->

Scanning
--------

Scanning is the brute-force approach to knowing what is happening in the
file system. The relevant Win32 APIs are `FindFirstFile` and
`FindNextFile`. Limitations to this approach are that it is slow and
resource intensive, and it can't detect file deletions unless it can
compare against a previous snapshot of the file system.

Change Notifications
--------------------

The Win32 APIs `FindFirstChangeNotification` and
`FindNextChangeNotification` let you monitor a volume subtree and be
notified when a particular class of file changes occurs. The main
limitation of this approach is that these APIs don't actually tell you
what changed (unless what you're watching is *really* narrow), just that
something did.

To know what changed, you need to use `ReadDirectoryChangesW` instead.
This is much more efficient than scanning, but changes can be missed if
your application isn't running, or if the buffer supplied to
`ReadDirectoryChangesW` overflows.

I think the documentation for the .NET Framework
[`FileSystemWatcher`](http://msdn2.microsoft.com/en-us/library/system.io.filesystemwatcher.aspx)
class (which clearly uses `ReadDirectoryChangesW` in its implementation)
is actually better at explaining the limitations and pitfalls than the
documentation for `ReadDirectoryChangesW` itself.

Change Journal
--------------

The [change
journal](http://msdn2.microsoft.com/en-us/library/aa363798(VS.85).aspx "Change Journal Documentation")is
a feature of NTFS 5.0 (Windows 2000). It keeps a persistent record of
all changes to a volume, which can then be queried by an application to
see what has changed. This is more efficient than scanning, and doesn't
require that your application be running in order to catch all the
changes.

The change journal obviously requires NTFS so if you need to monitor FAT
volumes, this isn't the solution. Also, other applications can actually
turn the change journal off, so you might still have to resort to
scanning if this were to happen (and it *is* detectible) to be sure that
something wasn't missed. Finally, you need administrator privileges to
query the change journal. I guess it would be too hard to enforce all
the access rights to the file system and keep the journal efficient.

Distributed Link Tracking
-------------------------

[Distributed Link
Tracking](http://msdn.microsoft.com/en-us/library/aa363997.aspx) is
another NTFS 5.0-only approach. It was created to solve the problem of
broken shortcuts and OLE links. The interesting thing about link
tracking is that with it you can actually detect moves to other
machines, renames of machines or network shares that would otherwise
"break" a known path, or even physical moves of a volume to another
machine (but not removable media).

Link tracking is a polling system -- you don't get notified when a file
moves or gets renamed. Instead you have to ask where a particular file
is.

You can try out the functionality by creating a shortcut to any file.
Now rename the original file and double-click the shortcut. It should
still resolve correctly to the renamed file. Move the file to some
network share on the domain and the shortcut will still work. Another
user can also move a file, and as long as the location to which it was
moved can be resolved to a path, the link tracking service can find it.

You can also use
[fsutil](http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/fsutil_objectid.mspx?mfr=true),
a built-in Windows utility, to manipulate object identifiers (OIDs) that
are used to implement link tracking.

I wrote a little Windows Forms program to explore using link tracking
programmatically. Here's the interesting part of the code (I got the
needed interop signatures from [pinvoke.net](http://pinvoke.net)):

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;    

namespace FileTracker
{
    public partial class MainForm : Form
    {
        IShellLinkW shellLink;    

        public MainForm()
        {
            InitializeComponent();
        }    

        private void TrackFile(string fileName)
        {
            shellLink = (IShellLinkW)Activator.CreateInstance(
                Type.GetTypeFromCLSID(UnsafeNativeMethods.CLSID_ShellLink));
            shellLink.SetPath(fileName);
            shellLink.SetDescription("File Tracker Link");
        }    

        private string ResolveFile()
        {
            if (shellLink != null)
            {
                shellLink.Resolve(IntPtr.Zero,
                    UnsafeNativeMethods.SLR_FLAGS.SLR_UPDATE |
                    UnsafeNativeMethods.SLR_FLAGS.SLR_NO_UI |
                    UnsafeNativeMethods.SLR_FLAGS.SLR_NOSEARCH);    

                StringBuilder path = new StringBuilder(256);
                UnsafeNativeMethods.WIN32_FIND_DATAW findData =
                    new UnsafeNativeMethods.WIN32_FIND_DATAW();
                shellLink.GetPath(path,
                    path.Capacity,
                    out findData,
                    UnsafeNativeMethods.SLGP_FLAGS.SLGP_UNCPRIORITY);    

                if (File.Exists(path.ToString()))
                {
                    return path.ToString();
                }
                else
                {
                    return path.ToString() + " (deleted?)";
                }
            }    

            return string.Empty;
        }    

        private void btnBrowse_Click(object sender, EventArgs e)
        {
            OpenFileDialog dialog = new OpenFileDialog();
            dialog.Title = "Choose File to Track";
            if (dialog.ShowDialog(this) == DialogResult.OK)
            {
                tbOriginal.Text = dialog.FileName;
                tbCurrentLocation.Text = string.Empty;
                TrackFile(dialog.FileName);
            }
        }    

        private void btnResolve_Click(object sender, EventArgs e)
        {
            tbCurrentLocation.Text = ResolveFile();
        }
    }
}
```

File System Filter Driver
-------------------------

A filter driver can see everything that happens to the file system
because it is inserted between the IO manager and the underlying file
system implementation. I don't have any personal experience with this
approach, but there is [abundant
documentation](http://www.microsoft.com/whdc/driver/filterdrv/default.mspx)
from Microsoft on filter drivers.

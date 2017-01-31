Title: .NET Context Menu Handler
Date: 2005-04-07 17:00
Author: Eric
Category: Programming
Tags: .NET, Windows
Slug: net-context-menu-handler
Status: published

I've been working on a context menu handler shell extension in C\#
lately. There are a few samples that people have produced on the web
(for example, [The Code
Project](http://www.codeproject.com/csharp/ratingcolumn.asp),
[pek.com](http://www.pek.com/blogs/pek/archives/2005/02/c_explorer_cont.php),
and
[TheServerSide.net](http://www.theserverside.net/articles/showarticle.tss?id=ShellExtensions)).
I've found a better way of implementing `IShellExtInit.Initialize` than
in the examples I've seen.

<!--more-->

The point of `IShellExtInit.Initialize` is for the shell to let your
handler know which files are selected so that you can display your
context menu based on, believe it or not, *context*. Here is a typical
implementation:

```csharp
int IShellExtInit.Initialize (IntPtr pidlFolder, IntPtr lpdobj, uint hKeyProgID)
{
  try
  {
    // save the information about the selection
    m_dataObject = null;
    if (lpdobj != (IntPtr)0)
    {
      m_dataObject = (ShellLib.IDataObject)Marshal.GetObjectForIUnknown(lpdobj);
      FORMATETC fmt = new FORMATETC();
      fmt.cfFormat = CLIPFORMAT.CF_HDROP;
      fmt.ptd = 0;
      fmt.dwAspect = DVASPECT.DVASPECT_CONTENT;
      fmt.lindex = -1;
      fmt.tymed = TYMED.TYMED_HGLOBAL;
      STGMEDIUM medium = new STGMEDIUM();
      m_dataObject.GetData(ref fmt, ref medium);
      m_hDrop = medium.hGlobal;
    }
  }
  catch(Exception)
  {
  }
  return 0;
}
```

Then later on, to get the selected file:

```csharp
// Get the file name to work with
StringBuilder sb = new StringBuilder(1024);
Helpers.DragQueryFile(m_hDrop, 0, sb, sb.Capacity + 1);
```

There's a fair amount of nasty interop going on here, which is sometimes
inevitable for things like shell extensions. In this case, however, you
can actually use the .NET Framework's DataObject class instead for much
simpler code:

```csharp
int IShellExtInit.Initialize (IntPtr pidlFolder, IntPtr lpdobj, uint hKeyProgID)
{
  DataObject dataObject = new DataObject(lpdobj);
  string[] selectedFiles = (string[])dataObject.GetData(DataFormats.FileDrop);
}
```

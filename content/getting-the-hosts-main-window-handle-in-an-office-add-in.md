Title: Getting the Host's Main Window Handle in an Office Add-in
Date: 2008-01-23 15:26
Author: Eric
Category: How-To
Tags: .NET, Office
Slug: getting-the-hosts-main-window-handle-in-an-office-add-in
Status: published

Sometimes you want the window handle of the host application when you're
writing an Office add-in. Excel includes that as a property of the
Application object in newer versions of the object model, but Word and
PowerPoint don't. I seem to remember some sample code from Microsoft
that suggests using FindWindow to get the handle, but that always seems
problematic:

-   You can search by class name (e.g. "OpusApp" for Word), but what if
    you somehow have multiple Word processes running? Which window do
    you get?
-   You can search by window text, but it can be really hard to figure
    out what the window text is.
-   You can set the Caption property on the Application object to some
    magic text and search for a window with the magic text, but Word
    throws all kinds of other stuff into the caption so this generally
    doesn't work reliably.

Instead, if you're using managed code, you can just do this:

```csharp
IntPtr hwnd = Process.GetCurrentProcess().MainWindowHandle;
```

Underneath this uses `EnumWindows` and `GetWindowThreadProcessId` to
find the right window.

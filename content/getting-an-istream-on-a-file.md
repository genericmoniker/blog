Title: Getting an IStream on a File
Date: 2007-04-28 14:03
Author: Eric
Tags: Windows
Slug: getting-an-istream-on-a-file
Status: published

Getting a COM `IStream` instance on a normal file seems like something
that should be trivial to do, but it always seems to take some hunting
to remember how it is actually done.<!--more-->

There is a function in the shell API that will return an `IStream` on a
file:
[SHCreateStreamOnFile](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/shellcc/platform/shell/reference/shlwapi/version/shcreatestreamonfile.asp "MSDN Documentation"). It
is in version 5 or later of the shell, which is the version that shipped
with Windows 2000, but comes along with IE 5 or later for older
operating systems.

I've also heard people suggest that there is a similar function in the
Extended MAPI library, but using the shell seems generally more
palatable.

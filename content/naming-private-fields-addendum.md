Title: Naming Private Fields (Addendum)
Date: 2007-01-30 17:00
Author: Eric
Category: Programming
Slug: naming-private-fields-addendum
Status: published

This is just a quick addition to the [previous
posting](http://esmithy.net/2007/01/10/naming-private-fields/),
confirming the alleged use of `m_` by Microsoft in their own
code.<!--more-->

[Lutz Roeder's .NET Reflector](http://www.aisto.com/roeder/dotnet/) is a
fascinating tool for various reasons, including its ability to show all
the .NET Framework classes that use prefixes on member variables. There
are a bunch. Here is a very small sample of venerable classes that use
`m_`:

-   System.Int32
-   System.String
-   System.Threading.Thread
-   System.Reflection.Assembly
-   System.Environment
-   System.Globalization.CultureInfo
-   System.Net.Connection
-   System.Net.HttpWebRequest
-   System.Net.IPAddress
-   System.Uri
-   System.WeakReference

And here are a few of the classes that use a leading underscore for
field names, though there aren't as many in this category:

-   System.AppDomain
-   System.Guid
-   System.Console
-   System.Exception
-   System.Collections.ArrayList
-   System.Delegate
-   System.TimeSpan


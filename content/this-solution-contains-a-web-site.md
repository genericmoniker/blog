Title: This solution contains a web site...
Date: 2010-05-06 10:50
Author: Eric
Tags: Visual Studio Tips
Slug: this-solution-contains-a-web-site
Status: published

I kept getting a message from Visual Studio 2008 when opening a solution
saying:

> This solution contains a web site at 'http://localhost/Services'.
> There is already a web site at this location on this computer. Do you
> wish to use this existing location for your web site (existing files
> will be overwritten)?

It looks like the (one?) cause is a corrupt solution file.

[Many](http://bloggingabout.net/blogs/rick/archive/2007/12/06/quot-some-of-the-properties-associated-with-the-solution-could-not-be-read-quot.aspx)
[people](http://blogs.msdn.com/rjohri/archive/2010/03/11/some-of-the-properties-associated-with-the-solution-could-not-be-read.aspx)
[have](http://esersahin.wordpress.com/2009/01/02/some-of-the-properties-associated-with-the-solution-could-not-be-read/)
reported that they get a warning when opening a solution saying:

> Some of the properties associated with the solution could not be read.

The problem in that case was that there are multiple
"GlobalSection(TeamFoundationVersionControl) = preSolution" sections in
the solution file. This was true for my situation as well, and repairing
the .sln file seems to have fixed the prompt about an already existing
web site.

I originally tried editing the .sln file by hand to remove the duplicate
section, but then I *started* getting the "Some of the properties..."
message. I think it works better to use Visual Studio to unbind and
rebind the source control.

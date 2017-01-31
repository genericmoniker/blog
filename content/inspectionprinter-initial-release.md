Title: InspectionPrinter Initial Release
Date: 2005-04-26 17:00
Author: Eric
Slug: inspectionprinter-initial-release
Status: published

I've released the first version of my InspectionPrinter utility. We have
been renewing our efforts to do more formal code inspections at NextPage
recently, which finally motivated me to finish this thing off, having
originally started it nearly two years ago. It can be downloaded from
the [software](/software) section.<!--more-->

The original motivations for creating were:

1.  It bugged me that it would take so long to figure out all the
    printing settings to get a good amount of code on a page with line
    numbers using whatever IDE was current at the time.
2.  I didn't like printing out lots of pages for optional reviewers who
    just ended up throwing it away.
3.  I wanted something that would be consistent regardless of the
    programming language being used.

InspectionPrinter was written in C\#, integrating with HTMLDOC to
produce a PDF document. I was pleasantly surprised at how easy it was to
use the .NET Framework to incorporate an external command-line tool. The
System.Diagnostics.Process class is really fantastic, allowing silent
running of the external executable and easy capture of stdout.

Going forward I'd really like to be able to do diff printouts as well,
since we sometimes want to inspect bug fixes that might touch several
large files in small ways, and including all the code isn't so helpful.

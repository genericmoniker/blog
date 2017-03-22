Title: InspectionPrinter - Prepare source code for inspection
Date: 2007-04-23 21:43
Author: Eric
Category: Project
Slug: inspectionprinter
Status: published

InspectionPrinter is a utility to help get source code ready for a
formal inspection.

Download
--------

**[Install via
"ClickOnce"]({filename}/downloads/inspection-printer/InspectionPrinter.application)**  
Version 1.1.2326.36040  
15 May 2006  
Around 1.7 MB

Inspection Printer depends on the Microsoft .NET Framework 2.0, which
can be obtained through [Windows
Update](http://windowsupdate.microsoft.com "Windows Update").

Note: Installing the software means that you agree to the
[license](#license).

Note for **Firefox** users: Microsoft's
[ClickOnce](http://msdn.microsoft.com/clickonce "ClickOnce") technology may
require an add-on to work (such as the Microsoft .NET Framework Assistant
add-on).

If you have a previous version that was installed through a normal
Windows Installer setup script, you can uninstall that version

About Inspection Printer
------------------------

Inspection Printer is a utility to help get source code ready for a
formal inspection. Despite its name, Inspection Printer doesn't actually
print anything. Instead, it creates a PDF file that can be sent to
reviewers. The PDF contains a cover sheet, a table of contents, and
source files with monochrome syntax highlighting. Highlighting is
supported for C++, C\# and Java. Here is a sample output file:
**[sample.pdf]({filename}/downloads/inspection-printer/sample.pdf "Sample Output")**

_Screen Shot_

![Screen Shot]({filename}/downloads/inspection-printer/screen-shot.gif "InspectionPrinter Screen Shot")

### Features

-   Cover page with a form for reviewer statistics and author comments
-   Table of contents with links
-   Lines of code counter (blank lines and comments are not counted)
-   Code output with line numbers and monochrome (printer-friendly)
    syntax highlighting
-   Unambiguous page numbers (page numbers don't start over for each
    source file)
-   Snazzy Windows Forms GUI

### Change History

#### 15 May 2006 - Version 1.1.2326.36040

-   ClickOnce deployment
-   Fixed a problem that prevented C\# files from being recognized
    correctly
-   Better error handling when a file type isn't recognized
-   Added a command to refresh the file line counts

#### 22 Sep 2005 - Version 1.1.0

-   Fixed incorrectly anchored "lines of code" controls
-   Added a line count that includes comments
-   Ctrl+A in the files list selects all files
-   Made the "Add Files..." file dialog start in the location of the
    last added file

License
-------

### Copyright

The software, the documentation and all other content of the distributed
package except HTMLDOC copyright 2003-2006 Eric Smith. All rights
reserved.

HTMLDOC, which is copyrighted by [Easy Software
Products](http://www.easysw.com/), is released under the GNU GPL
license.

### Terms of Use

Permission is hereby granted to use this software, for both commercial
and non-commercial purposes, without limitations and free of charge.
Permission is hereby granted to copy and distribute the software for
non-commercial purposes. A commercial distribution is NOT allowed
without prior written permission of the author.

### Warranty

This software is supplied "AS IS". The author disclaims all warranties,
expressed or implied, including, without limitation, the warranties of
merchantability and of fitness for any purpose. The author assumes no
liability for direct, indirect, incidental, special, exemplary, or
consequential damages, which may result from the use of this software,
even if advised of the possibility of such damage.

### Submissions

The author encourages the submission of comments and suggestions
concerning this software. All suggestions will be given serious
technical consideration. By submitting material to the author, you are
granting the right to make any use of the material deemed appropriate,
i.e. any communication or material that you transmit to the author by
electronic mail or otherwise, including any data, questions, comments,
suggestions or the like, is, and will be treated as, non-confidential
and nonproprietary information. The author may use such communication or
material for any purpose whatsoever, including, but not limited to,
reproduction, disclosure, transmission, publication, broadcast and
further posting. Further, the author is free to use any ideas, concepts,
know-how or techniques contained in any communication or material you
send for any purpose whatsoever, including, but not limited to,
developing, manufacturing and marketing products.

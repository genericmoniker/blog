Title: Batch File Libraries
Date: 2011-07-12 20:19
Author: Eric
Category: Programming
Tags: Windows
Slug: batch-file-libraries
Status: published

I've always considered batch files as kind of ghetto. Anything too
complex devolves into a morass of gotos and labels. But I recently put
together some install batch scripts that I was actually pleased with,
including a clean mechanism for sharing common code.

<!--more-->
A while back, I used [WiX](http://wix.sourceforge.net/) to
build an installer, which was handed off to IT to deploy a web site.
After a fair amount of anguish and frustration, I eventually realized
that my installer was essentially a difficult to create and maintain
batch file. Half the project was just custom command calls out to
appcmd.exe anyway. If you're so unfortunate as to absolutely have to
create an MSI install, WiX isn't a bad way to go, but it was a layer of
massive unnecessary complexity in my case. Instead, I ended up creating
a [7zip
self-extractor](http://www.msfn.org/board/topic/39048-how-to-make-a-7-zip-switchless-installer/)
that ran an actual batch file when launched.

One challenge is that I actually had a few installers, and I wanted to
share code between them, which I was able to do after discovering the
[CALL](http://technet.microsoft.com/en-us/library/cc772743(WS.10).aspx)
command. Here's an example:

    call lib.cmd CopyFiles "C:\ServiceInstallDir"

This is essentially a function call, where "CopyFiles" is the name of
the function, and "lib.cmd" is the file where it is implemented.
Arguments follow the name of the function, the destination directory
being the single argument in this case.

The lib.cmd file looks something like this:

```batch
@echo off
REM Within the "function" the args will be shifted, so 3 here becomes 2, 2 becomes 1, etc.
call :%1 %2 %3 %4 %5 %6 %7 %8 %9
goto :EOF

:Heading
REM %1 - Text for heading
echo ------------------------------------------------------
echo ^| %~1
echo ------------------------------------------------------
goto :EOF

:CopyFiles
REM %1 - Install directory
call :Heading "Copying files..."
if exist "%~1" rd /s /q "%~1"
md "%~1"
xcopy *.* "%~1" /s
goto :EOF
```

Each label in this file acts as a function call. The CALL at the
beginning passes control off to the label, including the additional
arguments. The function ends by jumping to the special :EOF label (which
exits the batch context). Note also that functions can call each other,
as where the "CopyFiles" function calls the "Heading" function.

It's a great way to encapsulate little bits of functionality in a common
place.

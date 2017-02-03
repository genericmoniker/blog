Title: git-flow with Cmder
Date: 2015-01-06 20:35
Author: Eric
Category: How-To
Tags: Git
Slug: git-flow-with-cmder
Status: published

["Git Flow"](http://nvie.com/posts/a-successful-git-branching-model/) is
a branching model using the Git version control system. There is also a
[set of extensions for Git](https://github.com/nvie/gitflow) that make
using Git Flow easier, but there aren't installation instructions
specifically for use with the excellent
[cmder](http://bliker.github.io/cmder/) Windows shell replacement.
Here's how to do it...

<!--more-->

These instructions are basically the same as for
[msysgit](https://github.com/nvie/gitflow/wiki/Windows#msysgit), but
tweaked slightly.

1.  Download the [util-linux zip
    file](http://downloads.sourceforge.net/gnuwin32/util-linux-ng-2.14.1-bin.zip)
    and extract getopt.exe into the msysgit bin directory under cmder.
    For example: C:\\tools\\cmder\\vendor\\msysgit\\bin
2.  Download the [dependencies zip
    file](http://sourceforge.net/projects/gnuwin32/files/util-linux/2.14.1/util-linux-ng-2.14.1-dep.zip/download?use_mirror=colocrossing)
    and extract the two DLLs in 'bin' to the same place
3.  Clone the gitflow repo:

    `λ git clone --recursive git://github.com/nvie/gitflow.git`
4.  Run the install script, specifying the right directory (notice that
    'bin' is not included):

    `λ gitflow\contrib\msysgit-install.cmd C:\tools\cmder\vendor\msysgit`

After that, you should be able to use the various `git flow`
[commands](http://danielkummer.github.io/git-flow-cheatsheet/).

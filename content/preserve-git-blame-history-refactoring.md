Title: Preserving Git Blame History when Refactoring
Date: 2020-08-15 17:36
Author: Eric
Category: How-To
Tags: Git
Slug: preserve-git-blame-history-refactoring
Status: published

I have some big source files in a project I'm working on. Embarrassingly big
files -- multiple thousands of lines long. Those files also have years of Git
blame history associated with them, and not wanting to lose that history has
deterred me from refactoring to break those files into more manageable modules.
It is wonderful, after all, to turn on blame/annotate in my editor to see what
bozo made the last edit (Oh, wait, *I* did that?) as well as when and why.

If you Google about this problem, there are a bunch of StackOverflow and blog
posts about it, which I'll divide into two categories:

1. Lofty Git expositions that tell you Git just doesn't work that way, implying
   that you don't *really* want what you think you want.
2. Pragmatic steps you can take to coerce Git to keep the blame history when
   splitting files apart.

I was partial to category #2, because I was pretty sure I *did* want to
preserve the history, and if the tool needed some arm twisting, so be it.

Unfortunately, the general workflow for category #2 involves a lot of copying
files and deleting the parts you don't want in the final file. So if you want
to split a file into 5 files, make 5 copies of the original and edit each one
to delete the lines you don't want in that copy, with some strategically placed
commits along the way. I actually did this once, and it took the better part of
an incredibly tedious day to accomplish. This is where programmers naturally
think, "There really needs to be a tool to automate this." So [I made
one](https://github.com/genericmoniker/git-split).

I based the tool on a couple of blog posts by [Raymond
Chen](https://devblogs.microsoft.com/oldnewthing/author/oldnewthing), because
he's smart and had nice step-by-step instructions with simple examples. I was
coding away, having fun with the elusive promise of a side-project that might
actually be useful. I had unit tests that followed Raymond's example, and they
all passed! It was time to try my nifty tool in the real world... where it
immediately failed for one of the primary uses. `git-blame` showed *me*, the
one splitting the file, as the author of all of the lines in the extracted
file, rather than the original authors.

Humbled a bit, I had to go back to category #1 of the posts about how Git
works. Funny thing, if you're writing a tool to extend the functionality of
some other tool, it is good to understand how the original tool works.

One of those posts led me to this [explanation from Linus
Torvalds](http://web.archive.org/web/20090423040902/http://article.gmane.org/gmane.comp.version-control.git/217)
about the difference between content and files, and how Git keeps the
information that allows tools (like `git blame`) to *figure out* that content
was moved from one file to another. This, as opposed to keeping some
representation of the "move" operation between files in the repository. Linus
had some confidence that this design choice was appropriate:

> In other words, I'm right. I'm always right, but sometimes I'm more right
than other times. And dammit, when I say "files don't matter", I'm really
really Right(tm).

So, pragmatically, what do you do?

1. Split the file apart without any special efforts.
2. Commit the changes all together in a single commit.
3. Use the `-C` flag when running `git blame`.

The `-C` flag, according to the
[documentation](https://git-scm.com/docs/git-blame), detects moved or copied
lines within a file, and detects lines moved or copied from other files that
were modified in the same commit. That is exactly what I was looking for.

Except... I don't usually run `git blame` in the terminal -- my editor does
it. Fortunately, in the GitLens extension for Visual Studio Code, there is an
option you can use to supply `-C` when running blame. Add this to
settings.json:

```
"gitlens.advanced.blame.customArguments": ["-C"]
```

So now that I can split those monstrous files apart, how big or small should
the resulting files be? My rule of thumb: Small enough that it wouldn't be
unreasonable to read the entire file if I needed to make a change to it.

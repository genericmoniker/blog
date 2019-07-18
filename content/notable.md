Title: Notable for Note Taking
Date: 2019-07-13 11:53
Author: Eric
Category: Project
Slug: notable
Status: published

I recently started using [Notable](https://github.com/notable/notable) for my
software development notes. It is an [Electron](https://electronjs.org/) app
that lets you write your notes as Markdown. It is a little light on features
currently, but that can be a good thing.

## OneNote

![OneNote Screenshot]({static}/images/notable-onenote.png)

I've used Microsoft OneNote [for a long time](evernote-vs-onenote.md). There
are a lot of things I like about it, though I've sometimes wished for more
programmer-centric features, like code syntax highlighting and structure that
is more semantic rather than just formatting.

I had a work-specific notebook that synchronized with my work Microsoft
account, and a more general programming notebook that synchronized with my
personal Microsoft account. A few months ago, this synchronization split
stopped working, and after hours of trying to get it to work again, I gave up.

Finally, if you want to use OneNote on Linux, you'll need to use the web
version, and search is fairly worthless there because it isn't currently 
possible to search an entire notebook.

With these issues, it seemed like a good time to survey the current note taking landscape.

## Boostnote

![Boostnote Screenshot]({static}/images/notable-boostnote.png)

I first came across [Boostnote](https://boostnote.io/). It is pretty cool and
has a wide variety of features like:

* Syntax highlighting
* Editor themes
* The ability to add images to a note through the clipboard
* Versatile tagging

There are tons of people contributing to the project, which although could be
good, gives me more a sense of chaos after using the application for a while.
Releases seem to break major functionality as often as not. For example,
recently the auto-updater broke, and the display of images within notes stopped
working. Those seem like things that you'd hopefully notice before pushing an
update. 

Also, while there used to be an Android app, I believe its development was
halted in order to do a more maintainable version at some point. Since the
notes aren't stored natively as Markdown, you also can't as easily use some
kind of Android-based text editor.

With so many people interested in Boostnote, things could quickly change for
the better, but I decided to look some more, and found Notable.

## Notable

![Notable Screenshot]({static}/images/notable-notable.png)

Although Boostnote and Notable are similar, Notable is a bit simpler. The UI
feels a little more natural to me, and notes are stored on disk as Markdown.
Although there are features that I'd love to see, it seems to have a steadier
foundation, and a little firmer direction as the result of having a primary
maintainer.

There is a
[chart](https://raw.githubusercontent.com/notable/notable/master/resources/comparison/table.png)
comparing Notable to many other note taking apps. It can't help but be a little
biased, but it can give a sense of what is considered important.

Features I'd *really* like are:

* [Add attachments via copy/paste](https://github.com/notable/notable/issues/26)
* Screen "Snipping" functionality like OneNote
* [Highlight text matching search query](https://github.com/notable/notable/issues/243)
* Improved searching -- such as being able to search for an exact string.

So far it is working out well, and the nice thing about open formats like
Markdown is that it is pretty easy to convert to something else if needed.

Speaking of which, I've got a couple of projects on GitHub:

* [boostnote-dump](https://github.com/genericmoniker/boostnote-dump) - A fairly
 simple utility to convert notes from Boostnote format to Notable.
* [onenote-dump](https://github.com/genericmoniker/onenote-dump) - A
  considerably more involved utility to convert OneNote notes to Notable.

Neither are extensively tested at this point, but they got the job done for me.

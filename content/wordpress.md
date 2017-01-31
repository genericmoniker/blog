Title: WordPress
Date: 2007-04-28 12:06
Author: Eric
Category: Uncategorized
Slug: wordpress
Status: published

After years of building this site with my own custom software, I've
decided to switch to [WordPress](http://wordpress.org "WordPress").

<!--more-->

My previous system started with XHTML content transformed through
various XSLT style sheets thatproduced summaries, an RSS feed, a Google
sitemap, and a common appearance across all the pages. The whole process
was driven by an Ant script, and required no server-side code except for
a comments form. It worked pretty well except for a few things:

-   Running the scripts (which included FTP to the server) to publish a
    new article took a while, so it wasn't something you could just
    quickly do.
-   The scripts were only available on one machine, so publishing could
    only happen from there.
-   When my comments form was turned on, it got a bunch of comment spam.
-   If I wanted any new features, I had to do them all myself.

I thought I'd take a look at some actual blogging software to see what
was available. I ran across an extensive comparison (though I can't
remember where that was now) where the person doing the comparison
decided on using WordPress. I had thought about trying to use a .NET
application, since I'm trying hard to learn .NET deeply right now, but
there was a telling comment about .Text (the only .NET blogging tool
considered) in the comparison. The reviewer said something like, ".NET
programmers are more excited about .NET than actual working software."
While a sweeping generalization, I sense a bit of truth in there. Also,
as a programmer, it is good to be exposed to lots of things, so a PHP
application seemed good for technical diversification.

I created my own WordPress theme, both in order to preserve my site's
look as well as to learn more about WordPress. Then I needed a way to
migrate my content. I don't have a ton of articles, but certainly more
than a manual approach would work for. I tried adding a couple
of articles by hand, and quickly discovered that the WordPress editor
treats all whitespace as significant, unlike HTML's text flowing
regardless of line breaks.

My first attempt at an automatic import was to transform my content to
WordPress' native export/import format. I abandoned that after a little
while because it was based on RSS, but added a bunch of stuff that
wasn't really relevant for my content. I realized that I might as well
just do an RSS import, which was easier.

The significant whitespace characteristics I noticed in the editor
carried over to imports as well, so my conversion program had to strip
out all the non-significant linefeeds out. I also discovered that if
there were XML namespace declarations where the importer didn't expect
them, then it would think that there weren't any posts to import.
It would just say, "All done! Have Fun!", which was kind of infuriating
until I figured it out. I think I've heard someone say that blogging
software is only as good as its import and export functions, and I
almost gave up on WordPress at this point.

Once I got my content imported, I was happier about WordPress when I
discovered Ryan McGeary's [WP-Syntax
Plugin](http://wordpress.org/extend/plugins/wp-syntax/ "WP-Syntax Plugin"). I
had thought about doing something like that myself at some point. I did
make one small tweak to the plugin, though. GeSHi's default syntax
colorings were a bit too much for me, so I switched the GeSHi
option over to use CSS styles for the highlighting, and chose fewer and
more subtle colorings. I'm sure there are lots of other interesting
plugins that I've yet to discover.

There have been some glitches (bug-like behavior), some manual work
required even after my automatic import, and still some things to figure
out, but I'm optimistic that WordPress will work out.

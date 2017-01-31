Title: When Does XHTML Matter?
Date: 2006-07-05 17:00
Author: Eric
Category: Software Development
Slug: when-does-xhtml-matter
Status: published

I noticed the other day that the pages on this site had double `body`
tags in the HTML. As someone who favors standards it was kind of
embarrassing. But what started as a quick fix turned into a few days of
ruminating about how I'm putting this site together.<!--more-->

I use FrontPage 2000 to write my articles. Then I run an
[Ant](http://ant.apache.org/) script that uses the HTML content of the
site to build an RSS feed, a home page with recent articles, the archive
page, a Google site map and finally run the content through an XSLT to
apply the common page elements.

Since FrontPage 2000 doesn't output, or even tolerate XHTML, I use a
custom Ant task, [styler](http://www.langdale.com.au/styler/), that lets
you do XSLT transformations on HTML pages, even when they aren't
actually XML. My poorly formed result pages were the result of an XPath
goof of selecting `html/body` when I should have done `html/body/*`.

But I started to take a look at the community technology preview of
Microsoft's new [Expression Web
Designer](http://www.microsoft.com/products/expression/en/web_designer/default.mspx),
which is one of the successors of FrontPage. It supports XHTML, which
might make me finally upgrade when it comes out. I wondered if I could
replace a bunch of the stuff in my Ant script by just using Web Designer
features.

The first interesting thing was Dynamic Web Templates, which are
actually a FrontPage 2003 feature. They provide essentially the same
functionality as my XSLT transformation -- centralizing all the common
page elements into a single place. There were a couple of things that
bothered me about the feature, though. First, every time you save the
template page, it asks if you want to update all the pages that use it.
I guess the idea is that you won't edit your template much once you get
it right, but for habitually frequent savers like myself, it was a
little annoying. Second, when doing real writing of content, Web
Designer shows a dimmed template and provides you an editable area where
the content ends up. Maybe I'm just quirky, but I'd rather compose
articles in a pretty minimal layout. I don't really need my site banner
and search side bar -- just give me a nice plain HTML editing surface,
please, with a simple CSS for fonts. In fact, that's really how I'd
prefer my articles to be anyway -- nice simple XHTML instead of being
filled with automatically replicated layout tables and
presentation-oriented `div` tags.

Next I decided to take a look at ASP.NET 2.0. I'm pretty ignorant of all
versions of ASP, to be honest. But I worked on a web application before
ASP 1.0 ever came out, building something that maybe would have been
kind of like SharePoint had NextPage had a hundred times the resources
that we did. We had to build our own presentation framework, and it
suffered from neglect even when we started to learn some things about
how to build web applications but had more pressing requirements.

In my foray into ASP.NET, I learned about master pages, which
functionally overlap with Dynamic Web Templates but are in fact dynamic,
whereas Dynamic Web Templates are, from a typical programmer point of
view, static.

A master page has placeholders for content, like this:

```html
... <body> <asp:contentplaceholder id="Body" runat="server"/> </body> ...
```

When creating the content to go in that placeholder, I initially thought
I'd be able to create a nice XHTML page, sullied only slightly by some
extra ASP tags to match up with the placeholders in the master document.
That's not the case. The content page can *only* have the blocks of ASP
tags:

```
 
  

OK, here is my body text. 
```

If you have more than one placeholder in the master, you have the same
number of top-level `asp:Content` tags in the content page. So what is
this strange thing that I'm supposed to store my content in? It's not
HTML -- you're not even allowed to have an `<html>` tag in the page.
It's certainly not XML because there's no root element if there are
multiple content blocks. So how are you supposed to author your content?

Of course you can author in plain text, writing markup by hand, but that
seems kind of primitive. You can use Visual Studio, but that doesn't
give you spell checking or a UI geared toward English composition.
Finally there's Web Designer, but the rendering is messed up (but it's
only a CTP after all) and it has the same "edit in full context" UI as
Dynamic Web Templates. And what do you end up with when you're done
authoring? Some non-standard text file.

People tend to agree that XHTML to the browser is a good thing, but
isn't it a good thing for authoring, too? A variety of authoring tools
exist, and it's so much easier to manipulate source material in XHTML.
But master pages seem only concerned with good markup for the browser
delivery portion of a document's lifecycle.

I'd like to learn ASP.NET better at some point -- I'm sure it's
excellent for lots of things, but the master page system doesn't feel
right to me. My XSLT approach feels better -- clean source documents
combined with a "master page" that pulls in the appropriate content. The
content pages don't have any special markup saying "this section will go
into some other page at location X", they just have *markup*.

So I decided to stick with my current system, fixing the `body` problem
and taking advantage of Web Designer and [HTML
Tidy](http://tidy.sourceforge.net/) to have XHTML sources and XHTML
delivery. I'm content with it... for now, anyway.

Title: Cipher Suite for webOS
Date: 2010-09-30 22:26
Author: Eric
Category: Project
Slug: cipher-suite-for-webos
Status: published

My son turns 14 this month, but we still have bedtime stories.
Currently, the bedtime story is Simon Singh's *[The Code
Book](http://www.amazon.com/gp/product/0385495323?ie=UTF8&tag=esmithy.net.sparks-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0385495323)*.
While reading the description of the Vigenére cipher, I
started to think about how I'd code up an implementation, and that led
to my first webOS application. Cipher Suite is a small collection of
classic ciphers, and is currently in the Palm [beta
feed](http://www.precentral.net/app-gallery/beta/cipher-suite).
Hopefully a few people will give it a try and let me know if it sets
their phone on fire or drowns some kittens or anything. Having gotten it
that far, I thought I'd share a little bit about how the app was
developed.

### Development Environment

I don't love Eclipse, so I was excited when Palm announced
[Ares](http://ares.palm.com/Ares/about.html). Ares combines most of the
tools you need for webOS development in a simple, browser-based IDE.
Built-in JSLint support is awesome. Viewing logs while an app is running
is simple. The editor and debugger are surprisingly capable. Source
control integration is a great feature.

The visual designer, though possibly the most visible feature of Ares,
wasn't that helpful for me. There's just not enough documentation to
figure out how to accomplish what I want. The developer site has just
barely enough documentation to build an app in the "traditional" Mojo
way, let alone translating from Mojo to the Ares designer. The [Ares
presentation from Developer
Days](http://www.youtube.com/watch?v=cR5_iW71soA) was hugely
disappointing. So I just ended up creating a regular Mojo application
instead, which worked just fine. It would be nice if you could choose up
front which style of app to develop, and have the "New Scene" menu item
either create an HTML scene or an Ares "chrome" scene as appropriate.

### Source Control

Even though Ares keeps your code in the cloud, it's still a good idea to
use source control for change tracking. I looked at a bunch of online
Subversion hosts, and ended up picking [Unfuddle](http://unfuddle.com/).
It's free, which is a big factor for a hobby project, and has worked
reasonably well. It took me a little while to realize that adding a new
project file in Ares does not add it to source control automatically --
you have to do that as a separate step.

### Unit Testing

Another benefit of my Subversion repository was that I could work on my
project outside of Ares and still keep everything organized. The main
thing I found missing in Ares was a built-in way to do unit tests, so I
took care of those on right on my PC. I used the [Jasime JavaScript unit
test framework](http://pivotal.github.com/jasmine), running the tests
from a local "runner" HTML file within Firefox so that I could step
through any failing tests using the Firebug debugger.

### Summary

Learning to develop for webOS definitely took some effort, but now as
I'm going through the same learning process for iOS, I realize that
writing code in JavaScript and building views in HTML provides for a
gentler learning curve than Objective-C and Cocoa. I started my
professional development career as a C programmer, but the merger with
Small Talk makes Objective-C an odd beast.

Cipher Suite is kind of a niche application, but hopefully it will be
fun or useful to a few people. It took a lot of spare-time hours over
several months to put it together, but I wanted to do my small part to
support the great webOS community.

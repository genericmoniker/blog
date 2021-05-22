Title: Office Open XML Deep Dive
Date: 2007-06-28 17:35
Author: Eric
Category: How It Works
Tags: Microsoft Office
Slug: office-open-xml-deep-dive
Status: published

Last week I went to San Francisco to take a dive off the deep end into
the new XML file formats in Microsoft Office 2007. The training was
hosted by MindJet, and presented by [Doug
Mahugh](http://blogs.msdn.com/dmahugh/ "Doug Mahugh") of Microsoft, and
[Chris Predeek](http://predeekc.spaces.live.com/ "Chris Predeek"), a
consultant who put together the code samples for the hands-on labs.

NextPage has been involved in the standardization process for
Open XML, with our very own [Tom
Ngo](http://www.nextpage.com/about/bios/tom.htm "Dr. Ngo")serving on the
Ecma committee. Doug, at a post-training session dinner (thanks
[Erick](http://erickwa.spaces.live.com/ "Erick Watson")!) had only good
things to say about Tom. He said that he wished Tom could be at all the
committee meetings because he's able to reason from neutral ground,
whereas a Microsoft representative saying the same things would
immediately be treated with skepticism and mistrust.

The training focused mainly on document generation independent of Office
applications. This included some general XML programming with .NET and
using the System.IO.Packaging API included in .NET 3.0, which I had
heard of but had never seen used. The packaging API give a little higher
level of abstraction than just working with the raw ZIP and XML. I also
learned that there is [yet another
API](http://openxmldeveloper.org/archive/2007/06/06/1640.aspx)in the
works that is at an even higher level of abstraction. It is currently in
CTP form, and Doug indicated that the developers would *really* like
feedback on it. Chris also showed using XSLT to generate documents from
templates.

Aside from general understanding of our implementation domain, we're not
extremely interested in document generation at NextPage. Our efforts are
more toward tracking documents that others create. There may be
opportunities to store our tracking metadata as a custom XML part,
whereas we currently mash some XML into the structured storage custom
properties for the previous binary format.

Something that made the training experience unique was that it was all
professionally videotaped. I don't just mean that there was a camcorder
running in the back of the room. They had multiple cameras, extensive
lighting, a control room, and lots of other stuff completely lost on me
as a TV production ignoramus.

Doug's [blog has a
photo](http://blogs.msdn.com/dmahugh/archive/2007/06/22/san-francisco-workshop.aspx)
showing all the extra lighting added for the cameras. That's the back of
my balding head in the front row, second from the right. I've always
heard that the best students sit toward the front to the side, so I was
looking for someone up there to copy off of. I'm hoping there isn't much
footage of me nodding off, what with the late-night travel to get there
and the limited personal relevance of some of the material.

The film crew also did interviews with the various attendees of the
training, which I agreed to participate in mostly for the interesting
experience of being formally interviewed on camera. My willingness was
nearly offset by my fear that I would say something incredibly stupid.
I'm fairly sure that I said stuff at least moderately stupid. This is
why I prefer writing a blog instead of doing some sort of podcast.
Hopefully the producer will have a goal of making the attendees appear
insightful and articulate and omit my interview altogether.

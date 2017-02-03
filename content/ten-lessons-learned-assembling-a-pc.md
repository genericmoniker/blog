Title: Ten Lessons Learned Assembling a PC
Date: 2006-01-03 17:00
Author: Eric
Category: How-To
Slug: ten-lessons-learned-assembling-a-pc
Status: published

I spent some of my Christmas vacation upgrading the hardware on my PC.
I've been suspicious that there was something wrong with my old
motherboard, so I decided to get a new one. And when you're getting a
new motherboard, you might as well get a new CPU and new RAM. And since
I was getting a new motherboard, it ought to have PCI-Express, so that
meant a new graphics card as well. I've been through this process a few
times now, so I thought I'd try to collect some of the wisdom I've
acquired by doing it. There are lots of people who are more expert at
system building than myself, but maybe I can save someone from a special
class of boneheaded mistakes: those I've made myself.<!--more-->

#### 1. Put a screw in all the motherboard mounting screw holes.

I actually learned this one several years back. I was doing a similar
motherboard swap and was perplexed to discover that my case didn't have
motherboard screw posts in all the places that the motherboard had screw
holes. *Oh well*, I thought, *I can fit in about six of the nine
holes... that ought to hold it*. It didn't work out so good. When I
turned on the machine, it kept rebooting over and over. After some
baffled frustration I discovered that I could move the case's mounting
posts around so there were exactly the right number in exactly the right
places. After that, the machine was much happier. Probably one of the
out-of-place posts had been causing a short.

#### 2. Make sure the port faceplate has all the metal tabs arranged so they don't block the ports.

I've made this mistake a couple of times. The metal face-plate that goes
over all the motherboard ports (PS/2 connectors, network, speaker jacks,
parallel port, etc.) frequently has metal tabs that, if you're not
careful to bend them inwards when installing the motherboard, will
actually cover some of the ports. Or worse, leave a little piece of
metal sticking *inside* the port. Sometimes it is hard to notice that
this has happened until you've got your machine all put together and are
just hooking up the cables. When you discover this problem, you might
want to go out for some fresh air for a bit, because you're going to
have to undo a lot of work to get the motherboard back out enough to
bend the tabs in.

#### 3. Neatness counts with power cables.

While my [CoolerMaster Wave
Master](http://www.coolermaster-usa.com/CoolerMaster/Products.aspx?pid=36)
case is beautiful and sleek, I'm not the kind of guy who puts a window
in the side of his computer. So when I originally built my current box,
I didn't worry too much about power cable placement. I strung wires
everywhere, threw on whatever extra connectors seemed convenient, and
crammed the whole tangle behind a shiny black side panel. Not long ago,
I had a problem where my system would periodically lock up (accompanied
by a nice little squeak from the PC speaker). Then the hard drives would
hiccup. Eventually I ended up with a BSoD. I opened the case, and after
some rearranging some of the power cables (mostly an act of
desperation), the problem disappeared. I'm thinking this was probably
another motherboard short -- this time by a stray power plug.

While installing my new motherboard, I did things much more carefully
and discovered that there were a handful of extra power cables that I
could just disconnect and pull out, which helped the rat's nest
considerably.

#### 4. Hook up *all* the case fans.

On my first build in this case, I had some fairly severe heat problems.
Playing games in the winter months was kind of nice -- no need for a
space heater! After some spelunking with a flashlight, I discovered two
fans in the front of the case that weren't hooked up. I hadn't even
realized that they were there. After hooking them up, I could keep the
side panel on without overheating!

#### 5. Prefer the motherboard fan power connectors over the power supply's connectors.

The motherboard is generally smarter than the power supply, and it can
regulate fan speeds based on the current temperature. That means your
machine sounds less like a 747 taking off when you turn it on. I think
my power supply actually purports to be able to adjust fan speeds as
well, but I relieved it of such duties for poor performance. Maybe it is
just too far removed from the main cooling action to be effective.

#### 6. A 20 pin power supply connector works just fine in a 24 pin motherboard socket.

I had my machine all assembled and was ready to attach power to the
motherboard as one of the final steps when, *WTF?!My power supply cable
is the wrong size for this motherboard!* After some Googling I
discovered that there is a new power supply standard that has 24 pin
motherboard connectors, so naturally my new motherboard had such a
connector. Google also revealed some sites selling adapter cables to
convert from 20 pin to 24. I was ready to adapt some Howard Jones: *You
can have shiny new hardware but you just can't plug it in*.

The day after this disappointment, I set about trying to find someplace
local that might have an adapter cable. I discovered that a fair number
of local businesses indicating that they sell computer hardware have not
been able to pay their phone bills. I hesitantly called Totally Awesome
Computers. Hesitantly because their owner, based on his TV spots, is an
energetic individual most likely from some other dimension. But
fortunately the owner doesn't answer the phones, and the guy I talked to
understood my plight immediately. He said that if memory served, I could
just plug in my 20 pin connector to the first 20 pins on the
motherboard, and given that I connected the motherboard's other 4 pin
supplemental power supply (which I had already done), I should be good
to go. It makes a certain amount of sense. After all, 20 + 4 = 24 and
everything. So I gave it a try and the system powered up just fine (and
continues to work normally). Thanks
[guys](http://www.totallyawesomecomputers.com/)!

#### 7. Most modern video cards need extra power.

My new video card is a PCI-Express GeForce 6800 MS from EVGA. When I
opened the box, I had a vague impression that the package had been
assembled somewhat hastily. For example, the driver CD was not inside
the sleeve -- they were just both loose inside the box. There was also a
conspicuous lack of printed documentation. The CD had a manual of sorts,
but it was rather vague about certain things. It said something like
this: "If your video adapter requires a supplemental power supply
connection, we strongly suggest that you connect it." Hmm... Why don't
*you* tell *me* if my video adapter needs extra power?

Being new to PCI-Express, I wondered if they had boosted the power
capabilities of the bus such that supplemental power connectors would be
a thing of the past. But there was a six pin connector on the edge of
the board that looked suspiciously like a power connection, so I wasn't
sure how to proceed. My previous video card had taken a fan power
connector, but I didn't have anything hanging off my power supply with
that six pin configuration.

After some time formulating queries on EVGA's forum, I found a posting
where someone had received a similarly packaged product, and so learned
that there was supposed to be a six pin power adapter in the box. A
company representative had posted a message that anyone missing their
adapter should give support a call and they'd expedite it out.
"Expedite" somehow connotes to me something faster than "UPS Ground",
but I'm still waiting. Fortunately the card works without the
supplemental power -- just in a hobbled mode. So while I can write this
article, I don't expect to attempt Battlefield 2 until my part
arrives. 

#### 8. Have access to a working computer with an internet connection.

Fortunately I have a computer for my kids in my office. Otherwise it
would be tricky to do things like check EVGA's web site, read PDF
manuals and create RAID driver floppy disks. Of course, it also makes
backing up data easier if the spare machine has a decent amount of hard
drive space.

#### 9. Arrange your data for transferability.

For a long time I've had a `C:\Data` directory on my systems for
everything that I couldn't reacquire through an install or a download.
This is all the precious, irreplaceable, I-actually-back-this-stuff-up
data. When Windows started having "My Documents", I fought it for a
while and with Windows XP, it got a little worse and better. First worse
because the user profile directory in `C:\Documents and Settings`, which
held "My Documents" also had mountains of crap -- er, non-critical
settings and cached data -- in it. I just didn't feel *clean* keeping my
data down there. But the shell is determined to have you put stuff in
there since it is the default file location when it doesn't know where
else to put you. The good new is that you can move "My Documents" by
right-clicking the Start Menu's shortcut to it, and choosing properties.
Now "My Documents" is in `C:\Data\Eric's Documents`, and I feel clean
again.

I also change my email store and address book locations to be in my data
directory. I haven't figured out how to move my Internet Explorer
favorites, but I put a shortcut to them in my data directory to remind
me to copy them. I did that reminder strategy with my Fonts directory as
well, since I have nice fonts that were installed with some otherwise
worthless applications, and I'd rather not have to reinstall them to get
the fonts again.

It's also a good idea to back up any DRM licenses you might have for
music and such. I'm morally opposed to DRM for music, but I do have a
few songs blighted by it. After copying my music to the backup computer
and back, none of those songs would play. I figured that it was just
another way that DRM was screwed up and that I had lost those songs. But
I ran Windows Media Player's license restore and they played again. Of
course I had to have backed them up previously for this to work...

All this makes is much easier to reformat your hard drive without losing
irreplaceable data.

#### 10. Resetting the icon cache can be a handy trick.

After getting the clean OS installed, I logged into my wife's account.
Mysteriously, the Internet Explorer and Outlook Express icons on the
start menu didn't show up correctly. It just had some generic icons.
Normally shortcut icons are easy to fix -- you just go to the properties
and change the icon. But those two shortcuts are magic ones, and there
isn't a way to get the shortcut properties in order to change the icon.
I tried changing the applications to the MSN versions, and those icons
worked fine, but switching back to IE and OE still gave me generic
icons. I finally managed to fix them by invalidating the icon cache by
changing the system setting for the icon size and then changing it back
to the original size. You find that setting in "Display Properties &gt;
Appearance &gt; Advanced" as one of the things in the "Item" drop-down.

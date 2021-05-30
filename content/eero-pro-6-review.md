Title: eero Pro 6 First Impressions
Date: 2021-05-29 18:23
Author: Eric
Category: Review
Tags: Hardware
Slug: eero-pro-6-review
Status: published

I set up an eero Pro 6 mesh network in my house this past week. These are my
first impressions of the system.

## Why

Earlier this year, my employer decided that the pandemic-motivated "work from
home" policy would continue indefinitely for the engineering department. After
moving a few PCs from the office to my house, I started thinking about
isolating the work machines from the rest of my network. I figured I'd have a
router just for them, using my aging Asus RT-AC66U for that and getting a
newer router as the gateway for my whole home network.

## Shopping

My first thought was to get another Asus, since the current one did a fine job,
and the RT-AX86U is a well-reviewed candidate. Unfortunately it was sold out
everywhere unless you were willing to pay a $100 premium over MSRP. B&H Photo
at least let me back-order one, so I did that and waited, and waited, and a
month or so later decided to cancel the order when there was no indication of
when it might be fulfilled.

Doing some more research, I read an article about mesh wireless routers. I'd
had the impression that some of those were dumbed-down "consumer-y" products,
and I was more wanting something in a "pro-sumer" category. The article said
good things about routers from eero, a subsidiary of Amazon, so I did some
research to see if those could do the things that I wanted:

* IP reservations? check
* Parental controls? check
* Guest network? check
* Custom DNS? check, with some caveats

I quickly gravitated to the eero Pro 6 which has 3 access points supporting (up
to) gigabit wireless connections. It is recommended for coverage of 6000 square
feet, which is overkill for my house, but the fact that each access point has
ethernet ports opened up interesting possibilities.

I have a "home" office and a "work" office in the house, which makes it easier
to keep a clear distinction between being "at work" or not. I've always had my
cable modem and router in my home office since that's where most of the
high-bandwidth equipment has been, but I've *occasionally* suffered from poor
internet connections. The Comcast tech that checked things out when my
connection was especially spotty speculated that I had a crappy coax splitter
in the house, because the signal was dirty in the office, but clean in other
areas of the house. Unfortunately that splitter would be in a wall somewhere,
and I would probably need to hire an electrician to find and fix it.

With three access points from the Pro 6, I could move the modem to a clean area
of the house, then use the ethernet ports to plug in a switch in the home
office, and the old router in the work office. Clean internet, and fast wired
connections between all the machines in each office. Sounds great!

Except that the eero Pro 6 was sold out too! Good grief. Amazon let me
back-order it, and it actually showed up in just under two weeks. That seems
long when spoiled with Amazon Prime, but acceptable for something that wasn't
in stock. They also did a decent job of keeping me apprised when I'd get it and
then [beat their own
estimate](https://www.popsci.com/story/science/head-trip-disney-wait-lines/).

## Setup

![eero Router]({static}/images/eero-router.jpg)

Unlike all the previous routers I've owned, eero devices don't have a web
interface at the gateway address. Instead you need to use their mobile app to
set it up and administer it. I was a bit worried about that at first, but it
has turned out OK so far. I did the initial setup with my phone because
something I'd read in the shopping phase suggested that you needed an internet
connection for the initial setup. There's something perverse about that (but I
didn't actually verify that it was true). I've since installed the app on my
tablet, because big screens are right and good.

One of the very first setup questions the app asked was "What do you want to
call your network?" Hmm... Is it asking me what I want the wireless SSID to
be? I've usually had separate ones for different bands (like a "_5" suffix for
5 GHz). How do I answer this question!?!? Whatever, I figured I'd be able to
change it later if needed, so I put in an "unadorned" name. It turns out that
the router can serve all its bands with a single SSID, so having different ones
is unnecessary. Huh. That's kind of nice. There's even a setting called "Band
steering" which is described as "Improves performance by encouraging capable
devices to connect to 5 GHz." Yes, please.

The overall setup process went smoothly. Basically plug in an access point and
let the app discover it. It did automatically start a trial of the Secure+
service, which I'm not really interested in paying for since I get the features
I'm interested in with my [Pi-Hole DNS server](https://pi-hole.net/). I did
have to disable the "Advanced Security" features (in the "Discover" section of
the app) before I could set a custom DNS server, since some those features are
implemented via DNS.

## The App

The main screen of the app gives a view of the your internet connection (with a
built-in speed test), access points, and the devices connected to your network,
as well as devices *recently* connected to your network but not currently. That
last category is nice because it gives you a more complete view of everything,
even if, say a smart TV doesn't happen to be turned on right now.

You can give devices "nicknames" to more clearly identify them, as well as
indicate what type of device they are (such as Laptop, Network Equipment, Game
Console, Security Camera, Light Bulb and many others), which will assign them
an appropriate icon and group them into categories. The result, frankly, is
beautiful.

![eero app Home]({static}/images/eero-home.jpg)

My Asus router had a way of naming devices, and some icons for different kinds,
but it feels clunky in comparison. People had even created entire [custom icon
sets](https://www.snbforums.com/threads/additional-device-icons.33102/) to try
to get a nicer-looking client list on the Asus.

I was a bit stumped on giving devices nicknames at first. There's clearly an
edit field, but there was no "Save" button, and just leaving the screen didn't
automatically save. I even went to the [support web
site](https://support.eero.com/hc/en-us/articles/211096103-How-do-I-identify-the-devices-on-my-network-and-assign-nicknames-),
which said:

> Type in the Nickname you would like to assign the device then tap Save on the
> top right corner

Gah! There is no Save button. Is this a bug? There *had* been a Save button in
other parts of the app. I sent an email to support, and they responded the next
day saying, "After you tap the name field and type in your nickname simply tap
the enter/done key that's on your keyboard on your phone." OK, that works, and
also let me know that support requests get handled in a timely way (at least
the easy ones).

Another thing I like is the Activity screen, which shows data usage per device
or per profile (a group of devices associated with a person). This is
fantastic.

![eero app Activity]({static}/images/eero-activity.jpg)

A couple of months ago, I got a data cap warning from Comcast -- I had nearly
used all of my allotted bandwidth for the month. I looked at the historical
monthly usage graphs on the Xfinity site, and could see that usage was up
significantly that month, but I had no idea why. How can I tell what was eating
my bandwidth? From my research, unless your router keeps track, you don't have
much chance of figuring it out, and the Asus router did not.

## The Actual Wi-Fi

I haven't done a lot of detailed testing, but I can say that there isn't
anywhere in my house that doesn't have full Wi-Fi bars. I can even walk down
the road 150 feet from the edge of my property and still have a signal. It
makes me hope that allegations Wi-Fi is bad for your health are unfounded,
because I am fully awash, but otherwise I'm pretty happy.

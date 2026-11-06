Title: Lessons from UTF-8
Date: 2026-11-05 19:34
Author: Eric
Category: How-It-Works
Slug: standards-utf-8
Status: published

[![XKCD Standards]({static}/images/xkcd-standards.png)](https://xkcd.com/927/)

The famous XKCD comic includes "character encodings" in its list of
proliferating standards, and it is no joke. There are dozens, just counting the
ones in common use. But the UTF-8 encoding seems unique in that it didn't just
add one more, but is managing to legitimately become that one standard everyone
hoped would do away with the mess. The [UTF-8 Everywhere
Manifesto](https://utf8everywhere.org) is pretty persuasive about why it should
be the one-and-only standard.

I don't know a ton about the history of character encoding design, but I'll not
let my ignorance prevent me from making my point. It seems that someone (Joe
Becker and friends) looked at ASCII and thought, "This doesn't work! Let's make
a fresh start and design something that does." Mistakes were made, and it didn't
go as smoothly as hoped for a while. Notably, the first Unicode encodings
weren't exactly compatible with ASCII. They kind of *looked* like ASCII it if
you ignored all of the `00` bytes in there. But why bother being compatible
anyway? We're inventing the way forward here!

I've always thought that UTF-8's compatibility with ASCII was brilliant and
elegant: Any 7-bit ASCII is valid UTF-8. Other people feel like it is an ugly
hack. What I like about it is that rather than looking at a hugely successful
but fatally flawed design, UTF-8 doesn't throw it away to make something totally
new, it extends it, making the transition to it less painful.

IP addressing seems like it might be following a similar path. IPv4 is wildly
successful but also has a fatal flaw. In this case, that there are too many
network devices that want an address rather than there being too many characters
that want a representation. "This doesn't work! Let's make a fresh start and
design something that does!" So IPv6 was born. Personally, I use IPv4 all the
time, while IPv6 support in products I work on is more of a "Somebody probably
uses this somewhere so we ought to handle it" situation.

I recently became aware of the work-in-progress [IPv8 addressing
proposal](https://www.ietf.org/archive/id/draft-thain-ipv8-00.html) -- is the 8
a coincidence? Surely.

This jumped out at me from the spec:

> IPv4 is a proper subset of IPv8. An IPv8 address with the routing prefix field
> set to zero is an IPv4 address. No existing device, application, or network
> requires modification. The suite is 100% backward compatible. There is no flag
> day and no forced migration at any layer. IPv8 also resolves IPv4 address
> exhaustion.

In other words, it takes the successful standard and extends is to remove its
fatal flaw it rather than throwing it away and starting over. Maybe that's the
key to consolidating standards rather than proliferating standards.

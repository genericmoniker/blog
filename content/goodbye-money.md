Title: Goodbye Money
Date: 2008-11-08 12:51
Author: Eric
Category: Review
Slug: goodbye-money
Status: published

The current stock market makes the title generally appropriate, but I'm
specifically talking about Microsoft Money here. I used to use Quicken
pretty heavily, but I got tired of forced upgrades so I've been using
Microsoft Money for a little while. Now I'm happy to be done with both
of them.

The thing that appealed to me about Microsoft Money Plus is the
"Essential" user interfaces. They're simple, clean ways of doing basic
personal finance geared toward people who get their transactions
electronically and aren't accounting hobbyists.

Unfortunately, the Essential features are on or off -- there's no way to
just dip a toe into "advanced" features. If you venture into such
financial rocket-science as splitting a transaction across categories or
adding a memo to a transaction, you have to surrender the streamlined UI
and switch completely to the Advanced Register. Some Essential features
are just broken, like credit card payments not counting as expenses in
reports (since the credit card transactions already account for those
expenses). The documentation explains it exactly how it should work, but
apparently someone forgot to tell the developers. So while the Essential
UI showed promise, it was ultimately just disappointing.

After some guilty months of ignoring my finances, I thought, "Heck, I'm
a software engineer. I'll just write my own application." How hard could
it be? With a database and a grid control I'd be halfway there. Of
course, there's the critical part about downloading transactions...
There's probably some standard protocols for that somewhere. Then I
noticed line at the bottom of the account register in Money:

> Account information provided by Yodlee, Inc. or your financial
> institution's online services.

What's Yodlee?

A quick Google search led me Yodlee and Mint.com, both online
applications for personal finance. The consensus seemed to be:

-   Yodlee: More powerful
-   Mint.com: Built on Yodlee services, better UI

I went straight for [Mint.com](http://mint.com).

These are the things that I've come to like about Mint.com:

-   It does have a pretty nice, AJAX UI.
-   I was able to connect it to all my financial institutions, including
    things like PayPal, my mortgage and 529 savings accounts, which I
    could never figure out with MS Money.
-   Since the application is running on a server, it knows what's going
    on without me having to download transactions (or even boot my home
    machine), and can send me alerts about potentially interesting
    things like large transactions, budget overruns, etc.
-   It sends a nice financial summary each week to both me and my wife.
-   It's free.

What about concerns?

Security is a pretty important consideration, but they seem to have done
a reasonable job being at least as secure as your bank.

Their business model is around making sponsored recommendations based on
your financial situation. For example, if you've got a high-interest
credit card, they'll recommend a lower interest alternative. Hopefully
that model is sustainable.

There are still some bugs in the system. One of my accounts won't update
(I've got an open ticket on that one), and my budget disappeared for a
little while.

Despite these, I'm cautiously optimistic that I've found a superior
alternative to Quicken and Money.

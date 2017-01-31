Title: Matches and Bulk Actions
Date: 2006-05-26 17:00
Author: Eric
Tags: User Interface
Slug: matches-and-bulk-actions
Status: published

I noticed again this morning that Quicken was still unable to download
my credit card transactions online. It hasn't worked since some time in
February. The error message said that my PIN or Customer ID was wrong. I
know I've double-checked the PIN previously, so I figured it must be the
user name that was the problem. This led me to think about a few ways
that the Quicken user interface is deficient.<!--more-->

First a general gripe, though. Does it seem unprofessional to anyone
else to have software that you paid for constantly try to up-sell you on
every imaginable financial service that Intuit has to offer? And in that
vein, I should also add the disclaimer that I've resisted the up-sell
sufficiently that this is Quicken 2004 Deluxe that I'm talking about.

#### How do I change my customer ID?

After looking around through the PIN vault, the account information
screen and the online help, I couldn't find any way to change the
"customer ID" originally provided in the online account setup. So I just
deactivated online access and set it up again, which worked just fine
except...

#### Why can't you download only the transactions I don't have?

Resetting the online access also caused Quicken to forget which
transactions it had already downloaded, so it got an entire year's
worth. Well, OK, bandwidth is cheap, and Quicken should at least be able
to match all the transactions it had downloaded previously, right?

#### How is this not a match?

The requirements for a downloaded transaction to be a match for a
transaction in the register are beyond me. I've got two transactions
with the exact same date, payee and amount. Even the case of the payee
matches because, after all, both transactions were downloaded from the
same place. They are **the same**. But still, out of 9 months of
transactions I already downloaded, there's not a single match in the
lot. Everything is "new".

I had figured out previously that Quicken only checks "memorized"
transactions for matches, which is kind of an interesting thing. Why
doesn't it "memorize" everything that made its way into my register? A
full index of everything doesn't seem like a lot to ask. I can spare the
disk space. In any case, at some point I actually bothered to go through
and suggest, one by one, that Quicken remember the transactions that
were already in my register, in a vain hope that it might successfully
execute a string compare.

Oh, well, I've got something like 200 duplicate transactions in the
download list. I'll just multiple select those, hit Delete and... wait a
minute.

#### I have to delete each transaction individually?

There is no multiple select in the downloaded transactions list. You can
accept all the transactions, or you can give each the special individual
attention it obviously craves. It takes three clicks to delete a
transaction from the list. First, you click the "Edit" button, which
pops up a menu. I note ruefully that "Unmatch" is one of the items on
the menu, which I'm sure was really easy for the programmer to
implement:

    EnableMenuItem(unmatchMenuItem, false);

"Delete" is another menu item, which is click \#2. Then of course comes
the confirmation dialog. I was pleased to note that "Yes" is the default
button in the message box, so that last click can actually be hitting
Enter instead. Click, click, Enter. Click, click, Enter. Click, click,
Enter. OK, I can't do this another 197 times.

Hmm, what if I just click "Accept All". Maybe deleting the duplicates of
out the register is fewer clicks. Of course, then I would have to select
every other transaction, which might offset any efficiency gain. Maybe I
could write an [AutoIt](http://www.autoitscript.com/autoit3/) script to
do this...Â  But that's kind of tricky when there's no keyboard
interface in the window for doing deletes. Oh, well. It's a hack, so
relying on exact mouse click coordinates is OK.

```autoit
WinActivate("Quicken 2004 Deluxe") 
For $i = 1 to 20 
  MouseClick("left", 900, 808) 
  MouseClick("right", 900, 808) 
  MouseClick("left", 910, 860) 
  Send("{ENTER}") 
Next
```

That let me whack them in 20 transaction chunks (I didn't want to bother
counting exactly how many to delete). Not a long script, but what do
"normal" people do? I guess maybe their carpal tunnel syndrome isn't as
advanced as mine. Click, click, Enter. Click, click, Enter.

I'm not sure if Intuit has added any actual features to Quicken over the
past few years. It seems like they mostly just redesign the UI, which
maybe explains why it hasn't matured into something highly usable.

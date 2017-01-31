Title: Password Management
Date: 2015-01-10 14:23
Author: Eric
Category: Misc
Tags: Security
Slug: password-management
Status: published

It's been two years since Wired's Mat Honan [declared the age of
passwords
over](http://www.wired.com/2012/11/ff-mat-honan-password-hacker/), but
somehow the successor hasn't yet found its way to the throne. That being
the case, this is how I currently manage my passwords.

The challenge with security is that it tends to be in direct opposition
to convenience, but a password manager helps with the compromise.

I use the free and open-source [KeePass
Professional](http://keepass.info/) as my password manager on Windows,
and the compatible [KeePass2Android
app](https://play.google.com/store/apps/details?id=keepass2android.keepass2android)
on my Android devices.

Despite having a slightly naughty sounding name, KeePass gives me a a
place to store all of my passwords, encrypted with a single master
password. I only have to memorize the master password, and can use
strong, random passwords for everything else.

![keepass]({filename}/images/keepass.png)

There are a few tricks of using it that tip the never-ending conflict of
security vs. convenience toward the convenience side.

Automatic Password Generation
-----------------------------

KeePass generates random passwords for you (if you want). People aren't
very good at coming up with their own strong passwords, so just let the
tool do it for you when you're creating an account somewhere.

Double-Clicking Columns
-----------------------

When you add an account entry, you have columns like those in the screen
shot above, for User Name, Password and URL. If you double-click the
URL, it will take you to that URL in your browser. If you double-click
the User Name or Password, it will copy those temporarily to your
clipboard so that you can paste them into login fields.

Auto-Type
---------

Even better than copy-and-paste, when your database is unlocked and just
sitting in the background on your computer, you can use Auto-Type to
automatically log in to a form sitting in your browser window. By
default, the key combination is Ctrl+Alt+A. You go to the page with the
login form, press the key combination, and KeePass will look for an
entry in its database matching the site, and automatically type your
user name and password.

This can be customized in KeePass for each account to both increase the
chances of it figuring out the right account to use as well as the right
keystrokes to move between input fields (usually just 'TAB') and submit
the form.

Synchronization
---------------

The desktop version of KeePass doesn't do synchronization, but you can
just save your database in a DropBox folder to synchronize it to other
devices. KeePass2Android has native support for DropBox, so it will
synchronize without any extra apps.

But wait, do you trust DropBox with your password safe?

There are two things that help make this an acceptable risk:

1.  DropBox doesn't have your master password, so all the data is
    encrypted and unreadable on their servers.
2.  KeePass also supports two-factor authentication for its databases.

Two-Factor Authentication
-------------------------

Beyond having a master password, you can also require that another file
be present in order to unlock your database. This is an option that you
select when you create your database (highlighted area):

![keepass]({filename}/images/keepass2.png)

If you
choose "Create...", it will save an XML document with some random data
in it to your hard drive:

```xml
<?xml version="1.0" encoding="utf-8"?>
<KeyFile>
 <Meta>
 <Version>1.00</Version>
 </Meta>
 <Key>
 <Data>zPVFcvJqZE2SEL42PVZSRDJcJz+hr/+3QMzEzc4aV4g=</Data>
 </Key>
</KeyFile>
```

You'll have to have both your password, and this "key" file to unlock
your database. But **don't** just put that file next to your database
and let it synchronize with DropBox. Instead, use a USB cable and copy
the file directly to your phone or other device. The point is to never
let the key file escape out onto the Internet (by email, DropBox, or
whatever other mechanism might be tempting to get a file from your
computer to a mobile device).

Now the security of your database, if it happens to end up in a bad
guy's hands, is protected by two factors:

1.  Something that only you know (your master password)
2.  Something that only you have (your key file)

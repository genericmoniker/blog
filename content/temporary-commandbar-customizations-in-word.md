Title: Temporary CommandBar Customizations in Word
Date: 2007-09-04 17:00
Author: Eric
Category: How-To
Tags: Office
Slug: temporary-commandbar-customizations-in-word
Status: published

It's common for an Office add-in to put some custom menu items or
toolbar buttons in the UI of the hosting application. The method to call
to do this is
[CommandBars.Add](http://msdn2.microsoft.com/de-de/library/microsoft.office.core.commandbarcontrols.add(VS.80).aspx).
It is also typical that you'd like those customizations to appear so
long as the add-in gets loaded, but not appear if it doesn't. If your
add-in gets uninstalled, for example, you clearly don't want left-over
customizations littering the application. For this reason, the Add
method's final parameter is a boolean that indicates whether a
particular added control should be added temporarily. The documentation
describes the parameter like this:

> Temporary
> :   Optional **Object**. **True** to make the new control temporary.
>     Temporary controls are automatically deleted when the container
>     application is closed. The default value is **False**.
>
This looks perfect. You can add the customizations at startup, and
they'll be gone at shutdown... except that it doesn't work in Word.\
<!--more-->

There is a [support
article](http://support.microsoft.com/default.aspx?scid=kb;en-us;212616)that
acknowledges this, but it is not a *bug* in Word. Instead, as I read the
article, it is functionality not deemed worthy of Word, given its vastly
superior customization capabilities.

By default, Word adds any customizations to the Normal.dot template,
which causes a couple of problems:

1.  Those customizations are persistent, so the goal of having the
    customizations go away is foiled.
2.  You tend to get these confusing prompts where the user is asked
    whether to save changes to Normal.dot, when most users don't have a
    clue what Normal.dot even is.

I've tried a few different approaches to get the temporary functionality
in Word similar to how it is documented (and implemented by other Office
applications like Excel and PowerPoint). One approach is to add all the
customizations at add-in startup, and (since the temporary flag doesn't
do it for you) remove them all again at add-in shutdown. This mostly
works, but you have to be kind of careful. If the application crashed
for some reason, missing the add-in shutdown step, you need to check for
your customizations before adding them again or you'll get duplicates.
Also, Normal.dot needs saving every time the application exits. It's not
a huge problem -- the little progress bar goes pretty fast -- but it is
slightly annoying.

Among several others that I tried, the approach that I finally settled
on takes advantage of the Word application object's CustomizationContext
property, which lets you send CommandBar customizations to a
template other than Normal.dot.

Here are the basic steps:

1.  Embed an empty Word document template (.dot file) as a resource in
    the add-in. Maybe there's a way to create a .dot programmatically
    from scratch, but embedding an already created one is pretty easy.
2.  On start-up, if the template isn't already on disk, extract the
    resource to disk in the user's template directory (which is
    retrievable from the Options object using wdUserTemplatesPath).
3.  Load the template by adding it to the application's
    AddIns collection.
4.  Before doing CommandBar customizations, set the CustomizationContext
    to be this template.
5.  After doing customizations, *set the Saved property of the template
    to true*.

The last step is the key. Since Word thinks that the template isn't
dirty, it doesn't save it, and any customizations it contained will be
automatically discarded when the application exits. If your add-in
doesn't get loaded ever again, the customization template will never be
loaded, and would be empty even if it was.

I've found this approach to be simple; you don't have to check for
existing customizations at startup or remove anything at shutdown. No
templates need to be saved, and I stopped getting random bug reports of
lingering customizations or Normal.dot save prompts.

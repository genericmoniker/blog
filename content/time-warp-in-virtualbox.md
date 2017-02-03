Title: Time Warp in VirtualBox
Date: 2016-03-05 20:26
Author: Eric
Category: How-To
Tags: Virtualization
Slug: time-warp-in-virtualbox
Status: published

Here are a couple of tips for manipulating the clock in Oracle's
VirtualBox.

<!--more-->

Sometimes you need to tweak a virtual machine's clock for some kind of
test or another. With the VirtualBox Guest Additions installed, you'll
have trouble because the service will keep the guest's clock
synchronized with the host's clock. You'll change the guest's clock only
to see it snap right back to the host's date and time. One way to defeat
that is to simply kill the Guest Additions service.

A more persistent way is to set the GetHostTimeDisabled parameter. With
the VM off, you can do this by running this command on the host
(VBoxManage is in the VirtualBox install directory):

    VBoxManage setextradata "VM name" "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled" 1

Another interesting capability of VirtualBox is to speed up or slow down
the guest's clock to some percentage of real time. To do this, you need
to first turn off time synchronization with GetHostTimeDisabled. After
that, again with the VM off, run this command:

    VBoxManage setextradata "VM name" "VBoxInternal/TM/WarpDrivePercentage" 200

The 200 here means 200% of normal, or twice as fast. This could be
interesting for testing processes that naturally take a long time --
such as a series of scheduled events. Of course it doesn't make your CPU
do things twice as fast, the clock just runs faster. If you bring up a
clock widget on the guest, you'll see the seconds tick by at two per
(real) second.

The range of values for WarpDrivePercentage are [2 to
20000](https://www.virtualbox.org/browser/vbox/trunk/src/VBox/VMM/VMMR3/TM.cpp#L554),
but there are practical limits to how high you can go. As just a single
example, consider the mouse double-click. The OS decides between a
double click and two separate clicks by timing the interval between
them. With the clock accelerated, it can get pretty tricky to manage
click's quickly enough.

The
[documentation](https://www.virtualbox.org/manual/ch09.html#warpguest)
warns that other abnormalities in the guest are likely, such as failures
due to shortened timeouts for devices that are still running in the
"real" world.

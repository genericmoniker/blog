Title: Amazon Glacier and CloudBerry Online Backup
Date: 2013-01-07 18:13
Author: Eric
Category: Review
Tags: Applications, Windows
Slug: glacier-cloudberry
Status: published

![checkbox-0]({static}/images/checkbox-0.png) Offsite backup for critical files

This task has been lingering undone on my to-do list for months. I
imagined that I'd figure out some way to use Dropbox, Google Drive, Sky
Drive, or something to keep my data safe in case something catastrophic
happened at the house. All those solutions seem so expensive, though.
When Amazon Web Services announced [Amazon
Glacier](http://aws.amazon.com/glacier/) not long ago, with storage
rates at 1 cent per gigabyte per month, I figured I'd found my storage
location, but it is just an API. Finding [CloudBerry
Backup](http://www.cloudberrylab.com/amazon-s3-microsoft-azure-google-storage-online-backup.aspx)
completed the solution.

<!--more-->

CloudBerry is a client for a plethora of online storage locations,
including S3, Azure, Google Storage, and about a dozen providers I'd
never heard of in addition to Glacier. You're responsible for
establishing an account and paying the bill for the storage, but the
CloudBerry client takes care of getting your stuff there and back.

While Glacier support was enough to catch my interest, I was also happy
to see that I could use it to back up to my NAS. I was dismayed when
switching from Vista Ultimate to Windows 7 Home Premium that I'd lost
the ability to use Windows Backup to backup to a network location, so
I've just been using an external USB drive. It was pretty easy to set up
the network backup using CloudBerry, with plenty of good options to
control what got backed up.

Aside from the missing network support in Windows Backup (for the Home
variety of Windows), there a couple of things that bug me about it:

1.  <span style="line-height: 15px;" data-mce-mark="1">It's not always
    clear what your're backing up. You can pick certain paths, but does
    it include hidden and temporary files? Is there anything that I
    actually want that is being excluded? What if I don't want to
    include some fat file in the backup?</span>
2.  Compounding the first problem is that the backed-up data itself is
    somewhat opaque without the backup client.

CloudBerry gives you a lot of fine-grain control over what gets backed
up (I think I'll survive if my Linux VM isn't backed up, thanks), and
the backed-up data is perfectly navigable when I ssh into my NAS. You
can compress and/or encrypt the data as well if you want.

I used the NAS backup to fine-tune my settings. The first run took all
night for about 122 GB of data. Presumably backups will be incremental
going forward, so much speedier. That will be especially important for
Glacier. Having gotten some settings I liked for the NAS, I created a
configuration for Glacier, and kicked that off. This takes a **long**
time, as in many days, owing to the generally slow upload speeds from
ISPs. CloudBerry provides some bandwidth throttling that can come in
handy during the days-long upload.

For the Glacier configuration, I had to manually copy my settings from
the NAS configuration. It would have been nice to copy a configuration,
but I didn't see a way to do that. Also, when you edit a configuration,
you have to go through the entire wizard. All the values remain as they
were, but you have to fully navigate through the dozen wizard screens
before you can get to the end and commit the change.

I also ran into a bug when trying to enable the storage cost estimation
tool. I got an index out of range exception displayed in a message box,
without any further indication of what was wrong or how to fix it. I've
also seen a couple of NullReferenceExceptions reported from the
application, so there are a few rough edges.

Overall, though, I'm happy to call it good.

![checkbox-1]({static}/images/checkbox-1.png) Offsite backup for critical files

P.S. I paid for my own copy.

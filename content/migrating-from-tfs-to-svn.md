Title: Migrating from TFS to SVN
Date: 2011-02-01 20:14
Author: Eric
Category: How-To
Slug: migrating-from-tfs-to-svn
Status: published

I've just spent the past few days migrating a Team Foundation Server
source repository to Subversion. It took longer and was more difficult
than I expected it to be.

<!--more-->

Of course, the easy way is to just get the latest from the TFS
repository and add all of the files to the new SVN repository, but
change history is valuable and I didn't want to:

1.  lose it
2.  be required to go back to TFS to get it

I found [tfs2svn](http://sourceforge.net/projects/tfs2svn/), a tool
written by Kevin Colyar expressly for the purpose of migrating while
preserving the change history. If you're going to run this on a big,
mature TFS repository, there are a couple of things you should know:

1.  It's going to take a long time.
2.  Stuff is going to go wrong.

This is no disrespect to Kevin -- that the tool is available at all is a
great help. I also have to confess that I hacked the source code a bit,
so there's a possibility that some of what went wrong was my own fault.

### My Scenario

The repository I migrated has about five and a half years of history,
comprised of nearly 21,000 changesets. It also had code from several
projects, and I really only wanted to migrate a subset of the tree. We
already have a Subversion repository with some source in it, so I wanted
to get the TFS source into there.

### Strategy

My plan was to create a local, temporary Subversion repository into
which I could do the conversion. This would let me mess up in various
spectacular ways without risk to the real SVN repository that would be
the code's ultimate home. It also seemed like it would be faster than
running all of the SVN commands across the network to the Subversion
server. Once the migration was done locally, I'd use **svnadmin dump**
to generate a version of the repository that could be imported into the
"real" repository with **svnadmin load**.

I hoped that I'd be able to use tfs2svn to limit the migration to only
the parts of the tree that I wanted, but the tool resisted my attempts
to do so. I was thinking that I'd run it multiple times, changing the
paths to get one relevant top-level  folder at a time. It's not clear
which path to change, though. You've got the TFS repository path (which
would be a must), the SVN repository path and the SVN working copy path.
It turns out that all of those paths are used in different situations by
the tool, and I eventually thought it might be best to just migrate the
whole thing.

It would be tragic to actually include everything in the final SVN
repository, though, given that Subversion doesn't have a permanent
delete feature (that is, "obliterate"). All the stuff I didn't want to
migrate would be forever in the repository. But since I was going to do
a dump anyway, I could run **dumpfilter** to remove the stuff I didn't
want.

The trouble then becomes time. It takes so long to migrate all those TFS
changesets into SVN that I very quickly decided I needed to push the
filtering forward in the process. This is where the hacking began.

I added a "IncludeChange" check into TfsClientProvider's ProcessChange
method:

```csharp
private bool ProcessChange(Changeset changeset, Change change)
      {
          if (IncludeChange(change))
          {
              // Process file change.
              if (change.Item.ItemType == ItemType.File)
                  ProcessFileChange(changeset, change);

              // Process folder change.
              else if (change.Item.ItemType == ItemType.Folder)
                  ProcessFolderChange(changeset, change);

              return true;
          }
          return false;
      }
```

IncludeChange has a bunch of lines that look like this:

```csharp
if (change.Item.ServerItem.StartsWith("$/Projects/Main/Applications", StringComparison.OrdinalIgnoreCase))
    return false;
```

This combination skips any changes that were in areas that I didn't care
about. ProcessChange also now returns a boolean to indicate whether
anything from the changeset needs to be committed in Subversion, saving
additional time by skipping an unneeded operation.

### Problems

One of the really good things about tfs2svn is the Start at Changeset\#
field. When something goes wrong, you can always start back up where you
left off -- even if you have to exit the program. Sometimes tfs2svn will
even offer to fill in the Start at Changeset\# field for you when it's
about to report an error.

These are some of the things that went wrong.

At first I was getting an obscure *Error resolving case of* \[some
path\]. Hard to figure out, but easy to fix: I just needed to take the
trailing backslash off the Working copy folder.

I also ran into a problem when a changeset moved some files from a place
that I was excluding to a place that I wasn't excluding. That didn't
turn out so well since the source files didn't exist, having been
skipped by my IncludeChange method. This was fairly early on, so I just
decided to start over and not exclude the source path. I might have been
able to get a copy of the files and add them to SVN in the appropriate
place and retry, though.

Directory deletes in TFS frequently caused trouble in the conversion.
They would result in an unresolved conflict on the directory and the
commit would fail. In these cases, I just marked the conflict resolved,
committed manually and skipped to the next changeset. You lose some of
the history in these cases by doing that, though.

Directory adds also caused troubles at times. The tool would try to add
a file to a directory that hadn't been created yet. To fix those, I just
created the directory by hand and added it to SVN and retried the
problematic changeset.

There was one situation where some file renames weren't working at all.
The original files didn't exist and the destination files did. I kind of
mangled that changeset, but fortunately I knew that those files were
obsolete and would all be deleted in a later changeset, so I didn't care
much about them anyway. I think this was probably caused by a situation
where part of a changeset had been processed, but then there was an
error. Retrying the changeset meant it tried to redo some moves that
were already done.

Finally, there were some times when the network would timeout, or
Subversion would report that a file or directory was corrupt or
unreadable. In those cases, I just tried again and was always successful
the next time.

With these errors popping up, tfs2svn required a lot of babysitting to
notice the error, make a fix and get it going again. That unfortunately
added to the total time span since it would invariably stop when you
were busy with something else, or when you hoped to make good progress
letting it run overnight.

### Finish

Once the migration was done, **svnadmin dump** was relatively quick and
completely painless. Once I could get some of IT's time (someone with
direct access to the Subversion server), the load also was quick and
easy.

### Update (4 Feb 2011)

I've noticed another problem in the migrated history. Sometimes the
author of a change seems to be incorrect. According to the history, a
developer from another team did some work that would be extremely
unlikely if it were true. I haven't figured this one out yet...

### Update (22 Mar 2011)

A possible explanation for the "The file or directory is corrupted and
unreadable" errors is a [bug in Windows
7](http://social.technet.microsoft.com/Forums/en/w7itprogeneral/thread/df935a52-a0a9-4f67-ac82-bc39e0585148).
The bug fix is included in Windows 7 SP1, which you can get through
Windows Update.

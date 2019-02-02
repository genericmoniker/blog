Title: Techniques for Effective Logging
Date: 2004-11-09 17:00
Author: Eric
Category: How-To
Slug: effective-logging
Status: published

Updated September 8, 2005

Logging is a testing and diagnostic technique that lies somewhere
between automated testing and debugging. It can help you understand what
your application is doing, especially in cases where there is some
non-determinism because of threading, or when running in an environment
where debuggers are not an option (such as on a customer's machine).
This article is an attempt at defining good logging style. There are
lots of things already written about the technical aspects of using a
particular logger, like Log4J, but not so much about how to use logging
effectively.<!--more-->

What to log
-----------

Knowing what to log is kind of difficult. I can think of a couple of
approaches: The first is to log everything you possibly can in the hopes
that something will be useful. After all, how can you predict where
there will be problems on a customer's machine that didn't show up
during development? The second approach is to put yourself into a
mindset similar to when creating automated tests. You think about what
could possibly go wrong and try to log specific things in those areas.

I think I prefer the latter approach, since it requires thinking about
how to break your code, which usually means you'll fix some problems
before they ever make it out to the customer. There will also be less
clutter in the code obscuring its meaning. Reality may actually be
somewhere in the middle of the two approaches, though.

Take some time to read your log output occasionally to see if you can
more clearly or more concisely convey information. When a log looks
mostly like "spew", its effectiveness as a tool goes down.

Logging and error handling
--------------------------

A worry I always have with logging is the temptation to let it replace
error handling. You have to be really careful that this doesn't happen.
If user tries to do some operation, and something goes wrong, you have
to tell them in a reasonable way, like with an error dialog. Expecting
them to read a log file is not reasonable.

The trouble is that logging is really easy, and good error handling is
hard. Resist the temptation to inappropriately take the easy road.

Logging and testing
-------------------

Sometimes you log messages to verify that your application is working
correctly. Usually this means you look at the log output to confirm your
expected behavior. This is manual testing. Ask yourself if it wouldn't
be better to have an automated test instead of the log output. The test
does the verification for you, and can remember what good and bad output
looks like much longer than you can. In the long run, automated testing
is much more efficient than manual testing.

Good log messages
-----------------

If you add log messages to your code with the intent to leave them
there, they should conform to the high standards of the lines of
production code around them.

### Log messages should make sense

You should be able to read a log message and sort of know why someone
would want to log that information. Preferably you don't also have to
read the code to get the gist of a message. Logging "`hwnd=5433`" might
make sense to you (for a little while), but
`"New top-level active window detected (hwnd=5433`)" is probably more
valuable.

### Keep related information together

In the spirit of intelligibility, combine a single logical log message
into a single physical log statement. Consider this code snippet:

```java
logger.debug("flags: " + flags); 
logger.debug("widgets: " + widgets);
```

This is kind of a trivial example, but when you see the log output, it's
not really clear if the "flags" state and the "widget" state are
related, or if you're off in completely different methods when the
messages get output. If there are multiple threads writing to the log,
things can get even less clear. You can do something like this instead:

```java
StringBuffer buffer = new StringBuffer("Some interesting things:\n"); 
buffer.append(" flags: "); 
buffer.append(flags); 
buffer.append("\n widgets: "); 
buffer.append(widgets); 
logger.debug(buffer);
```

This approach makes it clear that this is a single message full of
related information. Of course you would probably want to surround the
whole thing with a check that logging is enabled to avoid the message
construction cost when it isn't needed.

### Format log messages

The previous example also makes some effort to make the format of the
message readable. Use new lines and delimiting characters to make the
log output easy to read.

### Make good use of toString

If you want to output an object's state, create a nice toString
override. This can simplify logging code quite a bit in some cases. For
example, Collection classes dump their elements out in nice format
already.

Instead of creating a log message this way:

```java
buffer.append("Document Files: ["); 
Iterator iterator = values().getIterator(); 
while (iterator.hasNext()) 
{ 
        DocumentFile file = (DocumentFile)iterator.next(); 
        buffer.append(file); 
        if (iterator.hasNext()) 
        { 
                buffer.append(", "); 
        } 
} 
buffer.append("]");
```

just do this:

```java
buffer.append("Document Files: "); 
buffer.append(values());
```

If you don't have control of the object to give it a nice toString, or
if toString is actually being used in business logic and can't be
changed, you can create an ObjectRenderer instead (a Log4J thing).

Reevaluate Log Levels
---------------------

After the system has been running for a while, go back and reconsider
the log levels for various things. Something that seemed like it needed
to be logged at INFO level might be relegated to DEBUG once that area of
the system has been running smoothly for a while. Again, if there is too
much "spew" it's hard to recognize when something truly important
happens.

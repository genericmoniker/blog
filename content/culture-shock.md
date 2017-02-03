Title: Culture Shock
Date: 2007-07-20 15:31
Author: Eric
Category: Opinion
Slug: culture-shock
Status: published

Over twenty years ago, I moved from Oregon to Utah to start going to
school at BYU. As we were driving to Provo from the north, my mom, who
had been born in Utah, commented, "This place right here is called the
point of the mountain."

"That's stupid, there's nothing here!" I remember saying, a bit more
harshly than was appropriate. I think my mom was a little taken aback,
and didn't bother to try to justify why the place deserved to have a
name: It separates Utah valley from the Salt Lake Valley, and the
counties with corresponding names; it's the highest point on I-15
through the Wasatch Front and the place you'll most likely hit snowy
roads.

I realized later that I was just experiencing culture shock. After an
email discussion with a coworker today, I realized that culture shock is
possible between programming environments.

<!--more-->

My coworker was announcing that he was going to create a new class for
working with file paths, because the .NET classes `FileInfo` and
`DirectoryInfo` were unintuitive, awkward and poorly conceived. Among
his concerns was that it seemed stupid that `FileInfo.Exists` on a path
returns false even if there is a directory there. You have to use
`DirectoryInfo.Exists` to know if there is a directory at a particular
location. He had a couple of other complaints as well, but I want to
focus on this one.

My coworker is a proficient Java programmer, and if you look at the .NET
Framework design decision to have both `FileInfo` and `DirectoryInfo`
from the perspective of someone coming from `java.io.File`, you can
understand his discomfort.

At the same time, I can imagine a .NET programmer deciding that
`java.io.File` is messed up. Where's the logic behind `File.isAFile()`?
That's like `Apple.isAnApple()`. And isn't it really awkward that in
order to know if a file (and not a directory) exists, I have to use both
`File.exists()` and `File.isAFile()`? Ah for the simplicity of
`FileInfo.Exists`!

I began to think that his complaints in this respect were more a matter
of Java to .NET culture shock -- it's not what he expects, so .NET is
wrong. That's not to say that I'm dismissing his concern by giving it a
label, but I'm noticing that it is an important thing to be aware of as
you become familiar with a new environment. It's really easy to flip the
bozo bit when you see something new that you don't immediately
understand. And I think it is a mistake to reject the idioms and
patterns of a programming environment because they're not like back
home.

For a sort of ridiculous example, consider an English speaker learning
German. Compared to German, English is a fairly genderless language.
Don't the Germans understand, though, that getting rid of gender would
be so much more efficient? Instead of having to remember nouns
*and* their gender, I can just remember the noun itself. Therefore, when
I speak german, I'm just going to say "the" instead of the pointlessly
complex "der", "die" and "das".

I also realize that I'm currently suffering from reverse culture shock.
I used to write a lot of Java code myself, and absolutely loved
JetBrains IntelliJ. I was thrilled with the discovery of each
well-crafted feature. It was agonizing to have to go back to Visual
Studio in order to write some native code.

But then I had to spend more and more of my time doing native
development. Visual Studio 2005 came out and life started getting better
(hallelujah! I can do a "rename" refactoring!). If I ever had occasion
to get back into the Java code to look at something, I'd double-click
the IntelliJ icon and then get out a magazine. Five minutes later the
application and project would finally be loaded and ready to work with.
And good grief, look at the memory footprint of that thing.

Java? IntelliJ? Eh.

But I do think "point of the mountain" is just as natural as can be
now.

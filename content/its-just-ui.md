Title: It's Just UI
Date: 2010-01-30 23:41
Author: Eric
Tags: User Interface
Slug: its-just-ui
Status: published

Maybe I've just imagined this -- created my own straw man to take down
-- but I've sometimes sensed some disparagement of user interface
programming. "It's just UI," the architect will say. "It's not like it's
a hard or interesting part of the system." As I've done more and more UI
development lately, I've had to consider if this is the direction I want
my career to go.

Some UIs amount to binding a data grid to a database. In fact, based on
Microsoft's tools and examples, there are apparently a lot of those. In
such cases, I agree, the UI isn't terribly interesting. But to build a
user interface for more sophisticated applications is a real challenge.
Here are some of the reasons why.

**Graphic design** - Even when you've got a talented graphic designer
helping out, you usually don't get handed everything you need, or
everything exactly perfect. You'll need to fill in the gaps to get a
complete, attractive interface. Being able to fire up Illustrator to
tweak and extrapolate, or layout a clean window are  good skills to
have. Modern UIs also include animations, which are hard to get from a
static "comp".

**Validation** - It is reasonable for the model to establish
preconditions for methods. When user input is involved, there are few
preconditions. Welcome to the wild west. Sure, you can insist that users
enter phone numbers without any dashes, spaces, dots, parentheses or
other corruptions of data purity, but if I'm the user, that just ticks
me off.

**Error reporting** - The buck stops here. The model can just throw an
exception if something goes wrong, but presenting a meaningful and
actionable error message to the user is hard.

**Threading** - For Windows applications, all interaction with a window
must happen on the thread that created the window. Yet to keep the UI
responsive, you shouldn't do time-consuming operations on the UI thread,
forcing the introduction of other threads. You can see something
slightly at odds here.

**Usability** - Small design and implementation decisions can greatly
impact usability, and what is easiest to code is frequently not what is
easiest to use. Most applications involve tasks with a fair amount of
complexity, and making them as simple as possible is way harder than
laying all of the complexities at the feet of the user.

**Testability** - There is a gulf associated with what it means for UI
to work. On one side, you have "functions as specified without defects".
On the other, you have "effectively supports the user in his/her goals".
Furthermore, it is really hard to unit test UI code, which sort of leads
to the next challenge...

**Pattern ambiguity** - I remember reading once (I wish I could remember
the source) that if you ask 10 developers what the Model-View-Controller
pattern is, you'll get 11 different answers. While the most touted
pattern in UI development, Model-View-Controller has so many variations
that it can be daunting to figure out what it even means, and a fair
amount of experience to begin to understand when a particular variation
is most appropriate.

**Localization** - Model code needs to be culture-sensitive, but the
biggest impact of localization is in the UI. Some frameworks make it
easier than others, but having a UI that lays out equally well with
"Archive Video on PC" and "Archivierung aufgezeichneter Videos auf dem
PC" is tricky.

**HCI priesthood** - If you have a CS degree and actually write *code*,
just give up now, you'll never get it. Or so I've been told, but I still
believe in the enlightened engineer.

I'm thinking that there's enough challenge here to be interesting and
skills that will continue to be in demand.

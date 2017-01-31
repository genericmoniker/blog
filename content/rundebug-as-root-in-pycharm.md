Title: Run/Debug as root in PyCharm
Date: 2015-05-05 20:33
Author: Eric
Category: Programming, Software Development
Tags: Linux, PyCharm, Python
Slug: rundebug-as-root-in-pycharm
Status: published

I'm working on a Python project that needs to run as root in order to
work properly. Previously I've just run the whole PyCharm IDE as root,
but this has some down-sides, and I think I have a better approach now.

<!--more-->

The biggest hassle with running the IDE as root is with file
permissions. I tend to jump back and forth between the command line and
the IDE, but if I do version control operations, or just add new files
within the IDE, they naturally are owned by root, and are inaccessible
from the terminal running with my normal user account. Of course, I
could run the terminal as root, but at some point, it starts to [sound
like a bad
idea](http://unix.stackexchange.com/questions/1052/concern-about-logging-in-as-root-overrated).

How To
------

So here is a way to run code as root, without running the whole IDE that
way. More detailed explanations are lower on the page.

### Don't require a password running sudo python

    sudo visudo -f /etc/sudoers.d/python

Add a line of the form:

    <user> <host> = (root) NOPASSWD: <full path to python>

For example:

    eric V-LU-ERSM = (root) NOPASSWD: /home/eric/Envs/my-project/bin/python

### Create a sudo script

Call the script python-sudo.sh, containing (with your correct full
python path):

    #!/bin/bash
    sudo /home/eric/Envs/my-project/bin/python "$@"

Be sure to make the script executable:

    chmod +x python-sudo.sh

### Use the script as your Python interpreter

In PyCharm, go to Settings &gt; Project Interpreter. Click the gear icon
by the current Project Interpreter drop-down, and choose "More…". Then
click the green plus icon to add a new interpreter (Add Local). Browse
to python-sudo.sh and select it, and set it as the interpreter for the
project.

Now when you run or debug, the code will run as root.

More details
------------

If you don't use the NOPASSWD option, it could still technically work,
but it would be kind of annoying as you'd have to provide your password
on every run. If you run PyCharm from a terminal window, the sudo
prompts appear *there*, not anywhere within PyCharm.

Also, when adding the shell script as an interpreter, PyCharm apparently
executes it multiple times because the terminal is spammed with password
prompts.

![pass-spam]({filename}/images/pass-spam.png)

PyCharm isn't very patient in waiting for some of those executions, so even if
you enter your password, its call to figure out the Python interpreter's
version might fail, and it will say it is an "Unknown" version.

The `/etc/sudoers.d/python` file *must* use a full path to the python
executable. In my case, I'm setting things up to point at a virtual
environment, but you could use the system python instead.

There are couple of things to note about the script itself. First, its
name must start with "python". Second, the `"$@"` in the script just
passes the script's received arguments straight through to Python, so
that when PyCharm starts with debugging options, those are correctly
forwarded.

When adding the script as an interpreter, PyCharm doesn't seem to want
to keep it unless it is set as *the* interpreter for the project. All
signs will indicate that you could have that as an independent
interpreter, but if you close the Settings dialog and reopen it, that
interpreter will be gone. I'm not sure if that is a PyCharm bug. The
reason this is interesting is that you *could* leave your normal
interpreter for the project, and pick the sudo interpreter within the
Run/Debug Configuration dialog for the configuration that needs to be
run as root.

As it is, you sort of have to do the opposite: The sudo python
interpreter is the default, and if you have other entry points you'd
like to *not* run as root, you can pick the "plain" interpreter for
those.

**Update:** A down-side to this strategy is that PyCharm can't generally
stop the process -- so if you click the "stop" button in the debugger,
it will detach but the process continues running. The debugger prints
the process id to the console when starting, though, so you can use that
to know what to kill.

### References

-   [How to run / debug programs with super user
    privileges](http://forum.jetbrains.com/thread/PyCharm-424)
-   [debugging in pyCharm with sudo
    privileges?](http://stackoverflow.com/questions/14299509/debugging-in-pycharm-with-sudo-privileges)
-   [How do I run specific sudo commands without a
    password?](http://askubuntu.com/questions/159007/how-do-i-run-specific-sudo-commands-without-a-password)


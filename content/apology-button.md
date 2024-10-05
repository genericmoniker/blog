Title: Raspberry Pi Pico Apology Button
Date: 2024-10-05 13:15
Author: Eric
Category: Project
Slug: apology-button
Status: published

When playing *Call of Duty*, I like "hardcore" mode, where a bullet or two is
enough to send someone off to respawn land rather than having to empty half a
clip. That mode also allows for friendly fire, which is a challenge. I
appreciate that the game starts reflecting damage back at you if you shoot your
own teammates too much -- I gave up Halo multi-player years ago when you
couldn't play without some griefer team killing constantly -- I still feel bad
when I round a corner and in surprise accidentally take out a teammate.

When that happens, I usually type out a quick "Sorry!" in the chat, because even
small efforts can lead to less rage in the world. But in high-action maps, I've
sometimes been shot and respawned twice by the enemy while I'm typing, which
also doesn't help my team any.

Enter: the Apology Button.

At a Python Meetup a while back, we built a one-button USB keyboard using a
[Rasperry Pi
Pico](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
microcontroller and
[CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/overview).
The presenter even threw in a nice 3D printed case for our modest registration
fee.

![One button keyboard]({static}/images/apology-button-1.jpg)

<small>*One button keyboard*</small>

![One button keyboard inside]({static}/images/apology-button-2.jpg)

<small>*One button keyboard inside*</small>

It was a fun little project for the educational value, but I was struggling to
find a practical application. Maybe it could type my password for me somewhere?
Meh.

But if I could just hit the button to issue an apology to my unfortunate
teammates, that would be cool.

When connecting the Pico with a USB cable (and make sure it is a data-enabled
cable, some USB cables only deliver power!) you get a USB flash drive with a
code.py file. You can edit the file, save it, and it will automatically reload
the code into the board. I think the system polls every 30-60 seconds for
changes to code.py, though, so it can be nicer to use CircutPython's [web-based
editor](https://code.circuitpython.org) to edit and immediately load the
changes into the board.

![CircuitPython Web Editor]({static}/images/apology-button-3.jpg)

Now when I'm playing COD and screw up I can just hit the button to express my
regret to my teammate. I originally thought it would be funny to have a very
formal, "Please accept my sincerest apologies, dear teammate, for my having
inappropriately shot you, mistaking friend for foe." But who has time to read
that when the 'nades are flying? So I opted for a few pithier apologies, one of
which is chosen at random.

Here is the complete code:

```python
"""code.py will run automatically when the board powers up."""
import time
import board
import digitalio
import usb_hid
import random

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

btn = digitalio.DigitalInOut(board.GP15)
btn.pull = digitalio.Pull.UP

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

apologies = [
    "Dang! Sorry about the TK!",
    "Sorry! My bad on the TK!",
    "Sorry for the TK!",
]

print("Apology button running...")
while True:
    if not btn.value:  # because of Pull.UP, falsey is when the button is pushed

        # Team chat key binding (have to set this explicitly in the game):
        keyboard.send(Keycode.KEYPAD_PLUS)
        time.sleep(0.5)

        # Apologize:
        apology = random.choice(apologies)
        keyboard_layout.write(apology)

        # Send chat:
        keyboard.send(Keycode.ENTER)

        # Debounce:
        time.sleep(1)
```

I imagine there's a simpler (and less fun) way to do this with some kind of
macro-enabled gaming keyboard, but I've got a 20+ year old Microsoft keyboard,
so this is a great solution for me.

![Apology Button deployed]({static}/images/apology-button-4.jpg)

<small>*Apology Button deployed*</small>

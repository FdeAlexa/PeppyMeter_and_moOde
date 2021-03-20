## Functional and customization tests

We just have to try the operation and customize the aesthetics of our PeppyMeter.
To see the meter on the default display we have to start listening music and:
```
cd /home/pi/PeppyMeter
sudo python3 peppymeter.py
```
We should see, on the display, a kind of VU Meter that changes every 20 seconds (the time can be changed in the config.txt).
A couple of messages (warning) appear on the peppy screen at each change: don't care.
I suggest you, once you have decided which one you prefer, to stop the PeppyMeter:
with a 
```
double (Ctrl "c")
```
There are many parameters that can be changed in the program's config.txt. Let's analyze the type of VU Meter: currently there are numerous available and, for the video resolution we use (800x480), corresponding to "screen.size = large", they are the following:
```
bar
blue
vintage
dash
gas
rainbow
grunge
royal
compass
gold
black-white
white-red
orange
blue-2
emerald
red
tube
```
then configure our PeppyMeter:

Quote:
Code:
sudo nano /home/pi/PeppyMeter/config.txt

modifying the following contents. From:
Code:
"meter = random"

to e.g.:
Code:
"meter = emerald"

Ctrl o and Enter to save and then Ctrl x to exit.

Then start again:

Code:
cd /home/pi/PeppyMeter
sudo python3 peppymeter.py

Enjoy listening music... and its graphic


[Previous](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/3_PeppyMeter.md) / [Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md) 

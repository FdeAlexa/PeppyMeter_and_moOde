## Functional and customization tests

We just have to try the operation and customize the aesthetics of our PeppyMeter.
To see the VU Meter on the default display we have to start listening music and:
```
cd /home/pi/PeppyMeter
DISPLAY=:0 python peppymeter.py
```
We should see, on the display, a kind of VU Meter that changes every 20 seconds (the time can be changed in the config.txt).
A couple of messages (warning) appear on the peppy screen at each change: don't care.
I suggest you, once you have decided which VU Meter you prefer, to stop the PeppyMeter:
with a 
```
double (Ctrl "c")
```
There are many parameters that can be changed in the program's config.txt. Let's analyze the type of VU Meter (meter =): currently there are numerous available and, for the video resolution we use (800x480), corresponding to "meter.folder = 800x480", they are the following:
```
bar
big-bang
black-white
blue-2
blue
chillout
compass
dash
emerald
fantasy
gas
gold
grunge
orange
rainbow
red
relax
ring
royal
steam-punk
tube
vertical-circular
vertical-linear
vintage
white-red
```
This is very simple: 
```
nano /home/pi/PeppyMeter/config.txt
```
going to replace the content of the second line from:
```
"meter = random"
```
to, e.g.:
```
"meter = emerald"
```
Then save the file (Ctrl "o" and Enter)
and exit (Ctrl "x")

Note that the meaning of the parameters reported in the program's config.txt file can be found in https://github.com/project-owner/PeppyMeter.doc/wiki.

At this point: let us start again PeppyMeter:
```
cd /home/pi/PeppyMeter
DISPLAY=:0 python peppymeter.py
```
and...
Enjoy listening music... and its graphic

[Previous](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/3_PeppyMeter.md) / [Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md) 

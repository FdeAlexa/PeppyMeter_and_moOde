## Installation, configuration and modification of PeppyMeter
We have already installed and configured PeppyAlsa, then we modified moOde and checked that everything was done correctly; now we need to install the graphics part.
The following are the commands to install PeppyMeter:
```
cd /home/pi
git clone https://github.com/project-owner/PeppyMeter.git
sudo apt-get install python3-pygame
cd /home/pi/PeppyMeter
```
Now we just have to modify and configure PeppyMeter.
The change is to disable the double buffer, which is not compatible with the rpi touch screen.
To do this we need to modify the peppymeter.py program, as follows:
```
nano /home/pi/PeppyMeter/peppymeter.py
```

Ctrl -142 to go to row 142 and modify the current content from:
       
Code:
self.util.PYGAME_SCREEN = pygame.display.set_mode((screen_w, screen_h), pygame.DOUBLEBUF, depth)
to the new content:
Code:
self.util.PYGAME_SCREEN = pygame.display.set_mode((screen_w, screen_h))

Ctrl o and Enter to save and then Ctrl x to exit.


Code:
cd /home/pi
git clone https://github.com/project-owner/PeppyMeter.git
sudo apt-get install python3-pygame
cd /home/pi/PeppyMeter

Now we have to configure our PeppyMeter:


Quote:
Code:
nano /home/pi/PeppyMeter/config.txt

modifying the following contents:
Code:
"screen.size = large"
"framebuffer.device = /dev/fb0"
"mouse.device = /dev/input/event0"
"pipe.name = /var/tmp/peppyfifo"

Ctrl o and Enter to save and then Ctrl x to exit.

Now we have to modify the program to disable the double buffer:


Quote:
Code:
nano /home/pi/PeppyMeter/peppymeter.py

Ctrl -142 to go to row 142 and modify the current content from:
       
Code:
self.util.PYGAME_SCREEN = pygame.display.set_mode((screen_w, screen_h), pygame.DOUBLEBUF, depth)
to the new content:
Code:
self.util.PYGAME_SCREEN = pygame.display.set_mode((screen_w, screen_h))

Ctrl o and Enter to save and then Ctrl x to exit.

At this point we have finished. To see the meter on the default display we have to start listening music and:

Code:
cd /home/pi/PeppyMeter
sudo python3 peppymeter.py

We should see, on the display, a kind of meter that changes every 20 seconds (time can be changed in the config.txt).
On the Putty screen appears a couple of message (like an error) at every change.
I suggest that, once you have decided what you prefer, to stop the meter:

Quote:Ctrl c Ctrl c 

The available type of meter, for the "large" size we have choosen, at the moment, are:

Quote:
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

then configure our PeppyMeter:



```aplay -l```

and take care of the result because it will be useful later.

PeppyMeter needs PeppyAlsa to run: so we need first to install and adapt it to our environment.
The following are the command to install PeppyAlsa:
```
git clone https://github.com/project-owner/peppyalsa.git
cd peppyalsa
sudo apt-get install build-essential autoconf automake libtool libasound2-dev libfftw3-dev
aclocal && libtoolize
autoconf && automake --add-missing
./configure && make
sudo make install
```
Now we have to create a new files ````/etc/asound.conf````. In the third row (slave.pcm) of this file we have to put the default output we have in the moOde system.
This value (that normally is "hw:0,0" or "hw:1,0") is contained in the `aplay -l` results. E.g. if the results is 
`**** List of PLAYBACK Hardware Devices ****
card 0: PianoDAC [PianoDAC], device 0: Piano DAC HiFi pcm512x-hifi-0 [Piano DAC HiFi pcm512x-hifi-0]
  Subdevices: 0/1
  Subdevice #0: subdevice #0
`
The slave.pcm must contain "hw:X,Y" where X is the card (in this case "0") and Y is the device (in this case "0"): that means that we have to to insert:
`slave.pcm "hw:0,0"`

So: to create the file:
```
sudo nano /etc/asound.conf
```
Copy and past the following content:

```
pcm.peppyalsa {
       type meter
       slave.pcm "hw:0,0"
       scopes.0 peppyalsa
}
pcm_scope.peppyalsa {
       type peppyalsa
       decay_ms 400
       meter "/var/tmp/peppyfifo"
       meter_max 100
       meter_show 0
       spectrum "/var/tmp/peppyfifosa"
       spectrum_max 100
       spectrum_size 30
}
pcm_scope_type.peppyalsa {
       lib /usr/local/lib/libpeppyalsa.so
}
```
Modifying the value of the third row if necessary.
Then save the file (Ctrl "o")
and exit (Ctrl "x")

[Previous](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_moOde.md) / [Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md) /  [Next](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/4_Tests.md)

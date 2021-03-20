## Installation, modification and configuration of PeppyMeter
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
Let us go to the line 142 (Ctrl "-142")
and modify the current content from:
```
self.util.PYGAME_SCREEN = pygame.display.set_mode((screen_w, screen_h), pygame.DOUBLEBUF, depth)
```
to the new content:
```
self.util.PYGAME_SCREEN = pygame.display.set_mode((screen_w, screen_h))
```
Then save the file (Ctrl "o")
and exit (Ctrl "x")

The last step, before being able to see the result of our work, is to configure PeppyMeter, modifying the program's config.txt as follows:
```
nano /home/pi/PeppyMeter/config.txt
```
going to replace the content of only the lines below and leaving everything else unchanged:
```
"screen.size = large"
"framebuffer.device = /dev/fb0"
"mouse.device = /dev/input/event0"
"pipe.name = /var/tmp/peppyfifo"
```
Then save the file (Ctrl "o")
and exit (Ctrl "x")

[Previous](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_moOde.md) / [Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md) /  [Next](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/4_Tests.md)

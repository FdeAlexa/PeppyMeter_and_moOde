## Installation, modification and configuration of PeppyMeter
We have already installed and configured PeppyAlsa, then we modified moOde and checked that everything was done correctly; now we need to install the graphics part.
The following are the commands to install PeppyMeter:
```
cd /home/pi
git clone https://github.com/project-owner/PeppyMeter.git
sudo apt-get install python3-pygame
cd /home/pi/PeppyMeter
```
(In case of any error downloading Pygame, please use the following command:
```
sudo apt update --allow-releaseinfo-change
```
and try again.
Now we just have to configure PeppyMeter, modifying the program's config.txt as follows:
```
nano /home/pi/PeppyMeter/config.txt
```
going to replace the content of only the lines below and leaving everything else unchanged:
```
meter.folder = 800x480
framebuffer.device = /dev/fb0
mouse.device = /dev/input/event0
double.buffer = False
pipe.name = /var/tmp/peppyfifo
```
Then save the file (Ctrl "o" and Enter)
and exit (Ctrl "x")

[Previous](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_moOde.md) / [Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md) /  [Next](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/4_Tests.md)

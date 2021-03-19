## Modification of moOde

At this point we have to patch an important file that contributes to the creation of the moOde MPD configuration: this file is different for each moOde release: now let's choose which release we are using.
* [moOde 6.7.1](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_1_moOde671.md)
* [moOde 7.0.1](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_2_moOde701.md)
* [moOde 7.1.0](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_3_moOde710.md)

Code:
sudo nano /var/www/inc/playerlib.php

For moOde 7.0.1:
Quote:Ctrl -1994 to go to row 1994 and modify the current content from:
For moOde 7.1.0:
Quote:Ctrl -2041 to go to row 2041 and modify the current content from:
Code:
"name \"ALSA default\"\n" . "device \"hw:" . $device . ",0\"\n",

to the new content:
Code:
"name \"ALSA default\"\n" . "device \"peppyalsa\"\n",

Ctrl o and Enter to save and then Ctrl x to exit.

Now reboot the system and try to listen any music (a radio is the simplest way) if it is still alive!!! If not we have to troubleshoot where we made a mistake.

First of all let us open a putty session on our moOde system and run:

```aplay -l```

and take care of the result because it will be useful later.



[Previous](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/1_PeppyAlsa.md) / [Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md) /  [Next](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/3_PeppyMeter.md)

## Upgrade to moOde 7.1.0
This section is dedicated to those who, already with moOde 7.0.1, had previously installed PeppyMeter and, now, have upgraded to moOde 7.1.0. Obviously the PeppyMeter does not work as there is a need to modify the file ````playerlib.php```` for the release 7.1.0: please return to [previous](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_moOde.md) page if your current release is not 7.1.0.

To modify it:
```
sudo nano /var/www/inc/playerlib.php
```
Let us go to the line 2041 (Ctrl "-2041" and Enter)
and modify the current content from:
```
"name \"ALSA default\"\n" . "device \"hw:" . $device . ",0\"\n",
```
to the new content:
```
"name \"ALSA default\"\n" . "device \"peppyalsa\"\n",
```
Then save the file (Ctrl "o" and Enter)
and exit (Ctrl "x")

Now 
```
reboot
```
the system and try to listen any music (a radio is the simplest way) if the moOde is still alive!!! 

At this point: let us start again PeppyMeter:
```
cd /home/pi/PeppyMeter
sudo python3 peppymeter.py
```
and...
Enjoy listening music... and its graphic

[Previous](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_moOde.md)

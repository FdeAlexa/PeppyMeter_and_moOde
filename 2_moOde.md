## Modification of moOde

At this point we have to patch an important file that contributes to the creation of the moOde MPD configuration: this file is different for each moOde release: now let's choose which release we are using.
* [moOde 6.7.1](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_1_moOde671.md)
* [moOde 7.0.1](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_2_moOde701.md)
* [moOde 7.1.0](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_3_moOde710.md)

Now reboot the system and try to listen any music (a radio is the simplest way) if the moOde is still alive!!! 
If not we have to troubleshoot where we made a mistake.

If everything is ok, let us continue:
```
cd /home/pi/peppyalsa/src
gcc peppyalsa-client.c -o peppyalsa-client
```
At this point we can test the whole chain built up to now:
```
/home/pi/peppyalsa/src/peppyalsa-client /var/tmp/peppyfifo
```
Listening the music we should see on the putty screen a couple of bar moving with the music intensity, as the following picture:

![peppyalsa-client](https://user-images.githubusercontent.com/71403166/111850325-47ae0100-8910-11eb-9394-1a7616727404.jpg)
    
Now we are closer to the end: we have, now, to install PeppyMeter.

[Previous](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/1_PeppyAlsa.md) / [Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md) /  [Next](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/3_PeppyMeter.md)

## Installation, configuration and modification of PeppyMeter

First of all let us open a putty session on our moOde system and run:

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

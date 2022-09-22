## Installation and configuration of PeppyAlsa

First of all let us open a putty session on our moOde system and run:

```aplay -l```

and take care of the result because it will be useful later.

PeppyMeter needs PeppyAlsa to run: so we need first to install and adapt it to our environment.
The following are the command to install PeppyAlsa:
```
sudo apt install git
git clone https://github.com/project-owner/peppyalsa.git
cd peppyalsa
sudo apt-get install build-essential autoconf automake libtool libasound2-dev libfftw3-dev
aclocal && libtoolize
autoconf && automake --add-missing
./configure && make
sudo make install
```

[Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md) / [Next](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_moOde.md)

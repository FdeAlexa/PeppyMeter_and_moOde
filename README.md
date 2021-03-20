# PeppyMeter_and_moOde
PeppyMeter is a software VU Meter written in Python. It was originally developped as the new 'VU Meter' screensaver for Peppy Player. With minor modifications it became a stand-alone application. PeppyMeter gets audio data from media players (e.g. mpd) via fifo and displays current volume level in a Graphical User Interface in a form of traditional VU Meter. During the last few years there have been several versions and editions, aimed at improving the product and, mainly, aimed at increasing the number, type and resolution of VU meters. The product's original repository and wiki can be consulted in https://github.com/project-owner/PeppyMeter and in https://github.com/project-owner/PeppyMeter.doc/wiki.

MoOde audio is an audio player system for Raspberry Pi. It provides a beautifully designed and responsive Adaptive User Interface, extensive set of Audiophile options and support for a wide variety of audio devices designed to work with the wonderful Raspberry Pi family of Single Board Computers. Also for moOde there have been numerous releases mainly aimed at improving the user interface, increasing functionality and increasing the supported devices. The moOde official website and the repository can be consulted respectively in https://moodeaudio.org/ and in https://github.com/moode-player.

The successful integration of these two systems and therefore the creation of this repository was possible thanks to the help of some components of two large forums: that of diyAudio and moOde: in particular in the threads https: //www.diyaudio.com/forums/pc-based/291010-peppymeter.html and http://moodeaudio.org/forum/showthread.php?tid=155.
As a result, a thread dedicated to the subject was also generated: http://moodeaudio.org/forum/showthread.php?tid=3484.

It was decided to structure this repository in different sections which basically reflect the implementation of the integration and any additional developments. Please note that 
``
all the four steps
``
has to be completed and in the correct order to integrate PeppyMeter in moOde.
In particular the chapters are:
### Integration
1. [Installation and configuration of PeppyAlsa](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/1_PeppyAlsa.md)
2. [Modification of moOde](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/2_moOde.md)
3. [Installation, modification and configuration of PeppyMeter](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/3_PeppyMeter.md)
4. [Functional tests and customization](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/4_Tests.md)
### Additional developments
* [Creation of scripts & service](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/5_Script_Services.md)
* [Implementation of two buttons solution](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/5_Buttons.md)

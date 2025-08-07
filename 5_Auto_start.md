## Auto start (AutoPeppy)
This section is dedicated to those who want to start PeppyMeter automatically, following the audio playback, instead of the moOde GUI, I have prepared a Python program which, started as a service, checks the status of the MPD and, consequently, starts and stops PeppyMeter.
Obviously the first step is to have PeppyMeter: installed and running (see the complete procedure).
As mentioned, the program checks the current playback status: to do this, you need to enable metadata updating as follows:

At the moOde UI: go to
```
Menu / 
Configure / 
Audio /
MPD Options /
General
```
then set Metadata file to
```
ON
```

# Copy the files FdA_AutoPeppy (fda_autopeppy.py and fda_autopeppy.service) in to the PeppyMeter directory (/home/pi/PeppyMeter)
```
Now we just have to configure PeppyMeter, modifying the program's config.txt as follows:


```
nano /home/pi/PeppyMeter/config.txt
```

going to replace the content of only the line below and leaving everything else unchanged:

```
"exit.on.touch = True"
```

This will allow you to go back to the GUI mode for a short time with a simple tap on the touch screen.

So to create the service that will automatically start the driver run the following commands:
Code:

```
sudo cp /home/pi/PeppyMeter/fda_autopeppy.service /etc/systemd/system/
sudo chmod +111 /etc/systemd/system/fda_autopeppy.service
sudo systemctl daemon-reload
sudo systemctl enable fda_autopeppy.service
sudo systemctl start fda_autopeppy.service
```

Reboot the system
The PeppyMeter will start at the first "play".

Enjoy listening music... and its graphic

[Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md)

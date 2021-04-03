## Creation of scripts & service

### Scripts
Let's analyze some methods to start and obviously stop the PeppyMeter execution.

As previously mentioned, to be able to start it, simply run the program in python language in the application directory. This start can take place with the following commands:
```
cd /home/pi/PeppyMeter
sudo python3 peppymeter.py
```
This method has 2 limitations:
1. Using an SSH (putty) session to start the command
2. dedicated session until the end of the use of the program. In fact the session will be busy until
```
double (Ctrl "c")
```
just to finish.

Another method for controlling the program is to use two scripts: one to start the program, the other to end its use. This method still involves using an SSH (putty) session to initiate the start command, but not exclusive use until the stop command.

The first script we call peppyON:
```
nano /home/pi/PeppyMeter/peppyON.sh
```
Copy and past the following content:
```
#!/bin/sh
cd /home/pi/PeppyMeter && sudo python3 peppymeter.py > /dev/null 2>&1 &
```
Then save the file (Ctrl "o" and Enter)
and exit (Ctrl "x").

While we're at it, we also create the service stop script:
```
nano /home/pi/PeppyMeter/peppyOFF.sh
```
Copy and past the following content:
```
#!/bin/sh
sudo pkill -f peppymeter
```
Then save the file (Ctrl "o" and Enter)
and exit (Ctrl "x").

At this point we have to enable our scripts to be executed:
```
sudo chmod +111 /home/pi/PeppyMeter/peppyO*.sh
```
We just have to try them now:
```
/home/pi/PeppyMeter/peppyON.sh
```
check that everything works and then:
```
/home/pi/PeppyMeter/peppyOFF.sh
```
to finish and return to the moOde GUI.

### Service
Another method to be able to start the PeppyMeter program is to use it as a service: this will result in automatic startup when our moOde system is turned on. Which means we should act externally to operate with the moOde GUI.

Obviously by stopping the service, the gui will become available.

To create the service we need to create another script that starts the PeppyMeter with a delay that allows the system, at power on, to load the GUI before the PeppyMeter.
```
nano /home/pi/PeppyMeter/peppySER.sh
```
Copy and past the following content:
```
#!/bin/sh
sleep 20 && cd /home/pi/PeppyMeter && sudo python3 peppymeter.py
```
Then save the file (Ctrl "o" and Enter)
and exit (Ctrl "x").

At this point we have to enable our script to be executed:
```
sudo chmod +111 /home/pi/PeppyMeter/peppySER.sh
```
And now let's create the real service
```
nano /home/pi/PeppyMeter/peppymeter.service
```
Copy and past the following content:
```
[Unit]
Description=PeppyMeter, start a virtual VU Meter display
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/pi/PeppyMeter/
ExecStart=/home/pi/PeppyMeter/peppySER.sh

[Install]
WantedBy=default.target

```
Then save the file (Ctrl "o" and Enter)
and exit (Ctrl "x").

Then we copy it to the system area reserved for services:
```
sudo cp /home/pi/PeppyMeter/peppymeter.service /etc/systemd/system/
```
The service must therefore be enabled:
```
sudo systemctl daemon-reload
sudo systemctl enable peppymeter.service
```
and then started
```
sudo systemctl start peppymeter.service
```
After a while (>20 sec.) we will see the VU Meter screen.

As already mentioned, at this point when the system starts up we will have the VU Meters on the display, instead of the moOde GUI.

Of course there is the command to stop the service (and then return to the moOde GUI):
```
sudo service peppymeter stop
```
and that to know the status:
```
sudo service peppymeter status
```
and to restart it
```
sudo service peppymeter start
```

A possible evolution is to use two buttons to start and stop the program: see [Implementation of two buttons solution](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/5_Buttons.md)

[Home](https://github.com/FdeAlexa/PeppyMeter_and_moOde/blob/main/README.md) 

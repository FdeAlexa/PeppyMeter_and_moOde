#!/usr/bin/env python

import subprocess
#from subprocess import Popen
import time
from datetime import datetime

prevstat = "OFF"    
pause = "OFF"
lastsong = ""
currentSongTitle = ""
proc = None

def moodeCurrentSong():
    songc = 1
    info =""
    contaloopsong = 1
    while songc < 14:
        with open('/var/local/www/currentsong.txt', 'r') as f:
            info = f.read()
        songc = info.count('\n')
        contaloopsong = contaloopsong + 1        
        if songc > 10:    
            song = dict([t.split('=',1) for t in info.strip().split('\n')])

    return song

def graph_monitor():
    global prevstat
    global lastsong
    global proc

    progname = "/home/pi/PeppyMeter/peppymeter.py"
    song = moodeCurrentSong()
    currentSongTitle = song['title']

    if song['state'] == "play" and prevstat == "OFF":
       prevstat = "ON"
       lastsong = currentSongTitle
       time.sleep(4) # Give time so moOdeaudio can wake up the screen 
       proc = subprocess.Popen(["sudo", "python3", progname], shell=False)
    elif ( song['state'] == "pause" or song['state'] == "stop" )and prevstat == "ON":
       prevstat = "OFF"
       subprocess.run(["sudo", "pkill","-f", "peppymeter.py"])


    if song['state'] == "play" and lastsong != currentSongTitle and prevstat == "ON":
       if proc.poll() != None:
          prevstat = "OFF"
          lastsong = currentSongTitle 

def main():
    global x
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print ("Inizio programma - ", dt_string)
    while True:
        graph_monitor()
        time.sleep(0.1)
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass


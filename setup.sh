#!/bin/sh

#Install Python Modules Using PIP
pip install gtts
pip install pygame
pip install mutagen
pip install speechrecognition

#Install Python Support
sudo apt install python3-pyaudio
sudo apt install alsamixer

#Finish Up
chmod +x run.sh
ls
echo "Done"
echo "Running Now"
./run.sh

#!/bin/sh

#install python and support
echo "Installing Python and supports"
sudo apt install python3 python3-pip python3-pyaudio alsamixer -y

#Install Python Modules Using PIP
echo "Installing python libaries using Pip"
pip install gtts
pip install pygame
pip install mutagen
pip install speechrecognition

#Finish Up
echo "Finishing up"
chmod +x run.sh
ls
echo "Done"
echo "Running Now"
./run.sh

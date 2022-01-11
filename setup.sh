#!/bin/sh

<<<<<<< HEAD
#Install python and supports
echo "Installing Python3 and supports"
sudo apt install python3 python3-pip python3-pyaudio alsamixer

#Install Python Modules Using PIP
echo "Installing Python libaries using PIP"
=======
#install python and support
echo "Installing Python and supports"
sudo apt install python3 python3-pip python3-pyaudio alsamixer -y

#Install Python Modules Using PIP
echo "Installing python libaries using Pip"
>>>>>>> c11f1d6b66b8e1bc7526c9c90db412672beba069
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

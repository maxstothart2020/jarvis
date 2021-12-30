#Setup

#user editable variables
language = 'en'
accent = 'co.za' #south african?
name = 'Friday' #Name of the system
title = 'Sir' #What The system calls you

#system Variables
run = True
init = False

#Import Libaries
import speech_recognition as sr
from gtts import gTTS
import time
from pygame import mixer
from mutagen.mp3 import MP3

#Define functions

#play
def play(filename):
    mixer.init()
    mixer.music.load(filename)
    song = MP3(filename)
    delay = song.info.length
    print(delay) #<-- Debug Only
    mixer.music.play()
    time.sleep(delay)

#TTS
def speak(text):
    tts = gTTS(text=text, tld=accent, lang=language,  slow=False)
    filename = 'voice.mp3'
    tts.save(filename)
    play(filename)

#init
def beep():
    play("beep.mp3")

#Main Program
r = sr.Recognizer()

while run:
    mic = sr.Microphone()
    command = ""
    print('start talking')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio_text = r.listen(source)
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print(text) #uncomment for debug
            command = text
         
        except:
             print('Sorry Whave encountered an error retrying now')
             
    if command != '' and init == True:
        if command == 'hey '+name or command == 'ok '+name or command == 'hello '+name:
            response = ("Hello "+title+", how may I help you today?")
            speak(response)
            beep()
    elif init == False:
        if command == 'hey '+name or command == 'ok '+name or command == name:
            beep()
            init = True
            print(init) #<--debug

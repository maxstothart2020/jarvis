#Setup

#user editable variables
language = 'en'
accent = 'co.za' #south african?
name = 'Jarvis' #Name of the system
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
from datetime import datetime

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
    print(text)
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
    """
        elif command == "" or command == "":
            response = ""#+" "+title+" "+""
            speak(responses)
    """
    if command != '' and init == True:
        if command == 'hey '+name or command == 'ok '+name or command == 'hello '+name:
            response = ("Hello "+title+", how may I help you today?")
            speak(response)
            beep()
        elif command == "shut down" or command == "stop":
            speak("processing")
            speak("Are you sure?")
            mic = sr.Microphone()
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio_text = r.listen(source)
                print("processing")
                text = r.recognize_google(audio_text)
                print(text) #uncomment for debug
                confirm = text
            if confirm == "yes":
                run = False
        elif command == "what time is it" or command == "what is the time" or command == "what's the time":
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            speak(dt_string)
        elif command == "what day is it" or command == "what is the day" or command == "what's the day today":
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y")
            speak(dt_string)
    elif init == False:
        if command == 'hey '+name or command == 'ok '+name or command == name:
            beep()
            init = True
            print(init) #<--debug

import speech_recognition as sr
from gtts import gTTS
import os
import time
from pygame import mixer
from mutagen.mp3 import MP3

run = True

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
            #uncomment line below for debug
            print(text)
            command = text
         
        except:
             print('Sorry Whave encountered an error retrying now')


#variables
language = 'en'
accent = 'co.za'
#Import Libaries

import speech_recognition as sr
from gtts import gTTS
import os
import time
import vlc

#Define txt output function
def speak(text):
    tts = gTTS(text=text, tld=accent, lang=language,  slow=False)
    filename = 'voice.mp3'
    tts.save(filename)
    speech = vlc.MediaPlayer(filename)
    speech.play()
    
#run function speak
speak("the weather is cloudy")

#Setup

#variables
language = 'en'
accent = 'co.za'
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

    
#run function speak
speak("the weather is cloudy")

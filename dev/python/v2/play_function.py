from pygame import mixer
from mutagen.mp3 import MP3
import time

def play(filename):
    mixer.init()
    mixer.music.load(filename)
    song = MP3(filename)
    delay = song.info.length
    print(delay)
    mixer.music.play()
    time.sleep(delay)

while True:
    play('voice.mp3')

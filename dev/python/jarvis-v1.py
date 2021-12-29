#variables
#choose if the user should give a title
title = "Max"
name = "Friday"
#title = input("What Should I Call You:")

#speech Output Settings
language = 'en'
accent = 'ie' #South African

#System Variables
run = True
joke = 1
command = ""

#speech to text

#import libraries
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

#define text to speech program
def speak(tts):
    tts = gTTS(text=tts, tld=accent, lang=language,  slow=False)
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


#run While Loop
while run:

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

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

    #code
    """
    Blank Voice Command For Copy And Paste
    
    elif command == '':
        response = ""# + " " + title
        print("")
        print(response)
        speak(response)
        
    """
    if command != '':
        if command == name or command == 'hey ' + name or command == 'OK' + name:
            print("")
            print("Yes " + title)
            speak("Yes " + title)
        elif command == 'initiate Lockdown protocol' or command == 'initiate Lockdown procedure' or command == 'activate Lockdown procedure' or command == 'activate Lockdown protocol':
            print("")
            print("Lockdown Protocol Initiated")
            speak("Lockdown Protocol Initiated")
        elif command == 'exit' or command == 'deactivate' or command == 'restart' or command == 'reboot' or command == 'shut down':
            print("")
            print("Shutting down")
            speak("Shutting down")
            run = False
        elif command == 'tell me a joke':
            
            if joke == 1:
                print("Your Mum " + title)
                speak("Your Mum " + title)
                joke = joke+1
            elif joke == 5:
                print("Your Face " + title)
                speak("Your Face " + title)
                joke = joke+1
            elif joke == 6:
                print("Your Life " + title)
                speak("Your Life " + title)
                joke = joke+1
            elif joke == 2:
                print("Why did the chicken cross the road?")
                speak("Why did the chicken cross the road?")
                print("To get to the Idiots house!")
                speak("To get to the Idiots house!")
                print("Knock Knock")
                speak("Knock Knock")
                joke = joke+1
            elif joke == 3:
                print("You're so fat that when you got on the scales they said: I need your weight not your phone number")
                speak("You're so fat that when you got on the scales they said: I need your weight not your phone number")
                joke = joke+1
            elif joke == 8:
                print("Why is Peter Pan always flying?")
                speak("Why is Peter Pan always flying?")
                print("He Never lands.")
                speak("He Never lands.")
                joke = joke+1
            elif joke == 7:
                print("Today I actually saw a dwarf prisoner climbing down a wall")
                speak("Today I actually saw a dwarf prisoner climbing down a wall")
                print("I thought to myself, now that’s a little condescending")
                speak("I thought to myself, now that’s a little condescending")
                joke = joke+1
            elif joke == 4:
                print("That vegan teacher")
                speak("That vegan teacher")
                joke = 1
        elif command == 'hello Jarvis':
            response = "Hello" + " " + title
            print("")
            print(response)
            speak(response)
        elif command == "I'm sad" or command == "I am sad" or command == "I feel sad":
            response = "It is OK" + " " + title + ", " + "I am here for you, :)"
            response2 = "It Might be a good Idea to call Arny or Patrick"
            print("")
            print(response)
            speak(response)
            print(response2)
            speak(response2)
        elif command == "I'm angry" or command == "I am angry" or command == "I feel angry":
            if title == "Sir":
                response = "OK" + " " + title + " It is probably a good Idea to call Patrick or Arny"
                response2 = "In the mean time, Do you want to talk"
                print("")
                print(response)
                speak(response)
                print(response2)
                speak(response2)
            elif title == "Max":
                response = "OK" + " " + title + " It is probably a good Idea to call Patrick or Arny"
                response2 = "In the mean time, Do you want to talk"
                print("")
                print(response)
                speak(response)
                print(response2)
                speak(response2)
            else:
                response = "OK" + " " + title + " It is probably a good Idea to call someone you trust."
            print("")
            print(response)
            speak(response)
    """
     else:
        run = False
    """
        

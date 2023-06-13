import os
import time
import playsound
import datetime
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import webbrowser as wb
import wikipedia
import pyjokes
import requests
from requests import get

from PIL import ImageGrab
vname="chotu"
def screenshot():
    ch=ImageGrab.grab()
    ch.save('screeni.png')
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def get_command():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:                 #using microphone to hear audio
        print("listening")
        audio=r.listen(source)                        #using microphone wali audio(named source) as our actual audio
        try:
            print("recognising")
            mytext=r.recognize_google(audio)
            mytext= mytext.lower()
            print("user said  " + mytext)
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "none"
    return mytext

def username():
    speak("What should i call you sir")
    uname = get_command()
    speak("Welcome Miss")
    speak(uname)
        
        
username()

while True:
    order = get_command().lower()
    
    if "open youtube" in order:
        speak("opening youtube")
        wb.open("youtube.com")
        
    elif "open google" in order:
        speak("opening google")
        wb.open("google.com")
        
    elif "the time" in order:
        ans=datetime.datetime.today()
        speak(f"sir, the time is {ans}")
        
    elif "how are you" in order:
        speak("I am fine, Thank you")
        speak("How are you, Sir")
        
    elif "Good Morning" in order or "good afternoon" in order or "good night" in order or "good evening" in order:
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            speak("Good Morning Sir !")
  
        elif hour>= 12 and hour<18:
            speak("Good Afternoon Sir !")  
  
        else:
            speak("Good Evening Sir !")
            speak("How are you Miss")
            
            
    elif "fine" in order or "good" in order:
        speak("It's good to know that your fine")
        
    elif "what is your name" in order or "what's your name" in order:
        speak("my name is ")
        speak(vname)
        print("my name is  ", vname)
        
    elif "joke" in order:
        speak(pyjokes.get_joke())
        
    elif "i love you" in order:
        speak("you deserve better")
        
    elif "will you be my girlfriend" in order or "will you be my bf" in order:  
        speak("I'm not sure about, may be you should give me some time")
        
    elif "song" in order:
        speak("opening spotify")
        link="https://open.spotify.com/playlist/7Iba3sBxwW7RDjFOqaY10w"
        wb.open(link)
        
    elif "location" in order:
        apid=get('https://api.ipify.org').text
        print(apid)
        apilinki="https://geo.ipify.org/service/account-balance?apiKey="+ apid
        print(apilinki)
        apilink=get(apilinki).json()
        print(apilink)
        #print(apilink.location.country)
    
    elif "screenshot" in order:
        speak("taking screenshot")
        screenshot()
        speak("screenshot captured")
        print("screenshot captured")
        
    elif "calculator" in order:
        try:
            speak("opening calculator")
            os.system('cmd /k "calc"')
        except:
            speak("could not open")
    
    elif "notepad" in order:
        try:
            speak("opening notepad")
            os.system('cmd /k "notepad"')
        except:
            speak("could not open")
    
    elif "write a note" in order:
        file=open("srishti.txt", 'w')
        speak("what should i write sir")
        note=get_command()
        speak("should i include date and time")
        yesno=get_command()
        if "yes" in yesno or "sure" in yesno:
            strTime = str(datetime.datetime.now().strftime("% H:% M:% S"))
            file.write(strTime)
            file.write(note)
            speak("done sir")
        else:
            file.write(note)
    elif "show note" in order:
            speak("Showing Notes")
            file = open("srishti.txt", "r")
            print(file.read())
            speak(file.read(5))
    elif "open" in order:
            index=order.find("open")
            order=order[index::]
            order=order.replace("open","")
            dest=order[1::]
            dest=dest+" "
            
            index2=dest.find(" ")
            dest=dest[:index2]
            
            link="https://www."+dest+".com"
            print(link)
            wb.open(link)
    
        
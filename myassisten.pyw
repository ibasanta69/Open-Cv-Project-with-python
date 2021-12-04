from math import e
import datetime as date
from os import startfile
from sys import path
import pyttsx3 as py
import speech_recognition as sp


def speak(audio):
    engine = py.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 140)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    print(audio)
    engine.runAndWait()


speak('hi')


def Wish_me():
    hour = int(date.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak('''Good Morning Sir !
               i 'am jarvis sir . please tell me know how can i help you..? 
        ''')
    elif hour >= 12 and hour <= 17:
        print('Good Afternoon Sir !')
        speak('Good Afternoon Sir !')
    elif hour > 17 and hour <= 21:
        print('Good Evening Sir !')
        speak('Good Evening Sir !')
    elif hour > 21 and hour <= 24:
        # speak('i am lucifer sir . please tell me know how can i help you..? ')
        #speak('Good Night have a you Nice Dream  Sir!')
        print()


def Listening():
    r = sp.Recognizer()
    with sp.Microphone() as source:
        print('Listening------')
        r.pause_threshold = 1.4
        audio = r.listen(source)
    try:
        print('Recognition------')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said{query}")
    except Exception as e:
        speak('Say That again please..?')
        return None
    return query

Wish_me()
while True:
    query = Listening('open')
    if "open youtube" in query:
        path = 'C:\\Users\\Death Empire\\Desktop\\Login\\home.pyw'
        startfile(path,'open')
    else:
        print('invalid')
        break

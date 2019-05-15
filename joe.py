#!/usr/bin/env python3

# this is made by iamharsh.dev
# you can buy me a coffee if you wants

import speech_recognition as sr #install using(pip install SpeechRecognition)
from time import ctime
import time
import os
import smtplib
from weather import Weather, Unit
import random
import wikipedia #install using (pip install wikipedia)
import wolframalpha #install using (pip install wolframalpha)
import webbrowser
import pyttsx3
import datetime
from gtts import gTTS

your_name = "Harsh" #replace harsh with your name
app_id = "8X6934-62AK2LTJPY" #replace with your wolframaplha app id
ai_name = "John"

client = wolframalpha.Client(app_id)

def speak(audio):
 print(audio)
 engine = pyttsx3.init()
 voices = engine.getProperty('voices')
 engine.say(audio)
 engine.runAndWait()


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
         speak("What can i do for you?")
         audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""

    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("I am still learning")
    except sr.RequestError as e:
        print("Could not request results from web; {0}".format(e))

    return data

#this is to greet you everytime you open this ai based on current timings
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH < 20:
        speak('Good Evening!')

    if currentH >= 20 and currentH !=0:  
        speak("Good Night!")  

greetMe() #calling the variable to return the values

def joe(data):

    if "how are you" in data:
        speak("I am fine")

    elif "open Google" in data:
        speak("yah i am trying")
        os.system("google-chrome www.google.com/")

    elif "open Gmail" in data:
        speak("yah i am trying")
        os.system("google-chrome www.gmail.com/")  

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on " + your_name + ", I will show you where " + location + " is.")
        os.system("google-chrome https://www.google.nl/maps/place/" + location)
 
    elif "what time is it" in data:
        speak(ctime())

    elif "what\'s up" in data or "how are you" in data:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(random.choice(stMsgs))

    elif "nothing" in data or "stop" in data or "bye" in data:
        speak("okay")
        speak("Bye Sir, have a good day")
        sys.exit()
           
    elif "hello" in data:
        speak("Hello Sir")

    elif "remember that" in data:
        data = data.split(" ")
        remember_text = data[2]
        speak("You told me to remember that" + remember_text)

    elif "what i told you to remember" in data:
        speak("You told me to remember that" + remember_text + ".")     

    else:
        data = data
        speak('Searching...')
        try:
            try:
                res = client.query(data)
                results = next(res.results).text
                speak('WOLFRAM-ALPHA says - ')
                speak('Got it.')
                speak(results)
                    
            except:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it.')
                speak('WIKIPEDIA says - ')
                speak(results)
        
        except:
            speak("Soemthing else " + your_name)
        
# initialization
time.sleep(2)
speak("Hey this is " + ai_name + " your personal Assistant how may i help you?")
while 1:
    data = recordAudio()
    joe(data)


import pyttsx3 
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from time import strftime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    h = int (datetime.datetime.now().hour)
    if h>=0 and h<12 :
     speak("Good morning sir!")
    elif h>=12 and h<=18 :
     speak("Good Afternoon sir!")
    else:
     speak("Good Evening sir!")

    speak("I am your Personal Assistant How May I help You")


def takeVoiceInput():
    #Takes microphone input from the user and convert ouput in string
    r = sr.Recognizer()
    #with sr.Recognizer(device_index = 1) as source:

    with sr.Microphone(device_index=1) as source:
        #r.adjust_for_ambient_noise(source)
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold = 4000
        audio = r.listen(source)
    try:
        '''
        with sr.Microphone() as source:
           r.adjust_for_ambient_noise(source)
           print('listening')
           voice = r.listen(source)
           info = r.recognize_google(voice)
           #print(info) 
           print("Recognizing...")
           '''
        print("Recognizing...")
        query = r.recognize_google(audio, english = 'en-in')
        print(f"User said..{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"    
    return query

if __name__ == "__main__":
    #speak("Aryaman is a good boy")
    wishMe()
    while True:

       query = takeVoiceInput().lower()
    #query = 'open vscode'
#Logic for executing tasks based on query:
    if 'wikipedia' in query:
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'open music' in query:
        music_dir = 'F:\\songs'
        songs = os.listdir(music_dir)
        lenOfList = len(songs)
        randomNumber = random.randint(0,lenOfList - 1)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[randomNumber]))
    
    elif 'the time' in query:
        #strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        hr = int(strftime("%H"))
        if hr>12:
            hr = str(hr-12)
        #strfTime = datetime.datetime.now().strftime("%H:%M:%S")  
        minu = strftime("%M")
        sec  = strftime("%S")
        speak(f"Sir, the time is {hr} hour, {minu} minutes and {sec} seconds")

    elif 'open vscode' in query:
        code_path = 'C:\\Users\\Aryaman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(code_path)   
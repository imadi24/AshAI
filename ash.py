from importlib.resources import path
from re import search
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am Ash sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "none"
    return query


def sendEmail(to,content):
    server = smtplib.smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.startttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('yourmail@gmail.com',to,content)
    server.close()
    

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = 'D:\\Non critical\\songs\\fav songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\adity\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'email to ash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nmare8408@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Ash bhai, your mail has not been sent!")
                
        elif 'what is ' in query:
            search = 'https://www.google.com/search?q='+query
            print("Here is what I found on the Internet..")
            speak("Searching... Here is what I found on the Internet.. ")
            webbrowser.open(search)
            
        elif 'bye' in query:
            print("Good bye sir, Have a nice day!!!")
            speak("Good bye sir, Have a nice day!!!")
            sys.exit()
            
        elif 'thank you' in query:
            print("you are welcome!")
            speak("You are welcome!")
            
        elif 'stop' in query:
            print("Good bye sir, Have a nice day!!!")
            speak("Good bye sir, Have a nice day!!!")
            
        
                
        
        
          
        
       
        
        

            

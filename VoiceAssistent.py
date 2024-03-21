import pyttsx3   # Text to speech conversion library
import speech_recognition as sr    # Allow computer to understand human language
import webbrowser       # to provides a high level interface to allow displaying web based documents to users
import datetime      
import pyjokes     
import os      # Provide functions for the interacting with the operating system
import time    

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Not Understand ")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speechtx("Good Morning!")

    elif hour>=12 and hour<18:
        speechtx("Good Afternoon!")   

    else:
        speechtx("Good Evening!")  

    speechtx("Hi Sir. Please tell me how may I help you") 

if __name__ == '__main__':
    wishMe()
     
    if "hi bro" in sptext().lower():
        while True :
            data1=sptext().lower()
            if "your name" in data1:
                name = " my name is sachin "
                speechtx(name)

            elif "old are you" in data1:
                age = " i am 5 days old "
                speechtx(age)

            elif "now time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif "open youtube" in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "facebook" in data1:
                webbrowser.open("https://www.facebook.com/")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtx(joke_1)

            elif "play song" in data1:
                add="E:\song"
                listsong = os.listdir(add)
                os.startfile(os.path.join(add,listsong[0]))

            elif "exit" in data1:
                speechtx("thank you")
                break

            time.sleep(10)

    else:
        print(" thanks ")

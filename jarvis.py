import pyttsx3   #pip install pyttsx3
import datetime
import speech_recognition as sr   #pip install speechRecognition
import wikipedia   #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!") 

    speak("I am Jarvis sir. Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold=200
        audio= r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-IN')
        print(f"User said: {query}\n")

    except Exception :
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    #Here give the location of text file in which password of your email Id is kept.
    f=open(r"Location","r")
    password=f.read()
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Sender@email',password) #give th email of the sender.
    server.sendmail('Sender@email',to,content) #give the email of the sender.
    server.close()
    f.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query =takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
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
            music_dir='D:\\Songs'  #Location where songs are kept.
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        
        elif 'code' in query:
            os.startfile("Location/of/VS Code.exe/file") #location of VS Code.

        elif 'email' in query:
            try:
                speak("What should I say?")
                content= takeCommand()
                #give your email.id in to
                to = "@email"  #give email address to whom email has to be sent.
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email") 

        elif 'exit' or 'bye' in query:
            break           




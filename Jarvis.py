import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import datetime
import cv2


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:

        speak("Say that again please...")
        return "None"
    return query


def wishme():

    hour = int(datetime.datetime.now().hour)
    if 12 > hour >= 0:
        speak("Good Morning Sir")

    elif 18 > hour >= 12:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Jarvis. Please tell me how may I help you")


wishme()

query = takecommand().lower()

if "sleep" or "shutdown" in query.lower:
    run = False

elif "open notepad" in query.lower:
    npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"
    speak("Okay")
    os.startfile(npath)

elif "open command prompt" in query.lower:
    speak("Sure")
    os.system("start cmd")

elif "open camera" in query.lower:
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(50)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

elif "play music" or "play songs" in query.lower:
    music_dirc = "C:\\Users\\kaush\\Desktop\\SOUND"
    songs = os.listdir(music_dirc)
    os.startfile(os.path.join(music_dirc, songs[1]))

elif "sleep" or "shutdown" in query.lower():
    run = False
    quit()

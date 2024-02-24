if 'wikipedia' in query:
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

elif 'open youtube' in query:
    webbrowser.open("youtube.com")

elif 'open google' in query:
    webbrowser.open("google.com")

elif 'open stackoverflow' in query:
    webbrowser.open("stackoverflow.com")

elif 'play music' in query:
    music_dir = 'path here'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))

elif 'time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"Sir, the time is {strTime}")

elif 'open code' in query:
    codePath = "path here"
    os.startfile(codePath)

elif 'email to kaushik' in query:
    try:
        speak("What should I write?")
        content = takeCommand()
        to = "kaushik.dudhade@gmail.com"
        sendemail(to, content)
        speak("Email has been sent!, Sir.")
    except Exception as e:
        print(e)
        speak("Sorry. I am not able to send this email")

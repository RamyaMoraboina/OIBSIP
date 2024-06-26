import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
# import setuptools

# import pyaudio


engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Godd Afternoon")
    else:
        speak("good Evening")
    speak("I am spandy Mam,please tell me how may help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("say that again please")
        return None
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences =2)
            speak('According wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        # elif 'play music' in query:
        #     music_dir = 'c:\\users\\apple\\music'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam the time is {strTime}")
        # elif 'open code' in query:
        #     codepath = 'c:\\users\\apple\\Desktop\ReactTutorial\my-app\src\formExercise2.jsx'
        #     os.startfile(codepath)

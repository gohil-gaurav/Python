import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):

    engine.say(text)
    engine.runAndWait()

def proceesCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswitch("play"):
        song = c.lower().split(" ")[1]
        link = musiclib.music[song]
        webbrowser.open(link)

if __name__ == '__main__':
    speak("Initializing Jarvis...")

    while True:

        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "hello"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    proceesCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

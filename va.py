import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand")
        return ""

speak("Voice assistant started")

while True:
    command = take_command()

    if "hello" in command:
        speak("Hello, how can I help you")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("Current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "search" in command:
        speak("What should I search?")
        query = take_command()
        webbrowser.open("https://www.google.com/search?q=" + query)

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)

        return command.lower()

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""

    except sr.RequestError:
        print("Speech recognition service unavailable. Check internet connection.")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""

# Welcome message
speak("Voice Assistant Started")

while True:
    command = take_command()

    if not command:
        continue

    if "hello" in command:
        speak("Hello, how can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        speak("What should I search for?")
        query = take_command()

        if query:
            speak(f"Searching for {query}")
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I don't know that command yet.")
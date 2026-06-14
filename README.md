# Voice Assistant using Python

## Project Description

The Voice Assistant is a Python-based application that listens to voice commands and performs basic tasks such as greeting the user, telling the current time and date, searching the web, and exiting the application. It uses speech recognition for voice input and text-to-speech technology for voice responses.

This project demonstrates the integration of speech recognition, voice synthesis, and task automation in Python.

## Features

* Voice command recognition
* Text-to-speech responses
* Greeting functionality
* Current time announcement
* Current date announcement
* Google search through voice commands
* Exit command to stop the assistant

## Technologies Used

* Python 3
* SpeechRecognition
* pyttsx3
* datetime
* webbrowser

## Project Structure

```text
Voice-Assistant/
│
├── voice_assistant.py
└── README.md
```

## Required Libraries

Install the required packages:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install PyAudio
```

## How to Run

### Step 1: Install Dependencies

Install all required Python libraries.

### Step 2: Connect a Microphone

Ensure your system has a working microphone.

### Step 3: Run the Program

```bash
python voice_assistant.py
```

## Available Commands

| Command     | Action                 |
| ----------- | ---------------------- |
| Hello       | Greets the user        |
| Time        | Tells the current time |
| Date        | Tells the current date |
| Search      | Opens a Google search  |
| Exit / Stop | Closes the assistant   |

## Example Usage

```text
Listening...
You said: hello

Assistant: Hello, how can I help you

Listening...
You said: what is the time

Assistant: Current time is 10:30
```

## How It Works

1. The assistant listens through the microphone.
2. Speech is converted into text using Google Speech Recognition.
3. The command is processed.
4. The assistant responds using text-to-speech.
5. Specific commands trigger predefined actions.

## Key Concepts Used

* Speech Recognition
* Text-to-Speech (TTS)
* Voice-Based Interaction
* Task Automation
* Exception Handling
* Web Integration

## Error Handling

The application handles situations where:

* Speech is not recognized.
* The microphone input is unclear.
* Invalid commands are given.

## Future Enhancements

* Weather updates
* Reminder system
* Email sending functionality
* Calculator commands
* AI-powered conversation
* GUI interface using Tkinter
* Integration with external APIs

## Learning Outcomes

Through this project, I learned:

* How speech recognition works
* How text-to-speech systems are implemented
* How to automate tasks using voice commands
* How to interact with web services through Python
* How to build user-friendly voice applications

## Author

Gokulnath S

Python Programming Internship Project

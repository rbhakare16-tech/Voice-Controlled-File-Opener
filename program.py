import speech_recognition as sr
import pyttsx3
import os

# Voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech recognition
listener = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    speak("Which folder do you want to open?")
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower()
    print("You said:", command)

# Conditions
if "documents" in command:
    os.startfile("C:\\Users\\dell\\Documents")
    speak("Opening Documents folder")

elif "downloads" in command:
    os.startfile("C:\\Users\\dell\\Downloads")
    speak("Opening Downloads folder")

elif "chrome" in command:
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    speak("Opening Chrome")

else:
    speak("Folder not found")
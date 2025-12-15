# main.py
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()  # create a fresh engine every time
    engine.say(text)
    engine.runAndWait()


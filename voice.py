import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):

    print("Jarvis:",text)

    engine.say(text)
    engine.runAndWait()

def listen():

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        print("You:",text)

        return text.lower()

    except:
        return ""
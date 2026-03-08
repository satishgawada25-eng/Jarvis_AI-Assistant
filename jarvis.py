import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import pyautogui
import datetime
import wikipedia
import os

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

def ask_ai(prompt):

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        return result["response"]

    except:
        return "AI brain is not running. Please start Ollama."

def run_command(command):

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    if "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    if "time" in command:
        return datetime.datetime.now().strftime("The time is %H:%M")

    if "screenshot" in command:
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        return "Screenshot saved"

    if "shutdown computer" in command:
        os.system("shutdown /s /t 5")
        return "Shutting down computer"

    return None


def search_wikipedia(query):

    try:
        return wikipedia.summary(query, sentences=2)

    except:
        return "I could not find information."


def jarvis():

    speak("Hello, I am Jarvis. How can I help you?")

    while True:

        command = listen()

        if command == "":
            continue

        if "exit" in command:
            speak("Goodbye")
            break

        automation = run_command(command)

        if automation:
            speak(automation)
            continue

        if "search" in command:

            query = command.replace("search", "")

            result = search_wikipedia(query)

            speak(result)

            continue

        answer = ask_ai(command)

        speak(answer)


jarvis()
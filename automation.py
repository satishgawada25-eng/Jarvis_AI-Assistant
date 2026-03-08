import webbrowser
import pyautogui
import os
import datetime

def run(command):

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    if "open chrome" in command:
        os.system("start chrome")
        return "Opening Chrome"

    if "time" in command:
        return datetime.datetime.now().strftime("%H:%M")

    if "screenshot" in command:
        img = pyautogui.screenshot()
        img.save("screen.png")
        return "Screenshot saved"

    return None
import os
import speech_recognition as sr
import pyttsx3
import tkinter as tk

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the rate of speech
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

while True:
    # Listen for the user's command
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Try to recognize the command
    try:
        command = r.recognize_google(audio).lower()
        print("Commanded: " + command)

        # Check if the command matches a predefined set of commands
        if "open chrome" in command:
            engine.say("Opening Google Chrome")
            engine.runAndWait()
            os.system("start chrome")
        elif "volume up" in command:
            engine.say("Turning up the volume")
            engine.runAndWait()
            os.system("nircmd.exe setsysvolume 65535")
        elif "volume down" in command:
            engine.say("Turning down the volume")
            engine.runAndWait()
            os.system("nircmd.exe setsysvolume 0")
        elif "lock" in command:
            engine.say("Locking the PC")
            engine.runAndWait()
            os.system("nircmd.exe monitor off")
        elif "open calculator" in  command:
            engine.say("Opening Calculator")
            engine.runAndWait()
            os.system("start calc")
        elif "open notepad" in  command:
            engine.say("Opening Notepad")
            engine.runAndWait()
            os.system("start notepad")
        elif "open camera" in  command:
            engine.say("Opening Camera")
            engine.runAndWait()
            os.system("start microsoft.windows.camera:")
        elif "capture screenshot" in  command:
            engine.say("Opening Snipping Tool")
            engine.runAndWait()
            os.system("start snippingtool")
        elif "open excel" in  command:
            engine.say("Opening Microsoft Excel")
            engine.runAndWait()
            os.system("start excel")
        elif "open word" in  command:
            engine.say("Opening Microsoft Word")
            engine.runAndWait()
            os.system("start winword")
        elif "open powerpoint" in  command:
            engine.say("Opening Microsoft PowerPoint")
            engine.runAndWait()
            os.system("start powerpnt")
        elif "open calender" in  command:
            engine.say("Opening Calender")
            engine.runAndWait()
            os.system("start outlookcal:")
        elif "open watch" in  command:
            engine.say("Opening Alarms & Clock")
            engine.runAndWait()
            os.system("start ms-clock:")
        elif "display available networks" in  command:
            engine.say("Displaying Available Networks")
            engine.runAndWait()
            os.system("start ms-availablenetworks:")
        elif "open mail" in  command:
            engine.say("Opening Mail")
            engine.runAndWait()
            os.system("start outlookmail:")
        elif "open store" in  command:
            engine.say("Opening Microsoft Store")
            engine.runAndWait()
            os.system("start ms-windows-store:")
        elif "open photos" in  command:
            engine.say("Opening Photos")
            engine.runAndWait()
            os.system("start ms-photos:")
        elif "open settings" in  command:
            engine.say("Opening Settings")
            engine.runAndWait()
            os.system("start ms-settings:")
        elif "open security" in  command:
            engine.say("Opening Security Service")
            engine.runAndWait()
            os.system("start windowsdefender:")
        elif "stop" in command:
            break
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

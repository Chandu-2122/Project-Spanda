import datetime
import os
import pyttsx3
import speech_recognition as sr
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import traceback
import sys
import time
import pyjokes
import pyautogui
import pygetwindow as gw

#defaulting webbrowser to brave
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))

#function to generate speech from text
def speak(text):
    """
    Converts the given text to speech using a fresh engine instance.

    Parameters:
        text (str): Text to speak.

    Returns:
        None
    """
    engine = pyttsx3.init('sapi5')  # fresh instance
    engine.setProperty('rate', 250)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 1 for female, 0 for male

    print(text)
    engine.say(text)
    engine.runAndWait()

#function to greet
def wish():
    """
        Greets the user based on the current time of day (morning, afternoon, or evening)
        and introduces the assistant.

        Returns:
            None
        """
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        greeting = "Good Morning C"
    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon C"
    else:
        greeting = "Good Evening C"

    full_message = f" It's {tt}, {greeting}. I am Project Spanda. Please tell me how may I help you now."
    speak(full_message)

#function to generate text from speech
def takecommand():
    """
    Listens to audio input from the microphone and attempts to convert it to text
    using Google's speech recognition API.

    Returns:
        str: The recognized text as a string. Returns 'None' if recognition fails.

    Raises:
        sr.WaitTimeoutError: If no speech is detected within the timeout.
        sr.UnknownValueError: If the speech is unintelligible.
        sr.RequestError: If there is an issue with the Google API request.
    """
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)#, timeout=4, phrase_time_limit=8)

    try:
        print("Recognizing...")
        #google sr works with internet connection
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query)
    except sr.UnknownValueError:
        speak("I didn't understand.")
        return "None"
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the speech service.")
        return "None"
    return query

#plays first youtube video from search results
def play_first_youtube_video(search_query):
    speak(f"Searching YouTube for {search_query}")
    try:
        speak(f"Playing {search_query} on YouTube...")
        kit.playonyt(search_query)
    except Exception as e:
        speak("Something went wrong while opening YouTube.")
        print("Error:", e)

#closing opened applications
def close_application(app_name):
    """
    Closes an application using its process name.
    Examples: 'notepad.exe', 'cmd.exe'
    """
    try:
        os.system(f"taskkill /f /im {app_name}")
        speak(f"Closed {app_name.replace('.exe', '')}")
    except Exception as e:
        speak("Couldn't close the application.")
        print("Error:", e)


if __name__ == '__main__':
    wish()
    while True:
        if 1:
            #take the command from user
            query = takecommand().lower()
            #logic to perform tasks
            if "open notepad" in query:
                path = "C:\\Windows\\System32\\notepad.exe"
                speak("Opening notepad...")
                os.startfile(path)
            elif "open command prompt" in query or "open cmd" in query:
                speak("Opening Command prompt...")
                os.system("start cmd")
            elif "open camera" in query:
                speak("Opening camera...")
                cap = cv2.VideoCapture(0) #0 for internal camera use and 1 for external
                while True:
                    ret, img = cap.read()
                    if not ret:
                        speak("Failed to access the camera.")
                        break
                    cv2.imshow('WebCam', img)
                    k = cv2.waitKey(1) #stores the ASCII code of the key that was pressed during the wait. If no key is pressed, '-1' will be stored in k.
                    if k == 27: #ASCII code of 'esc' = 27
                        break #if 'esc' key is pressed
                cap.release()
                cv2.destroyAllWindows()
            elif "play music" in query:
                music_dir = ""
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                for song in songs:
                    if song.endswith(".mp3"):
                        os.startfile(os.path.join(music_dir, song))
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak("Your IP address is " + ip)
            elif "wikipedia" in query:
                query = query.lower()
                for phrase in ["what is", "who is", "tell me about", "tell me what you know about", "tell me what do you know about", "what do you know about", "what you know about", "search about", "search on", "define", "according to", "based on", "describe", "on wikipedia", "in wikipedia", "from wikipedia", "with wikipedia", "wikipedia"]:
                    query = query.replace(phrase, "")
                query = query.strip()
                speak(f"Searching about {query} on Wikipedia...")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
                    print(results)
                    # Get the page and open in browser
                    page = wikipedia.page(query)
                    speak("To know more, I’ve opened the full Wikipedia page for you.")
                    webbrowser.get('brave').open(page.url)
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("Your query is too broad. Please be more specific.")
                    print(f"Disambiguation error: {e}")
                except wikipedia.exceptions.PageError:
                    speak("I couldn't find anything on Wikipedia for that topic.")
                except Exception as e:
                    speak("Something went wrong while searching Wikipedia.")
                    print(e)
            elif "open youtube" in query:
                speak("Opening youtube...")
                speak("C, what do you wanna play in youtube?")
                cm = takecommand().lower()
                if cm != "none":
                    try:
                        play_first_youtube_video(cm)
                    except Exception as e:
                        print("Exception occurred:")
                        traceback.print_exc()
            elif "open google" in query:
                speak("Opening google...")
                webbrowser.get('brave').open("google.com")
            elif "open linkedin" in query:
                speak("Opening linkedin...")
                webbrowser.get('brave').open("linkedin.com")
            elif "open github" in query:
                speak("Opening github...")
                webbrowser.get('brave').open("github.com")
            elif "close notepad" in query:
                close_application("notepad.exe")
            elif "close command prompt" in query or "close cmd" in query:
                close_application("cmd.exe")
            elif "close browser" in query:
                # Choose the browser you use
                close_application("brave.exe")  # or "chrome.exe", "firefox.exe"
            #elif "set alarm" in query:
            elif "tell me a joke" in query or "tell a joke" in query:
                joke = pyjokes.get_joke(language="en")
                speak(joke)
            elif "switch the window" in query or "switch window" in query:
                speak("Switching the window...")
                pyautogui.hotkey("alt", "tab")
            elif "show opened windows" in query or "show windows" in query:
                speak("Showing opened windows...")
                pyautogui.hotkey("win", "tab")
                while True:
                    command = takecommand().lower()
                    if "next" in command:
                        pyautogui.press("right")
                    elif "back" in command:
                        pyautogui.press("left")
                    elif "enter" in command:
                        pyautogui.press("enter")
                        break
                    elif "cancel" in command or "exit" in command:
                        pyautogui.press("esc")
                        speak("Exited Task View.")
                        break
            elif "go to desktop" in query:
                speak("Going to desktop...")
                pyautogui.hotkey("win", "d")
            elif "lock the screen" in query or "lock the system" in query:
                speak("Locking the screen...")
                os.system("rundll32.exe user32.dll,LockWorkStation")
            elif "go to next tab" in query or "switch to next tab" in query or "next tab" in query:
                speak("Switching to next tab...")
                pyautogui.hotkey("ctrl", "tab")
                time.sleep(1)  # Wait for tab to switch
                # Get the title of the active window
                active_window = gw.getActiveWindow()
                if active_window:
                    title = active_window.title
                    if title.strip():
                        speak(f"You are now on: {title} tab")
                    else:
                        speak("I switched the tab, but couldn't detect the title.")
                else:
                    speak("I switched the tab, but couldn't detect the window.")
            elif "go to previous tab" in query or "switch to previous tab" in query or "previous tab" in query:
                speak("Switching to previous tab...")
                pyautogui.hotkey("ctrl","shift", "tab")
                time.sleep(1)  # Wait for tab to switch
                # Get the title of the active window
                active_window = gw.getActiveWindow()
                if active_window:
                    title = active_window.title
                    if title.strip():
                        speak(f"You are now on: {title} tab")
                    else:
                        speak("I switched the tab, but couldn't detect the title.")
                else:
                    speak("I switched the tab, but couldn't detect the window.")
            elif "close current tab" in query or "close the current tab" in query or "current tab" in query:
                active_window = gw.getActiveWindow()
                if active_window:
                    title = active_window.title
                    if title.strip():
                        speak(f"Closing: {title} tab")
                        pyautogui.hotkey("ctrl", "w")
                else:
                    speak("Couldn't detect an active window.")
            elif "pause the video" in query or "pause video" in query:
                speak("Pausing the video...")
                pyautogui.press("k")
            elif "play the video" in query or "play video" in query:
                speak("Playing the video...")
                pyautogui.press("k")
            elif "mute the video" in query or "mute video" in query:
                speak("Muting the video...")
                pyautogui.press('m')
            elif "unmute the video" in query or "unmute video" in query:
                speak("Unmuting the video...")
                pyautogui.press('m')
            elif "full screen" in query:
                speak("Fullscreening the video...")
                pyautogui.press("f")
            elif "exit fullscreen" in query:
                speak("Exiting fullscreen...")
                pyautogui.press("esc")
            elif "shutdown the system" in query:
                speak("Shutting down the system...")
                os.system("shutdown /s")
            elif "restart" in query:
                speak("Restarting the system...")
                os.system("shutdown /r")

            elif any(phrase in query for phrase in ["bye", "quit", "exit", "leave"]):
                speak("Okay, Goodbye! Have a great day C.")
                sys.exit()
            time.sleep(0.5)
            speak("Do you want any other help, C?")
    #takecommand()
    #speak("Hello")
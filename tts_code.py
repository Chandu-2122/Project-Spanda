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
import sys, subprocess
import time
import pyjokes
import pyautogui
import pygetwindow as gw
from newsapi import NewsApiClient
import requests


# OLLAMA CONFIG
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:latest"

#defaulting webbrowser to brave
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))


def speak(text, rate=250, volume=1.0, voice_id=1):
    """
    Converts the given text to speech using a fresh engine instance, with optional custom rate, volume, and voice.

    Parameters:
        text (str): Text to speak.
        rate (int, optional): The speed at which the speech is spoken. Default is 250.
        volume (float, optional): The volume of the speech. Default is 1.0 (max volume).
        voice_id (int, optional): The index of the voice. Default is 1 for female. Use 0 for male.

    Returns:
        None
    """
    # Initialize the speech engine
    engine = pyttsx3.init('sapi5')  # fresh instance
    # Set properties
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    # Get available voices
    voices = engine.getProperty('voices')
    # Set the desired voice
    if 0 <= voice_id < len(voices):  # Check if the voice_id is valid
        engine.setProperty('voice', voices[voice_id].id)
    else:
        print("Invalid voice_id. Using default voice.")
        engine.setProperty('voice', voices[1].id)  # Default to female if invalid
    # Print and speak the text
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
def takecommand(timeout=5, phrase_time_limit=8, silent=False):
    """
    Listens to microphone input and returns recognized text.

    Parameters:
        timeout (int, optional): Seconds to wait for phrase start.
        phrase_time_limit (int, optional): The maximum length of time (in seconds) for a single phrase. Default is 8 seconds.
        silent (bool, optional): If True, suppresses error messages and the "Listening..." prompt. Default is False.

    Returns:
        str: Recognized speech or 'None' if no speech was detected.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if not silent:
            print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            if not silent:
                print("No speech detected.")
            return "None"
    try:
        if not silent:
            print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        return query
    except sr.UnknownValueError:
        if not silent:
            speak("I didn't understand.")
        return "None"
    except sr.RequestError:
        if not silent:
            speak("Sorry, I'm having trouble connecting to the speech service.")
        return "None"

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

#fetch and latest news
def news():
    """
       Fetches the latest news headlines and reads them aloud using text-to-speech.
       It listens for commands such as "stop" to stop reading, and "expand" or "read it" to read more details of an article.

       Parameters:
           None

       Returns:
           None

       Behavior:
           - Reads the title of each news article aloud.
           - After each title, listens for user commands to:
             - "stop" or "exit": Stops the news reading.
             - "expand", "read it", or "tell me more": Expands to read the description of the article.
             - Moves to the next article if no valid command is heard.
       """
    # Initialize News API with your API Key
    newsapi = NewsApiClient(api_key='781c4793a02d484d809e8e430a78e0a4')
    # Get the latest headlines
    top_headlines = newsapi.get_top_headlines(language='en')
    print(f"Number of news articles: {len(top_headlines['articles'])}")
    # Print the headlines

    for article in top_headlines['articles']:
        print("----")
        speak(text = article['title'],rate=200, volume=1.0, voice_id=0)
        # While speaking, listen for commands or keywords
        command = takecommand(timeout=4, phrase_time_limit=4, silent=True).lower()
        # Stop reading if "stop" is detected
        if command and ("stop" in command or "exit" in command):
            speak("Stopping reading...")
            break
        # Listen for keywords and read the description of the relevant article
        elif command and ("read it" in command or "tell me more" in command or "expand" in command):
            speak(text="okay", rate=200, volume=1.0, voice_id=0)
            description = article.get('description', "No description available.")
            speak(text = description, rate=200, volume=1.0, voice_id=0)
        elif command and ("next" in command or "what's next" in command or "skip" in command):
            continue
        speak(text="next", rate=200, volume=1.0, voice_id=0)

#Generate reply using Ollama LLM


WAKE_WORDS = ["hey spanda", "wake up", "spanda", "hey", "are you there", "bro", "dude"]
SLEEP_WORDS = ["sleep now", "go to sleep", "be quiet", "just wait", "wait"]
def ask_llama(prompt):
    try:
        system_prompt = (
            "You are Project Spanda. Your job is to make the user be conscious about himself/herself."
            "Whatever is asked answer briefly and clearly and do not mention that you are an AI."
        )
        payload = { 
            "model": OLLAMA_MODEL, 
            "prompt": f"{system_prompt}\nUser: {prompt}\nAssistant:", 
            "temperature": 0.7, 
            "stream": False 
            }
        response = requests.post(OLLAMA_URL, json=payload, timeout=60) 
        return response.json().get("response", "I couldn't think of an answer.") 
    except Exception as e: 
        print("LLM Error:", e) 
    return "Sorry, I'm having trouble thinking right now."


if __name__ == '__main__':
    wish()
    is_awake = True  # Start awake

    while True:
        if is_awake:
            #take the command from user
            query = takecommand().lower()
            if any(phrase in query for phrase in SLEEP_WORDS):
                speak("Okay, I am going to sleep. Just say 'Hey Spanda' to wake me up.")
                is_awake = False
                continue
            #logic to perform tasks
            elif "open notepad" in query:
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
            elif "news" in query:
                speak("Fetching the latest news, please wait...")
                news()
            elif "screenshot" in query:
                speak("What do you want the screenshot to be saved as...")
                filename = takecommand().lower()
                # If the user didn't specify a filename, generate one based on the current timestamp
                if filename == "none" or filename == "None" or filename == "":  # In case of no user input
                    filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Example: 2025-10-14_13-45-30.png
                speak("Taking screenshot, don't move and please wait...")
                ss = pyautogui.screenshot()
                ss.save(f"{filename}.png")
                speak(f"Screenshot saved as {filename}.png")
            elif "shutdown the system" in query or "shut down" in query:
                speak("Shutting down the system...")
                os.system("shutdown /s")
            elif "restart" in query:
                speak("Restarting the system...")
                os.system("shutdown /r")
            elif any(phrase in query for phrase in ["bye", "quit", "exit", "leave"]):
                speak("Okay, Goodbye! Have a great day C.")
                sys.exit()

            # LLM FALLBACK
            else:
                speak("Let me think...")
                response = ask_llama(query)
                speak(response)

        else:
            print("Sleeping... Waiting for wake word.")
            query = takecommand(timeout=4, silent=True).lower()

            if query == "none":
                continue  # nothing said, just keep waiting quietly

            if any(wake_word in query for wake_word in WAKE_WORDS):
                speak("Yes C, I am listening...")
                is_awake = True

#takecommand()
    #speak("Hello")
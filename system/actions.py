# system/actions.py

from newsapi import NewsApiClient
from system.speech import *
from config import BRAVE_PATH

import os
import webbrowser
import pyautogui
import pyjokes
import pywhatkit as kit
import pygetwindow as gw

# Register Brave browser
webbrowser.register(
    "brave", None, webbrowser.BackgroundBrowser(BRAVE_PATH)
)

def open_youtube() -> None:
    """
    Plays the first YouTube result for a given search query.

    Returns:
        None
    """
    speak("Opening youtube...")
    speak("C, what do you wanna play in youtube?")
    cm = take_command().lower()
    speak(f"Searching YouTube for {cm}")
    try:
        speak(f"Playing {cm} on YouTube...")
        kit.playonyt(cm)
    except Exception as e:
        speak("Something went wrong while opening YouTube.")
        print("Error:", e)

def close_application(app_name: str) -> None:

    """
    Force close an application using its process name.

    Args:
        app_name (str): Executable name (e.g., 'notepad.exe').
    Returns:
        None
    """
    try:
        os.system(f"taskkill /f /im {app_name}")
        speak(f"Closed {app_name.replace('.exe', '')}")
    except Exception as e:
        speak("Couldn't close the application.")
        print("Error:", e)

def tell_joke() -> None:
    """
    Speaks a random joke.

    Returns:
        None
    """
    speak(pyjokes.get_joke())

def take_screenshot() -> None:
    """
    Takes a screenshot and saves it to disk.

    Returns:
        None
    """
    speak("What do you want the screenshot to be saved as...")
    filename = take_command().lower()
    # If the user didn't specify a filename, generate one based on the current timestamp
    if filename == "none" or filename == "None" or filename == "":  # In case of no user input
        filename = datetime.datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S")  # Example: 2025-10-14_13-45-30.png
    speak("Taking screenshot, don't move and please wait...")
    ss = pyautogui.screenshot()
    ss.save(f"{filename}.png")
    speak(f"Screenshot saved as {filename}.png")

def next_tab() -> None:
    """
    Switches to the next tab in the current window.

    Returns:
        None
    """
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

def previous_tab() -> None:
    """
    Switches to the previous tab in the current window.

    Returns:
        None
    """
    speak("Switching to previous tab...")
    pyautogui.hotkey("ctrl", "shift", "tab")
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

def close_tab() -> None:
    """
    Closes the current tab in the current window.

    Returns:
        None
    """
    active_window = gw.getActiveWindow()
    if active_window:
        title = active_window.title
        if title.strip():
            speak(f"Closing: {title} tab")
            pyautogui.hotkey("ctrl", "w")
    else:
        speak("Couldn't detect an active window.")

def pause_video() -> None:
    """
    Pauses the video.

    Returns:
        None
    """
    speak("Pausing the video...")
    pyautogui.press("k")

def play_video() -> None:
    """
    Plays the video.

    Returns:
        None
    """
    speak("Playing the video...")
    pyautogui.press("k")

def mute_video() -> None:
    """
    Mutes the video.

    Returns:
        None
    """
    pyautogui.press('m')

def fullscreen() -> None:
    """
    Fullscreens the video.

    Returns:
        None
    """
    pyautogui.press("f")

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
    speak("Fetching the latest news, please wait...")
    # Initialize News API with your API Key
    newsapi = NewsApiClient(api_key='781c4793a02d484d809e8e430a78e0a4')
    # Get the latest headlines
    top_headlines = newsapi.get_top_headlines(language='en')
    print(f"Number of news articles: {len(top_headlines['articles'])}")
    # Print the headlines

    for article in top_headlines['articles']:
        print("----")
        speak(text = article['title'])
        # While speaking, listen for commands or keywords
        command = take_command(timeout=4, phrase_time_limit=4, silent=True).lower()
        # Stop reading if "stop" is detected
        if command and ("stop" in command or "exit" in command):
            speak("Stopping reading...")
            break
        # Listen for keywords and read the description of the relevant article
        elif command and ("read it" in command or "tell me more" in command or "expand" in command):
            speak(text="okay")
            description = article.get('description', "No description available.")
            speak(text = description)
        elif command and ("next" in command or "what's next" in command or "skip" in command):
            continue
        speak(text="next")

def shutdown() -> None:
    """
    Shuts down the system immediately.

    Returns:
        None
    """
    speak("Shutting down the system")
    os.system("shutdown /s")

def restart() -> None:
    """
    Restarts the system immediately.

    Returns:
        None
    """
    speak("Restarting the system")
    os.system("shutdown /r")

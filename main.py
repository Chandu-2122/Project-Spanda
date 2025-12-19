# main.py

from config import *
from system.actions import *
from llm.ollama import *
from memory.chat_memory import *

import sys

memory = ChatMemory()
awake = True

def main():
    """
    Main event loop for Project Spanda.

    Responsibilities:
    - Handle wake / sleep state
    - Route commands to system actions
    - Use LLM as a fallback
    - Store conversational memory
    """
    global awake
    wish()

    is_awake = True  # Start awake
    while True:
        if is_awake:
            # take the command from user
            query = take_command().lower()
            if query == "none":
                continue
            elif any(phrase in query for phrase in SLEEP_WORDS):
                speak("Okay, I am going to sleep. Just say 'Hey Spanda' to wake me up.")
                is_awake = False
                continue
            # logic to perform tasks
            elif "open youtube" in query:
                open_youtube()
            elif "close browser" in query:
                close_application("brave.exe")  # or "chrome.exe", "firefox.exe"
            elif "tell me a joke" in query or "tell a joke" in query:
                tell_joke()
            elif "go to next tab" in query or "switch to next tab" in query or "next tab" in query:
                next_tab()
            elif "go to previous tab" in query or "switch to previous tab" in query or "previous tab" in query:
                previous_tab()
            elif "close current tab" in query or "close the current tab" in query or "current tab" in query:
                close_tab()
            elif "pause the video" in query or "pause video" in query:
                pause_video()
            elif "play the video" in query or "play video" in query:
                play_video()
            elif "mute the video" in query or "mute video" in query or "unmute" in query:
                mute_video()
            elif "full screen" in query or "exit fullscreen" in query:
                fullscreen()
            elif "news" in query:
                news()
            elif "screenshot" in query:
                take_screenshot()
            elif "shutdown the system" in query or "shut down" in query:
                shutdown()
            elif "restart" in query:
                restart()
            elif any(phrase in query for phrase in ["bye", "quit", "exit", "leave"]):
                speak("Okay, Goodbye! Have a great day C.")
                sys.exit()

            # LLM FALLBACK
            else:
               speak("Let me think...")
               response = ask(query)
               speak(response)

        else:
            print("Sleeping... Waiting for wake word.")
            query = take_command(timeout=4, silent=True).lower()

            if query == "none":
                continue  # nothing said, just keep waiting quietly

            if any(wake_word in query for wake_word in WAKE_WORDS):
                speak("Yes C, I am listening...")
                is_awake = True


if __name__ == "__main__":
    main()

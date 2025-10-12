import datetime
import os
import pyttsx3
import speech_recognition as sr
import cv2
import random
import requests
import wikipedia
import webbrowser
import pywhatkit
import traceback
import sys

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
    if hour >= 0 and hour < 12:
        greeting = "Good Morning C"
    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon C"
    else:
        greeting = "Good Evening C"

    full_message = f"{greeting}. I am Project Spanda. Please tell me how may I help you now."
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
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

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
        import pywhatkit as kit
        kit.playonyt(search_query)
    except Exception as e:
        speak("Something went wrong while opening YouTube.")
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



            elif any(phrase in query for phrase in ["bye", "quit", "exit", "leave"]):
                speak("Okay, Goodbye! Have a great day C.")
                sys.exit()
            speak("Do you want any other help, C?")
    #takecommand()
    #speak("Hello")
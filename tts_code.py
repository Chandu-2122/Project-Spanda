import datetime
import os
import time
import pyttsx3
import speech_recognition as sr
import os

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
        speak("I didn't catch that. Please say it again.")
        return "None"
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the speech service.")
        return "None"
    return query

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
                os.system("start camera")

            elif any(phrase in query for phrase in ["bye", "quit", "exit", "leave"]):
                speak("Okay, Goodbye! Have a great day C.")
                break
    #takecommand()
    #speak("Hello")
#system\speech.py

import datetime, time
import pyttsx3
import speech_recognition as sr
from config import VOICE_RATE, VOICE_VOLUME, VOICE_ID


#function to speak
def speak(text):
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
    engine.setProperty('rate', VOICE_RATE)
    engine.setProperty('volume', VOICE_VOLUME)
    # Get available voices
    voices = engine.getProperty('voices')
    # Set the desired voice
    engine.setProperty("voice", voices[VOICE_ID].id)
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
def take_command(timeout=5, phrase_time_limit=8, silent=False):
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
    try:
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
            return ""
    except OSError:
        speak("Microphone is not available.")
        return "None"

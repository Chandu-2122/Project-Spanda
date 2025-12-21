# system/voice_flow.py

from system.speech import speak, take_command
import time

def reflective_speak(text, pause_after=1.0):
    """
    Slower, gentler speech for reflection mode.
    """
    speak(text)
    time.sleep(pause_after)

def reflective_listen(prompt=None, timeout=10, max_retries=2):
    """
    Slower listening window for self-reflection, with retries on no recognition.
    After max_retries, returns empty string to allow normal LLM fallback.

    Args:
        prompt (str): Optional prompt to speak before listening.
        timeout (int): Seconds to wait for speech.
        max_retries (int): Number of times to ask again if nothing is recognized.

    Returns:
        str: User response, empty string if no valid response after retries
    """
    from system.voice_flow import reflective_speak
    from system.speech import take_command

    retries = 0
    while retries <= max_retries:
        if prompt and retries == 0:
            reflective_speak(prompt)

        response = take_command(timeout=timeout, phrase_time_limit=12)
        response = (response or "").strip()  # normalize None to empty string

        if response and response.lower() != "none":
            return response  # valid response received

        # No valid response, retry
        retries += 1
        if retries <= max_retries:
            reflective_speak("Could you repeat, please?", pause_after=0.5)

    # Max retries reached: exit reflection step
    reflective_speak("Alright, we'll continue with something else.")
    return ""  # empty string triggers LLM fallback in main loop


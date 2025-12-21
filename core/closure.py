# core/closure.py

import datetime

from system.voice_flow import reflective_speak, reflective_listen
from personalization.feedback import collect_feedback
from personalization.profiles import (
    load_profile,
    save_profile,
    update_profile
)
from memory.reflection_memory import ReflectionMemory
from core.summary import generate_session_summary


# Optional long-term reflection storage (user-controlled)
reflection_memory = ReflectionMemory()


def closure(state: dict, memory) -> None:
    """
    Step 6: Closure / Logging

    Responsibilities:
    - Gently close the reflection session
    - Collect optional feedback (style only)
    - Update user prompt preferences safely
    - Ask for explicit consent before saving
    - Store a non-interpretive session summary
    - Log a lightweight record in short-term chat memory
    """

    # ---- Gentle closing ----
    reflective_speak(
        "We’ll close this reflection now. Take a moment before moving on.",
        pause_after=1.5
    )

    # ---- Collect bounded feedback (optional) ----
    feedback = collect_feedback()

    if feedback:
        profile = load_profile()
        updated_profile = update_profile(profile, feedback)
        save_profile(updated_profile)

    # ---- Ask consent before saving reflection ----
    save_response = reflective_listen(
        "Would you like me to save a short summary of this session for your own review later? Say yes or no.",
        timeout=8
    )

    summary = None

    if save_response and "yes" in save_response.lower():
        summary = generate_session_summary(state)

        reflection_memory.add({
            "timestamp": datetime.datetime.now().isoformat(),
            "summary": summary,
            "raw_state": state
        })

        reflective_speak("Okay. I’ve saved a short summary for you.")
    else:
        reflective_speak("Alright. Nothing has been saved.")

    # ---- Optional read-back of summary ----
    if summary:
        read_back = reflective_listen(
            "Would you like to hear the summary now?",
            timeout=6
        )

        if read_back and "yes" in read_back.lower():
            reflective_speak("Here is the summary.")
            reflective_speak(summary, pause_after=2.0)

    # ---- Always log a lightweight record to short-term memory ----
    if memory:
        memory.add(
            user="Reflection session completed",
            assistant=summary if summary else "Reflection session completed."
        )

    # ---- Final grounding ----
    reflective_speak(
        "You’re free to continue with your day, or ask for anything else when you’re ready."
    )

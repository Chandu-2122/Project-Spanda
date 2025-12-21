# core/workflow.py

from personalization.profiles import load_profile
from system.voice_flow import reflective_speak, reflective_listen
from core.closure import closure

def run_reflection_session(memory):
    """
    Runs a full reflective session with 6 steps:
    check-in, reflection, tuning, planning, closure.

    Args:
        memory: ChatMemory instance for session logging
    """
    profile = load_profile()  # load current user profile
    state = {}

    # Step 1: Check-in
    reflective_speak("Let’s slow down for a moment.")
    state["checkin"] = reflective_listen("How are you feeling right now?")
    if not state["checkin"]:
        return

    # Step 2: Reflective exploration
    reflective_speak("Thank you. Just noticing that is enough.")
    state["reflection"] = reflective_listen("What feels most present in your mind?")
    if not state["reflection"]:
        return

    # Step 3: Mood tuning / adjustment
    reflective_speak("We can gently adjust, if you want.")
    state["tuning"] = reflective_listen("Would you like to shift your energy, or just observe?")
    if not state["tuning"]:
        return

    # Step 4: Centered choice / action planning
    reflective_speak("You are in charge here.")
    state["plan"] = reflective_listen("What feels like the right next step?")
    if not state["plan"]:
        return

    # Step 5: Closure (session, memory)
    closure(state, memory)

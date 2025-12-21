# core/tuning.py

from llm.prompt_builder import build_prompt
from llm.ollama import ask

def mood_tuning(state, profile):
    """
    Step 4: Subtle adjustment.
    """

    prompt = build_prompt(
        intent="tuning",
        profile=profile,
        context=state["reflection"]["insights"],
        instruction="Offer one small grounding or perspective-shifting exercise. Optional, never forced."
    )

    response = ask(prompt, memory=None)

    return {
        "exercise": response
    }

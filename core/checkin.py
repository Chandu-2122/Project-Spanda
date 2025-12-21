# core/checkin.py

from llm.prompt_builder import build_prompt
from llm.ollama import ask

def check_in(profile):
    """
    Step 1: Detect mood / energy.
    """

    prompt = build_prompt(
        intent="checkin",
        profile=profile,
        instruction="Ask the user to describe their current mood or energy in simple words."
    )

    response = ask(prompt, memory=None)

    return {
        "raw": response
    }

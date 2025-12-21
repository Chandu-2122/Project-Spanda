# core/reflection.py

from llm.prompt_builder import build_prompt
from llm.ollama import ask

def reflective_exploration(state, profile):
    """
    Step 3: Gentle self-inquiry.
    """

    prompt = build_prompt(
        intent="reflection",
        profile=profile,
        context=state["checkin"]["raw"],
        instruction="Ask 1–2 gentle questions that help the user observe thoughts without judgment."
    )

    response = ask(prompt, memory=None)

    return {
        "insights": response
    }

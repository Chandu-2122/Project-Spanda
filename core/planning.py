# core/planning.py

from llm.prompt_builder import build_prompt
from llm.ollama import ask

def centered_choice(state, profile):
    """
    Step 5: Help user choose next step consciously.
    """

    prompt = build_prompt(
        intent="planning",
        profile=profile,
        context=state,
        instruction="Ask what the user wants to do next, emphasizing choice and agency."
    )

    response = ask(prompt, memory=None)

    return {
        "choice": response
    }

# llm/ollama.py

import requests
from config import OLLAMA_URL, OLLAMA_MODEL

SYSTEM_PROMPT = (
    "You are Project Spanda. "
    "Your purpose is to make the user conscious and aware. "
    "Answer briefly and clearly. "
    "Do not say you are an AI."
)


def ask(prompt: str) -> str:
    """
    Generate a response from the Ollama LLM.

    Args:
        prompt (str): User's input prompt.

    Returns:
        str: Generated assistant response.
    """
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": f"{SYSTEM_PROMPT}\nUser: {prompt}\nAssistant:",
        "temperature": 0.7,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )
        return response.json().get(
            "response",
            "I couldn't think of an answer."
        )
    except Exception:
        return "I'm having trouble thinking right now."

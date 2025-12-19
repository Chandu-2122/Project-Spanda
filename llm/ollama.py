import ollama
from memory.chat_memory import ChatMemory


SYSTEM_PROMPT = """You are Spanda, a helpful voice assistant.
You remember recent conversation context when it is provided.
Answer clearly and concisely.
"""


def ask(query: str, memory: ChatMemory) -> str:
    """
    Build prompt using memory and send to Ollama safely.
    """
    try:
        context = memory.context()

        prompt = f"""{SYSTEM_PROMPT}

Conversation so far:
{context}

User: {query}
Assistant:
""".strip()

        response = ollama.chat(
            model="llama3.2:latest",
            messages=[
                {"role": "user", "content": prompt}],
        )

        return response["message"]["content"]

    except Exception as e:
        # Fail gracefully
        print(f"[LLM ERROR] {e}")
        return "Sorry, I ran into a problem while thinking. Please try again."

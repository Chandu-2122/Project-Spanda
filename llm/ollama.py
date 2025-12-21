# llm/ollama.py

import ollama
from memory.chat_memory import ChatMemory


def ask(query: str, memory: ChatMemory, system_prompt: str) -> str:
    """
    Build prompt using memory and send to Ollama safely.
    """
    try:
        messages = [
            {"role": "system", "content": system_prompt},
        ]

        if memory.buffer:
            messages.append({
                "role": "assistant",
                "content": memory.context()
            })

        messages.append({
            "role": "user",
            "content": query
        })

        response = ollama.chat(
            model="llama3.2:latest",
            messages=messages,
        )

        return response["message"]["content"]

    except Exception as e:
        print(f"[LLM ERROR] {e}")
        return "Sorry, I ran into a problem while thinking."
# memory/chat_memory.py

from collections import deque


class ChatMemory:
    """
    Lightweight conversational memory.

    Stores the last N user–assistant interactions
    to provide short-term conversational context.
    """

    def __init__(self, max_turns: int = 10000):
        """
        Initialize chat memory.

        Args:
            max_turns (int): Maximum number of conversation turns to retain.
        """
        self.buffer = deque(maxlen=max_turns)

    def add(self, user: str, assistant: str) -> None:
        """
        Add a conversation turn to memory.

        Args:
            user (str): User input text.
            assistant (str): Assistant response text.

        Returns:
            None
        """
        self.buffer.append({
            "user": user,
            "assistant": assistant
        })

    def context(self) -> str:
        """
        Get formatted conversation history.

        Returns:
            str: Conversation history as a single formatted string.
        """
        convo = ""
        for turn in self.buffer:
            convo += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"
        return convo.strip()

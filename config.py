# config.py

# ===== SPEECH CONFIG =====
VOICE_RATE = 250
VOICE_VOLUME = 1.0
VOICE_ID = 1  # 0 = male, 1 = female

# ===== LLM CONFIG =====
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:latest"

# ===== ASSISTANT CONFIG =====
ASSISTANT_NAME = "Project Spanda"
USER_NAME = "C"

WAKE_WORDS = ["hey spanda", "wake up", "spanda", "hey", "are you there", "bro", "dude"]
SLEEP_WORDS = ["sleep now", "go to sleep", "be quiet", "just wait", "wait", "sleep"]

# ===== BROWSER =====
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

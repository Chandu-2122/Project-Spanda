#personalization/presets.py

PRESETS = {
    "minimal_mirror": {
        "tone": "neutral",
        "structure": "light",
        "pace": "slow",
        "prompt_style": "short_questions"
    },
    "grounded_guide": {
        "tone": "calm",
        "structure": "guided",
        "pace": "slow",
        "prompt_style": "gentle_questions"
    },
    "practical_clarity": {
        "tone": "clear",
        "structure": "structured",
        "pace": "medium",
        "prompt_style": "direct_questions"
    }
}

def load_preset(name):
    return PRESETS.get(name, PRESETS["minimal_mirror"])

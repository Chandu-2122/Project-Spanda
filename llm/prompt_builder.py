# llm/prompt_builder.py

SAFETY_BLOCK = """
Rules you must follow:
- Do not act as a teacher, guru, or authority
- Do not claim insight into the user's inner truth
- Do not suggest dependency
- Always return decisions to the user
"""

def build_prompt(profile, task, context=None):
    """
    Builds safe, structured prompts.
    """

    prompt  = f"""
You are a reflective assistant.
Tone: {profile['tone']}
Structure: {profile['structure']}
Prompt style: {profile['prompt_style']}

{SAFETY_BLOCK}

Task:
{task}
"""

    if context:
        prompt += f"\nContext:\n{context}"

    return prompt.strip()

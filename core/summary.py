# core/summary.py

def generate_session_summary(state: dict) -> str:
    """
    Generate a neutral, non-interpretive session summary.

    Rules:
    - No analysis
    - No emotional labels
    - No advice
    - No conclusions
    - Use user's own words when possible
    """

    lines = []

    if "checkin" in state and state["checkin"]:
        lines.append(f"Check-in: {state['checkin']}")

    if "reflection" in state and state["reflection"]:
        lines.append(f"Observed thoughts: {state['reflection']}")

    if "tuning" in state and state["tuning"]:
        lines.append(f"Adjustment noted: {state['tuning']}")

    if "plan" in state and state["plan"]:
        lines.append(f"Next step chosen: {state['plan']}")

    if not lines:
        return "A reflection session was completed."

    return " | ".join(lines)

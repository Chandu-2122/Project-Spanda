# personalization/feedback.py

from system.voice_flow import reflective_listen

def collect_feedback():
    """
    Lightweight, optional session feedback.
    """
    helpful = reflective_listen(
        "Did this reflection feel helpful? Say yes or no."
    )
    helpful = (helpful or "").lower()

    structure = reflective_listen(
        "Would you prefer more guidance, less guidance, or the same?"
    )
    # if user gave no usable feedback, return None
    if not helpful and not structure:
        return None

    return {
        "helpful": helpful,
        "structure": structure
    }

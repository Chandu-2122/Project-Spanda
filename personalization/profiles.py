# personalization/profiles.py

import json
import os
from personalization.presets import load_preset

# Path for storing user profiles
PROFILE_PATH = "personalization/user_profile.json"


def load_profile() -> dict:
    """
    Load the user's profile from disk.
    If no profile exists, load a default preset.

    Returns:
        dict: User profile containing tone, structure, pace, and prompt style.
    """
    if os.path.exists(PROFILE_PATH):
        try:
            with open(PROFILE_PATH, "r", encoding="utf-8") as f:
                profile = json.load(f)
                return profile
        except Exception as e:
            print(f"[PROFILE ERROR] Failed to load profile: {e}")

    # If profile does not exist, use default preset
    return load_preset("minimal_mirror")


def save_profile(profile: dict) -> None:
    """
    Save the user's profile to disk.

    Args:
        profile (dict): User profile to save
    """
    try:
        os.makedirs(os.path.dirname(PROFILE_PATH), exist_ok=True)
        with open(PROFILE_PATH, "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2)
    except Exception as e:
        print(f"[PROFILE ERROR] Failed to save profile: {e}")


def update_profile(profile: dict, feedback: dict) -> dict:
    """
    Update the user's profile based on session feedback.

    Rules:
    - Feedback affects only tone, structure, or prompt style
    - Feedback does NOT change values, beliefs, or suggest insights
    - Safe, bounded evolution

    Args:
        profile (dict): Current user profile
        feedback (dict): Feedback collected from the session
            - 'structure': "more", "less", or "same"
            - 'helpful': "yes" / "no"

    Returns:
        dict: Updated profile
    """

    updated_profile = profile.copy()

    # Adjust session structure
    structure_feedback = (feedback.get("structure") or "").lower()
    if "less" in structure_feedback:
        updated_profile["structure"] = "light"
    elif "more" in structure_feedback:
        updated_profile["structure"] = "guided"
    # "same" or unknown = keep existing

    # Optional: Can handle tone changes in the future
    # helpful_feedback = feedback.get("helpful", "").lower()
    # Could be used for pacing or prompt style

    return updated_profile

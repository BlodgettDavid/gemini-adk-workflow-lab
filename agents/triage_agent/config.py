"""
Configuration settings 
    for the triage_agent multi-agent workflow.
"""

import os

DEFAULT_MODEL = "gemini-3.8-flash"


def get_model_name() -> str:
    """Return the configured Gemini model name from the environment."""
    return os.getenv("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
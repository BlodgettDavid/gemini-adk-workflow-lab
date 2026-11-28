"""
Deterministic local Python tools for 
    CS & Software Engineering triage.
"""

from typing import Literal

CategoryType = Literal["debugging", "concept", "setup"]


def classify_request_priority(prompt: str) -> dict[str, str | list[str]]:
    """Classify an incoming engineering request by 
        category 
        and urgency level.

    Args:
        prompt: 
            The raw user question
            error log
            or support request.

    Returns:
        A dictionary containing 
            the inferred category
            urgency level
            and matched signals.
    """
    text = prompt.lower()
    signals: list[str] = []

    debug_keywords = ("traceback", "exception", "error", "bug", "failing", "assert", "crash")
    setup_keywords = ("install", "pip", "venv", "git", "path", "environment", "permission", "cli")
    concept_keywords = ("how does", "explain", "difference between", "architecture", "big o", "pattern")

    if any(k in text for k in debug_keywords):
        category: CategoryType = "debugging"
        signals.append("runtime_or_test_failure")
    elif any(k in text for k in setup_keywords):
        category = "setup"
        signals.append("environment_or_tooling")
    elif any(k in text for k in concept_keywords):
        category = "concept"
        signals.append("conceptual_inquiry")
    else:
        category = "concept"
        signals.append("general_default")

    if any(k in text for k in ("blocking", "deadline", "production", "cannot start", "crash")):
        urgency = "high"
        signals.append("blocker_detected")
    elif category in ("debugging", "setup"):
        urgency = "medium"
    else:
        urgency = "low"

    return {
        "category": category,
        "urgency": urgency,
        "signals": signals,
    }


def build_diagnostic_checklist(category: str) -> dict[str, str | list[str]]:
    """Return a 
        deterministic intake checklist for a given triage category.
    Args:
        category: One of 'debugging', 
        'concept', 
        or 'setup'.

    Returns:
        A dictionary with 
            normalized category 
            and ordered verification steps.
    """
    normalized = category.strip().lower()
    checklists: dict[str, list[str]] = {
        "debugging": [
            "Capture the exact exception type and full stack trace.",
            "Identify the minimal reproducible input or failing test case.",
            "Inspect recent changes near the failing line or module.",
        ],
        "concept": [
            "Define the core abstraction or problem constraints.",
            "Compare time/space or architectural trade-offs.",
            "Walk through a concise, concrete code example.",
        ],
        "setup": [
            "Verify active interpreter/runtime version and virtual environment.",
            "Check PATH, working directory, and environment variables.",
            "Run a minimal health-check command to confirm resolution.",
        ],
    }

    steps = checklists.get(normalized, checklists["concept"])
    resolved_category = normalized if normalized in checklists else "concept"

    return {
        "category": resolved_category,
        "checklist": steps,
    }
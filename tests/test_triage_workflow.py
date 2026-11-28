"""Offline unit and structural tests for Iteration 1 triage_agent."""

from agents.triage_agent.agent import root_agent
from agents.triage_agent.config import DEFAULT_MODEL, get_model_name
from agents.triage_agent.tools import (
    build_diagnostic_checklist,
    classify_request_priority,
)


def test_get_model_name_default_and_override(monkeypatch):
    monkeypatch.delenv("GEMINI_MODEL", raising=False)
    assert get_model_name() == DEFAULT_MODEL

    monkeypatch.setenv("GEMINI_MODEL", "gemini-2.5-pro")
    assert get_model_name() == "gemini-2.5-pro"


def test_classify_request_priority_debugging_high_urgency():
    result = classify_request_priority(
        "Production crash with Traceback (most recent call last): KeyError"
    )
    assert result["category"] == "debugging"
    assert result["urgency"] == "high"
    assert "runtime_or_test_failure" in result["signals"]
    assert "blocker_detected" in result["signals"]


def test_classify_request_priority_setup():
    result = classify_request_priority("How do I activate my Python venv and run pip install?")
    assert result["category"] == "setup"
    assert result["urgency"] == "medium"


def test_classify_request_priority_concept_default():
    result = classify_request_priority("Explain the difference between composition and inheritance.")
    assert result["category"] == "concept"
    assert result["urgency"] == "low"


def test_build_diagnostic_checklist_known_and_fallback():
    debug_plan = build_diagnostic_checklist("debugging")
    assert debug_plan["category"] == "debugging"
    assert len(debug_plan["checklist"]) == 3

    fallback_plan = build_diagnostic_checklist("unknown_category")
    assert fallback_plan["category"] == "concept"
    assert len(fallback_plan["checklist"]) == 3


def test_root_agent_sub_agents_wiring():
    assert root_agent.name == "triage_coordinator"
    sub_agent_names = {agent.name for agent in root_agent.sub_agents}
    assert sub_agent_names == {"debugging_agent", "concept_agent", "setup_agent"}
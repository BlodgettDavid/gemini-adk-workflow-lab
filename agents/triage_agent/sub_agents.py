"""Specialist sub-agents for CS and Software Engineering support triage."""

from google.adk.agents import Agent

from .config import get_model_name
from .tools import build_diagnostic_checklist

debugging_agent = Agent(
    name="debugging_agent",
    model=get_model_name(),
    description=(
        "Specialist for Python/software bugs, stack traces, failing pytest runs, "
        "and runtime exceptions."
    ),
    instruction=(
        "You are a senior software debugging specialist. Analyze tracebacks, isolate "
        "the root cause, explain why the failure occurs, and provide a minimal, clean fix. "
        "Use build_diagnostic_checklist with category='debugging' when structured triage "
        "steps help the user verify the fix."
    ),
    tools=[build_diagnostic_checklist],
)

concept_agent = Agent(
    name="concept_agent",
    model=get_model_name(),
    description=(
        "Specialist for computer science fundamentals, algorithms, data structures, "
        "software architecture, and design pattern explanations."
    ),
    instruction=(
        "You are a computer science and software architecture mentor. Explain concepts "
        "clearly with concrete trade-offs and concise code examples. Use "
        "build_diagnostic_checklist with category='concept' when helpful."
    ),
    tools=[build_diagnostic_checklist],
)

setup_agent = Agent(
    name="setup_agent",
    model=get_model_name(),
    description=(
        "Specialist for local development environments, Python virtual environments, "
        "pip dependencies, Git workflows, and CLI configuration issues."
    ),
    instruction=(
        "You are a developer environment and tooling specialist. Provide exact, "
        "OS-aware commands and verification steps to resolve setup, dependency, or "
        "version-control issues. Use build_diagnostic_checklist with category='setup'."
    ),
    tools=[build_diagnostic_checklist],
)
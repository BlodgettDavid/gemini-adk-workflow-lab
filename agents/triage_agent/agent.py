"""Root coordinator agent for CS & Software Engineering Support Triage."""

from google.adk.agents import Agent

from .config import get_model_name
from .sub_agents import concept_agent, debugging_agent, setup_agent
from .tools import classify_request_priority

root_agent = Agent(
    name="triage_coordinator",
    model=get_model_name(),
    description="Routes incoming CS and software engineering requests to specialist sub-agents.",
    instruction=(
        "You are the intake triage coordinator for a CS and Software Engineering support desk. "
        "For every incoming request:\n"
        "1. Call classify_request_priority to assess category and urgency.\n"
        "2. Delegate to the matching specialist sub-agent:\n"
        "   - debugging_agent for tracebacks, test failures, and code bugs.\n"
        "   - setup_agent for virtual environments, package installs, Git, and CLI setup.\n"
        "   - concept_agent for algorithms, architecture, and conceptual explanations.\n"
        "Do not answer specialist technical questions yourself when a sub-agent applies."
    ),
    tools=[classify_request_priority],
    sub_agents=[debugging_agent, concept_agent, setup_agent],
)
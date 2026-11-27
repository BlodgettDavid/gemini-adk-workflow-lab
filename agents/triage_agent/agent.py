import os
from google.adk.agents.llm_agent import Agent

DEFAULT_MODEL = "gemini-3.8-flash"
model_name = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)

root_agent = Agent(
    model=model_name,
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
)
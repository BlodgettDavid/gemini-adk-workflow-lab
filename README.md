# Gemini ADK Workflow Lab

A portable, local-first multi-agent workflow built with the Google Agent Development Kit (ADK).

## Prerequisites

- Python 3.11+
- A Google AI Studio API key (GOOGLE_API_KEY)

## Local Setup

1. Create and activate a virtual environment:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install google-adk

2. Create your local environment file from the provided template (.env is gitignored):
   Copy-Item agents\triage_agent\.env.example agents\triage_agent\.env

3. Open agents\triage_agent\.env and set your credentials and preferred Gemini model:
   GOOGLE_GENAI_USE_ENTERPRISE=0
   GOOGLE_API_KEY=your-google-ai-studio-api-key
   GEMINI_MODEL=gemini-3.8-flash

If GEMINI_MODEL is omitted, the agent defaults to gemini-3.8-flash.

## Running the Agent

From the repository root with .venv active:

adk run agents/triage_agent
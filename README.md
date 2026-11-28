Here is the complete `README.md` in one copyable block (using a 4-backtick outer fence so inner code blocks don't break copying):

```markdown
# Gemini ADK Workflow Lab

A portable, local-first multi-agent workflow built with the Google Agent Development Kit (ADK) implementing an Orchestrator–Specialist pattern for CS and software engineering request triage.

## Architecture

- **Root Orchestrator (`triage_coordinator`):** Classifies incoming prompts using `classify_request_priority` and routes requests by category and urgency.
- **Specialist Agents:**
  - `debugging_agent` (high urgency): Root-cause analysis, minimal fixes, and diagnostic checklists.
  - `setup_agent` (medium urgency): Environment, tooling, and Windows/venv troubleshooting.
  - `concept_agent` (low urgency): Conceptual explanations, trade-offs, and concise code examples.

## Prerequisites

- Python 3.11+
- A Google AI Studio API key (`GOOGLE_API_KEY`)

## Local Setup

1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. Create your local environment file from the template (`.env` is gitignored):
   ```powershell
   Copy-Item agents\triage_agent\.env.example agents\triage_agent\.env
   ```

3. Open `agents\triage_agent\.env` and configure your credentials and model:
   ```env
   GOOGLE_GENAI_USE_ENTERPRISE=0
   GOOGLE_API_KEY=your-google-ai-studio-api-key
   GEMINI_MODEL=gemini-3.8-flash
   ```
   If `GEMINI_MODEL` is omitted, the agent defaults to `gemini-3.8-flash`.

## Running & Testing

From the repository root with `.venv` active:

- **Interactive CLI:**
  ```cmd
  adk run agents/triage_agent
  ```
- **Web UI & Event Trace (`http://127.0.0.1:8000`):**
  ```cmd
  adk web agents
  ```
  On Windows, ADK automatically forces `--no-reload` so subprocess/tool execution works cleanly.
- **Unit & Integration Tests:**
  ```cmd
  pytest
  ```

### Troubleshooting Model Errors

- **Transient `503 UNAVAILABLE` or `429 RESOURCE_EXHAUSTED` quota limits:** You can override the model for a session without editing `config.py` (for example, `set GEMINI_MODEL=gemini-2.5-flash` in `cmd.exe`, then `set GEMINI_MODEL=` to clear it).

```
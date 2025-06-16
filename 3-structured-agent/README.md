# Structured Agent Example

This example demonstrates an ADK agent that generates structured output (emails) using Pydantic models. The agent creates professional emails with properly formatted subject lines and bodies.

## Prerequisites

1. Python 3.8 or higher
2. Google API key for Gemini model

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Set up your environment:
   - Create a `.env` file in the `email-agent` directory
   - Add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Running the Agent

1. Make sure you're in the `3-structured-agent` directory (the parent directory of email-agent)

2. Start the web interface:
```bash
adk web
```

3. Access the web UI:
   - Open your browser and go to http://localhost:8000
   - Select "email_agent" from the dropdown menu in the top-left corner
   - Start chatting with the agent in the textbox at the bottom

## Project Structure

```
3-structured-agent/
    email-agent/           # Agent package directory
        __init__.py       # Imports the agent module
        agent.py          # Defines the root_agent and output schema
        .env             # Environment variables (API key)
```

## Agent Configuration

The agent is configured in `agent.py` with the following settings:
- Name: "email_agent"
- Model: "gemini-2.0-flash"
- Description: "Generates professional emails with structured subject and body"
- Output Schema: EmailContent (Pydantic model)
- Instructions: Set to generate professional emails with proper formatting

## Output Structure

The agent uses a Pydantic model to ensure structured output:

```python
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )
```

This ensures that all generated emails have:
- A properly formatted subject line
- A well-structured body with:
  - Professional greeting
  - Clear and concise content
  - Appropriate closing
  - Signature

## Example Interactions

Try these example prompts:
- "Write a follow-up email after a job interview"
- "Create an email to request a meeting with a client"
- "Draft an email to thank a colleague for their help"
- "Write a professional email to decline a job offer"

## Features

1. **Structured Output**
   - Uses Pydantic models to ensure consistent output format
   - Validates email structure before returning
   - Maintains professional formatting

2. **Professional Formatting**
   - Generates appropriate subject lines
   - Creates well-structured email bodies
   - Includes proper greetings and closings
   - Adds professional signatures

3. **Context-Aware**
   - Adapts tone based on the email's purpose
   - Uses formal language for business communications
   - Maintains appropriate level of formality

## Troubleshooting

If you encounter any issues:

1. Verify you're in the correct directory (3-structured-agent)
2. Check that your `.env` file contains the correct API key
3. Ensure all dependencies are installed
4. Make sure the agent appears in the dropdown menu of the web UI
5. If the output isn't properly formatted, check that your prompt is clear and specific

## Stopping the Server

To stop the web server:
- Press `Ctrl+C` in the terminal where the server is running

## Notes

- The agent uses Pydantic models to ensure structured output
- All responses are validated against the defined schema
- The agent maintains professional formatting and tone
- You can modify the output schema to include additional fields if needed

# Basic ADK Agent Example

This is a simple greeting agent built using Google's ADK (Agent Development Kit). The agent is designed to greet users and ask for their names.

## Prerequisites

1. Python 3.8 or higher
2. Google API key for Gemini model

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Set up your environment:
   - Create a `.env` file in the `greeting-agent` directory
   - Add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Running the Agent

1. Make sure you're in the `1-basic-agent` directory (the parent directory of greeting-agent)

2. Start the web interface:
```bash
adk web
```

3. Access the web UI:
   - Open your browser and go to http://localhost:8000
   - Select "greeting_agent" from the dropdown menu in the top-left corner
   - Start chatting with the agent in the textbox at the bottom

## Project Structure

```
1-basic-agent/
    greeting-agent/         # Agent package directory
        __init__.py        # Imports the agent module
        agent.py           # Defines the root_agent
        .env              # Environment variables (API key)
```

## Agent Configuration

The agent is configured in `agent.py` with the following settings:
- Name: "greeting_agent"
- Model: "gemini-2.0-flash"
- Description: "Greeting agent"
- Instructions: Set to greet users and ask for their names

## Example Interactions

Try these example prompts:
- "Hello!"
- "What's your name?"
- "How are you today?"

## Troubleshooting

If you encounter any issues:

1. Verify you're in the correct directory (1-basic-agent)
2. Check that your `.env` file contains the correct API key
3. Ensure all dependencies are installed
4. Make sure the agent appears in the dropdown menu of the web UI

## Stopping the Server

To stop the web server:
- Press `Ctrl+C` in the terminal where the server is running

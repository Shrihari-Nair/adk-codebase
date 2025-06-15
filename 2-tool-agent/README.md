# Tool Agent Example

This is an example of an ADK agent that demonstrates the use of tools, specifically the Google Search tool. The agent can perform web searches to find information for users.

## Prerequisites

1. Python 3.8 or higher
2. Google API key for Gemini model
3. Google Search API key (for the search functionality)

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Set up your environment:
   - Create a `.env` file in the `tool-agent` directory
   - Add your API keys:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   GOOGLE_SEARCH_API_KEY=your_search_api_key_here
   ```

## Running the Agent

1. Make sure you're in the `2-tool-agent` directory (the parent directory of tool-agent)

2. Start the web interface:
```bash
adk web
```

3. Access the web UI:
   - Open your browser and go to http://localhost:8000
   - Select "tool_agent" from the dropdown menu in the top-left corner
   - Start chatting with the agent in the textbox at the bottom

## Project Structure

```
2-tool-agent/
    tool-agent/           # Agent package directory
        __init__.py      # Imports the agent module
        agent.py         # Defines the root_agent and tools
        .env            # Environment variables (API keys)
```

## Agent Configuration

The agent is configured in `agent.py` with the following settings:
- Name: "tool_agent"
- Model: "gemini-2.0-flash"
- Description: "Tool agent"
- Tools: google_search
- Instructions: Set to use the available tools to help users

## Available Tools

The agent currently has access to the following tools:

1. **Google Search** (`google_search`)
   - Allows the agent to search the web for information
   - Useful for finding up-to-date information
   - Can be used to answer questions that require current data

## Example Interactions

Try these example prompts:
- "What's the latest news about AI?"
- "Find information about climate change"
- "Search for the best programming practices in Python"

## Troubleshooting

If you encounter any issues:

1. Verify you're in the correct directory (2-tool-agent)
2. Check that your `.env` file contains both required API keys
3. Ensure all dependencies are installed
4. Make sure the agent appears in the dropdown menu of the web UI
5. If search isn't working, verify your Google Search API key is valid

## Stopping the Server

To stop the web server:
- Press `Ctrl+C` in the terminal where the server is running

## Notes

- The agent is configured to use only the Google Search tool, but the code includes commented examples of how to add more tools
- You can modify the agent's instructions to change how it uses the available tools
- The agent will automatically use the appropriate tool based on the user's request

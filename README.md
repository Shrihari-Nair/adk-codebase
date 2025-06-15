# ADK Agent Examples

This repository contains examples of agents built using Google's ADK (Agent Development Kit). Each example demonstrates different capabilities and features of ADK.

## Available Agents

### 1. Basic Agent (`1-basic-agent`)
A simple greeting agent that demonstrates the basic structure of an ADK agent.
- Greets users and asks for their names
- Uses the Gemini model for natural language understanding
- Shows how to create a basic agent without tools

[View Basic Agent README](1-basic-agent/README.md)

### 2. Tool Agent (`2-tool-agent`)
An agent that demonstrates the use of tools, specifically Google Search.
- Can perform web searches to find information
- Shows how to integrate and use tools with an agent
- Demonstrates tool configuration and usage

[View Tool Agent README](2-tool-agent/README.md)

## Prerequisites

1. Python 3.8 or higher
2. Google API key for Gemini model
3. Additional API keys as required by specific agents:
   - Google Search API key (for Tool Agent)

## Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd adk-codebase
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Each agent directory has its own `.env` file
   - Copy the required API keys to the appropriate `.env` files
   - See individual agent READMEs for specific requirements

## Running Agents

1. Navigate to the specific agent's parent directory:
```bash
cd <agent-directory>  # e.g., cd 1-basic-agent
```

2. Start the web interface:
```bash
adk web
```

3. Access the web UI:
   - Open your browser and go to http://localhost:8000
   - Select the desired agent from the dropdown menu
   - Start interacting with the agent

## Project Structure

```
adk-codebase/
├── 1-basic-agent/           # Basic greeting agent
│   └── greeting-agent/
│       ├── __init__.py
│       ├── agent.py
│       └── .env
├── 2-tool-agent/            # Agent with Google Search tool
│   └── tool-agent/
│       ├── __init__.py
│       ├── agent.py
│       └── .env
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## Common Features

All agents in this repository:
- Use the Gemini model for natural language understanding
- Follow ADK's required project structure
- Include proper documentation
- Can be run using the `adk web` command
- Provide a web interface for interaction

## Troubleshooting

If you encounter issues:

1. Verify you're in the correct directory (parent directory of the agent)
2. Check that all required API keys are properly set in the `.env` files
3. Ensure all dependencies are installed
4. Make sure the agent appears in the web UI dropdown menu
5. Check the specific agent's README for additional troubleshooting steps

## Stopping the Server

To stop any running agent:
- Press `Ctrl+C` in the terminal where the server is running

## Contributing

Feel free to:
- Add new agent examples
- Improve existing agents
- Add new tools or features
- Update documentation

## License

[Add your license information here]

## Resources

- [Google ADK Documentation](https://ai.google.dev/docs)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [ADK GitHub Repository](https://github.com/google/adk) 
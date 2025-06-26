# ADK Agent Examples

This repository contains comprehensive examples of agents built using Google's ADK (Agent Development Kit). Each example demonstrates different capabilities and features of ADK, from basic agents to advanced stateful sessions.

## Available Agents

### 1. Basic Agent (`1-basic-agent`)
A simple greeting agent that demonstrates the fundamental structure of an ADK agent.
- **Purpose**: Greets users and asks for their names
- **Features**: 
  - Basic agent creation without tools
  - Simple conversation handling
  - Web interface interaction
- **Use Case**: Learning ADK basics and agent structure

[View Basic Agent README](1-basic-agent/README.md)

### 2. Tool Agent (`2-tool-agent`)
An agent that demonstrates the integration and use of external tools, specifically Google Search.
- **Purpose**: Performs web searches to find real-time information
- **Features**:
  - Tool integration with Google Search
  - Real-time data retrieval
  - Dynamic information gathering
- **Use Case**: Creating agents that need access to current information

[View Tool Agent README](2-tool-agent/README.md)

### 3. Structured Agent (`3-structured-agent`)
An agent that generates structured output using Pydantic models for email generation.
- **Purpose**: Creates professional emails with consistent formatting
- **Features**:
  - Structured output using Pydantic models
  - Data validation and formatting
  - Professional email templates
- **Use Case**: Applications requiring consistent, validated output formats

[View Structured Agent README](3-structured-agent/README.md)

### 4. Stateful Sessions (`4-state-sessions`)
An advanced example demonstrating stateful sessions for maintaining context across conversations.
- **Purpose**: Maintains user information and preferences across multiple interactions
- **Features**:
  - Session state management
  - Context persistence
  - Template variable injection
  - User preference tracking
- **Use Case**: Personal assistants, customer support, and applications requiring user context

[View Stateful Sessions README](4-state-sessions/README.md)

### 5. Persistent Storage (`5-persistent-storage`)
An advanced example demonstrating database-backed persistent storage for long-term data retention.
- **Purpose**: Stores user data and session information in a SQLite database for persistence across application restarts
- **Features**:
  - Database-backed session services
  - Smart reminder management with CRUD operations
  - Session continuity and automatic discovery
  - Interactive CLI with colored output
  - Custom tools for state manipulation
- **Use Case**: Production applications requiring persistent data storage, personal assistants, and task management systems

[View Persistent Storage README](5-persistent-storage/README.md)

## Prerequisites

1. **Python 3.8 or higher**
2. **Google API key for Gemini model**
3. **Additional API keys as required by specific agents**:
   - Google Search API key (for Tool Agent)
   - No additional keys needed for Basic, Structured, or Stateful agents

## Setup

### 1. Repository Setup
```bash
git clone <repository-url>
cd adk-codebase
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Each agent directory requires its own `.env` file with appropriate API keys:

#### Basic Agent
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

#### Tool Agent
```
GOOGLE_API_KEY=your_gemini_api_key_here
GOOGLE_SEARCH_API_KEY=your_search_api_key_here
```

#### Structured Agent
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

#### Stateful Sessions
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

#### Persistent Storage
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

## Running Agents

### Web Interface Method (Recommended)
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

### Direct Execution Method (Stateful Sessions)
For the stateful sessions example:
```bash
cd 4-state-sessions
python basic-stateful-session.py
```

## Project Structure

```
adk-codebase/
├── 1-basic-agent/                    # Basic greeting agent
│   ├── greeting-agent/
│   │   ├── __init__.py
│   │   ├── agent.py                  # Basic agent definition
│   │   └── .env                      # Environment variables
│   └── README.md
├── 2-tool-agent/                     # Agent with Google Search tool
│   ├── tool-agent/
│   │   ├── __init__.py
│   │   ├── agent.py                  # Agent with tool integration
│   │   └── .env                      # Environment variables
│   └── README.md
├── 3-structured-agent/               # Agent with structured output
│   ├── email-agent/
│   │   ├── __init__.py
│   │   ├── agent.py                  # Agent with Pydantic models
│   │   └── .env                      # Environment variables
│   └── README.md
├── 4-state-sessions/                 # Stateful session example
│   ├── basic-stateful-session.py     # Main execution script
│   ├── question_answering_agent/
│   │   ├── __init__.py
│   │   └── agent.py                  # Agent with session state
│   ├── .env                          # Environment variables
│   └── README.md
├── 5-persistent-storage/             # Database-backed persistent storage
│   ├── main.py                       # Main execution script with session management
│   ├── utils.py                      # Utility functions for CLI and state display
│   ├── memory_agent/
│   │   ├── __init__.py
│   │   └── agent.py                  # Agent with custom tools and database storage
│   ├── my_agent_data.db              # SQLite database (created automatically)
│   ├── .env                          # Environment variables
│   └── README.md
├── requirements.txt                  # Project dependencies
└── README.md                        # This file
```

## Common Features

All agents in this repository share these features:
- **Gemini Model Integration**: Use Google's Gemini model for natural language understanding
- **ADK Compliance**: Follow ADK's required project structure and conventions
- **Comprehensive Documentation**: Each agent includes detailed README files
- **Web Interface**: Can be run using the `adk web` command for interactive testing
- **Environment Management**: Proper API key configuration and environment setup
- **Error Handling**: Basic error handling and validation

## Agent Capabilities Comparison

| Feature | Basic Agent | Tool Agent | Structured Agent | Stateful Sessions | Persistent Storage |
|---------|-------------|------------|------------------|-------------------|-------------------|
| Basic Conversation | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tool Integration | ❌ | ✅ | ❌ | ❌ | ✅ |
| Structured Output | ❌ | ❌ | ✅ | ❌ | ❌ |
| State Management | ❌ | ❌ | ❌ | ✅ | ✅ |
| Database Storage | ❌ | ❌ | ❌ | ❌ | ✅ |
| Web Interface | ✅ | ✅ | ✅ | ✅ | ❌ |
| CLI Interface | ❌ | ❌ | ❌ | ❌ | ✅ |
| API Keys Required | 1 | 2 | 1 | 1 | 1 |

## Example Interactions

### Basic Agent
- "Hello!"
- "What's your name?"
- "How are you today?"

### Tool Agent
- "What's the latest news about AI?"
- "Find information about climate change"
- "Search for the best programming practices in Python"

### Structured Agent
- "Write a follow-up email after a job interview"
- "Create an email to request a meeting with a client"
- "Draft an email to thank a colleague for their help"

### Stateful Sessions
- "What is shrihari's favorite TV show?"
- "What sports does shrihari like?"
- "What is shrihari's favorite food?"

### Persistent Storage
- "Hi, my name is John"
- "Add a reminder to buy groceries"
- "What are my reminders?"
- "Update reminder 1 to buy organic groceries"
- "Delete my grocery reminder"

## Troubleshooting

### Common Issues and Solutions

1. **Agent not appearing in dropdown**:
   - Verify you're in the correct directory (parent directory of the agent)
   - Check that `__init__.py` properly imports the agent module
   - Ensure `agent.py` defines a variable named `root_agent`

2. **API key errors**:
   - Verify all required API keys are set in the `.env` file
   - Check that the API keys are valid and have proper permissions
   - Ensure the `.env` file is in the correct location

3. **Import errors**:
   - Run `pip install -r requirements.txt` to install all dependencies
   - Check Python version (requires 3.8 or higher)
   - Verify virtual environment is activated if using one

4. **Session state issues** (Stateful Sessions):
   - Verify session is created successfully
   - Check that template variables match session state keys
   - Ensure session service is properly configured

### Getting Help

1. Check the specific agent's README for detailed troubleshooting
2. Verify all prerequisites are met
3. Check the ADK documentation for additional guidance
4. Ensure you're using the latest version of the ADK package

## Stopping the Server

To stop any running agent:
- Press `Ctrl+C` in the terminal where the server is running
- For stateful sessions, the script will complete automatically

## Development and Customization

### Adding New Agents
1. Create a new directory following the naming convention
2. Include the required files: `__init__.py`, `agent.py`, `.env`
3. Follow the ADK project structure
4. Add comprehensive documentation

### Extending Existing Agents
- **Basic Agent**: Add tools, modify instructions, change model
- **Tool Agent**: Add more tools, customize tool usage
- **Structured Agent**: Modify output schema, add new fields
- **Stateful Sessions**: Add more state fields, implement state updates

### Best Practices
1. Always include proper documentation
2. Use meaningful agent names and descriptions
3. Implement proper error handling
4. Test thoroughly before deployment
5. Follow ADK conventions and patterns

## Contributing

We welcome contributions! Please:

1. **Add new agent examples** that demonstrate different ADK features
2. **Improve existing agents** with better functionality or documentation
3. **Add new tools or features** to existing agents
4. **Update documentation** to make it clearer and more comprehensive
5. **Report issues** and suggest improvements

### Contribution Guidelines
- Follow the existing code structure and conventions
- Include comprehensive documentation for new features
- Test your changes thoroughly
- Update this README when adding new agents

## License

[Add your license information here]

## Resources

### Official Documentation
- [Google ADK Documentation](https://ai.google.dev/docs)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [ADK GitHub Repository](https://github.com/google/adk)

### Additional Resources
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Models](https://ai.google.dev/gemini-api/docs/models)
- [ADK Best Practices](https://ai.google.dev/docs/best-practices)

### Community
- [ADK Community Forum](https://github.com/google/adk/discussions)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/google-adk)
- [GitHub Issues](https://github.com/google/adk/issues) 
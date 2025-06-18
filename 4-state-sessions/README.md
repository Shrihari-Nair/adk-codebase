# Stateful Sessions Example

This example demonstrates how to create and manage stateful sessions in ADK, allowing agents to maintain context and user information across multiple interactions.

## Overview

Stateful sessions enable agents to:
- Remember user information across conversations
- Maintain context between interactions
- Store user preferences and data
- Provide personalized responses based on stored state

## Prerequisites

1. Python 3.8 or higher
2. Google API key for Gemini model

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Set up your environment:
   - Create a `.env` file in the `4-state-sessions` directory
   - Add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Project Structure

```
4-state-sessions/
├── basic-stateful-session.py    # Main script demonstrating stateful sessions
├── question_answering_agent/    # Agent package directory
│   ├── __init__.py             # Imports the agent module
│   └── agent.py                # Defines the question answering agent
└── .env                        # Environment variables (API key)
```

## How It Works

### 1. Session Service Setup
```python
session_service_stateful = InMemorySessionService()
```
- Creates an in-memory service to store session data
- Persists information across multiple interactions
- Can be replaced with database-backed services for production

### 2. Initial State Definition
```python
initial_state = {
    "user_name": "shrihari nair",
    "user_preferences": """
        I like to play Pickleball, Disc Golf, and Tennis.
        My favorite food is Mexican.
        My favorite TV show is Game of Thrones.
        Loves it when people like and subscribe to his YouTube channel.
    """,
}
```
- Defines the initial data that will be stored in the session
- Can include any user-specific information
- This data is accessible to the agent during conversations

### 3. Session Creation
```python
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
```
- Creates a unique session with the specified state
- Each session has a unique ID for tracking
- State is persisted and can be retrieved later

### 4. Agent Configuration
The agent uses template variables to access session state:
```python
instruction="""
You are a helpful assistant that answers questions about the user's preferences.

Here is some information about the user:
Name: {user_name}
Preferences: {user_preferences}
"""
```
- `{user_name}` and `{user_preferences}` are automatically replaced with session state
- The agent can access any data stored in the session
- Template variables are filled when the agent processes messages

### 5. Running the Agent
```python
runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)
```
- The runner manages the interaction between the agent and session
- Automatically injects session state into agent instructions
- Handles message processing and response generation

## Running the Example

1. Make sure you're in the `4-state-sessions` directory

2. Run the stateful session example:
```bash
python basic-stateful-session.py
```

3. The script will:
   - Create a new session with initial state
   - Send a question to the agent
   - Display the agent's response
   - Show the final session state

## Example Output

```
CREATED NEW SESSION:
    Session ID: 12345678-1234-1234-1234-123456789abc
Final Response: Based on the information provided, Shrihari's favorite TV show is Game of Thrones.

==== Session Event Exploration ====
=== Final Session State ===
user_name: shrihari nair
user_preferences: 
        I like to play Pickleball, Disc Golf, and Tennis.
        My favorite food is Mexican.
        My favorite TV show is Game of Thrones.
        Loves it when people like and subscribe to his YouTube channel.
```

## Key Features

1. **State Persistence**
   - Session data is maintained across interactions
   - Information can be updated and retrieved
   - State survives between agent calls

2. **Template Variable Injection**
   - Session state is automatically injected into agent instructions
   - No manual state management required
   - Dynamic content based on stored data

3. **Session Management**
   - Unique session IDs for tracking
   - User-specific sessions
   - Application-level organization

4. **Flexible State Structure**
   - Can store any JSON-serializable data
   - Nested objects and arrays supported
   - Easy to extend with new state fields

## Use Cases

- **Personal Assistants**: Remember user preferences and history
- **Customer Support**: Track conversation context and user information
- **Educational Bots**: Maintain learning progress and preferences
- **Shopping Assistants**: Remember shopping cart and preferences

## Troubleshooting

If you encounter any issues:

1. Verify you're in the correct directory (4-state-sessions)
2. Check that your `.env` file contains the correct API key
3. Ensure all dependencies are installed
4. Verify the session is created successfully
5. Check that the agent can access session state

## Notes

- The InMemorySessionService stores data in memory (not persistent)
- For production use, consider using database-backed session services
- Session state is automatically serialized and deserialized
- Template variables are case-sensitive and must match session state keys 
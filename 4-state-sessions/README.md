# Stateful Sessions Example - Comprehensive Guide

This example demonstrates advanced stateful session management in ADK, showing how to create agents that maintain context, user information, and conversation history across multiple interactions. This is essential for building personalized AI assistants that remember user preferences and provide contextual responses.

## Table of Contents

1. [Overview](#overview)
2. [Key Concepts](#key-concepts)
3. [Prerequisites](#prerequisites)
4. [Setup](#setup)
5. [Project Structure](#project-structure)
6. [Code Walkthrough](#code-walkthrough)
7. [How Stateful Sessions Work](#how-stateful-sessions-work)
8. [Running the Example](#running-the-example)
9. [Understanding the Output](#understanding-the-output)
10. [Advanced Features](#advanced-features)
11. [Use Cases](#use-cases)
12. [Troubleshooting](#troubleshooting)
13. [Best Practices](#best-practices)
14. [Extending the Example](#extending-the-example)

## Overview

Stateful sessions are a powerful feature in ADK that enables agents to:
- **Maintain Context**: Remember information across multiple conversations
- **Store User Data**: Keep user preferences, history, and personal information
- **Provide Personalization**: Deliver tailored responses based on stored data
- **Enable Continuity**: Continue conversations where they left off
- **Track Progress**: Monitor user interactions and learning progress

### Why Stateful Sessions Matter

Traditional stateless agents treat each interaction as independent, losing context between messages. Stateful sessions solve this by:
- Persisting data across interactions
- Enabling personalized experiences
- Supporting complex multi-turn conversations
- Allowing agents to learn from user behavior
- Providing consistent user experiences

## Key Concepts

### 1. Session Service
- **InMemorySessionService**: Stores session data in memory (for development/testing)
- **Database-backed services**: For production use with persistent storage
- **Session lifecycle**: Creation, retrieval, updates, and deletion

### 2. Session State
- **Initial state**: Data provided when creating a session
- **Dynamic updates**: State can be modified during conversations
- **Template injection**: State values are automatically injected into agent instructions
- **State persistence**: Data survives between agent calls

### 3. Template Variables
- **Dynamic content**: Placeholders in agent instructions that get replaced with state values
- **Automatic injection**: ADK handles the replacement process
- **Type safety**: Values are validated against expected types
- **Flexible structure**: Support for nested objects and arrays

### 4. Runner Integration
- **Session management**: Handles session creation and retrieval
- **State injection**: Automatically injects state into agent instructions
- **Event handling**: Processes agent responses and events
- **Error handling**: Manages session-related errors

## Prerequisites

1. **Python 3.8 or higher**
2. **Google API key for Gemini model**
3. **Understanding of basic ADK concepts** (from previous examples)
4. **Familiarity with Python dictionaries and JSON**

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Configuration
Create a `.env` file in the `4-state-sessions` directory:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 3. Verify Installation
Ensure all required packages are installed:
- `google-adk`: Core ADK functionality
- `google-genai`: Google's Generative AI library
- `python-dotenv`: Environment variable management
- `uuid`: Unique identifier generation

## Project Structure

```
4-state-sessions/
├── basic-stateful-session.py          # Main execution script
├── question_answering_agent/          # Agent package directory
│   ├── __init__.py                   # Imports the agent module
│   └── agent.py                      # Agent definition with template variables
├── .env                              # Environment variables
└── README.md                         # This comprehensive guide
```

### File Descriptions

- **`basic-stateful-session.py`**: Demonstrates session creation, state management, and agent interaction
- **`question_answering_agent/agent.py`**: Defines an agent that uses session state via template variables
- **`__init__.py`**: Makes the agent discoverable by ADK
- **`.env`**: Contains API keys and configuration

## Code Walkthrough

### 1. Session Service Setup (`basic-stateful-session.py`)

```python
session_service_stateful = InMemorySessionService()
```

**What this does:**
- Creates an in-memory service for storing session data
- Provides methods for session creation, retrieval, and management
- Handles data serialization and deserialization
- Manages session lifecycle (create, read, update, delete)

**Why InMemorySessionService:**
- Fast and simple for development and testing
- No external dependencies
- Data is lost when the process ends
- Perfect for learning and prototyping

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

**State Structure:**
- **`user_name`**: String value for personalization
- **`user_preferences`**: Multi-line string with detailed preferences
- **Flexible format**: Can include any JSON-serializable data

**State Design Principles:**
- **Descriptive keys**: Use clear, meaningful names
- **Structured data**: Organize information logically
- **Extensible format**: Easy to add new fields later
- **Human-readable**: Values should be clear and understandable

### 3. Session Creation

```python
APP_NAME = "shrihari_bot"
USER_ID = "shrihari_nair"
SESSION_ID = str(uuid.uuid4())

stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
```

**Session Parameters:**
- **`app_name`**: Identifies the application (e.g., "shrihari_bot")
- **`user_id`**: Unique identifier for the user
- **`session_id`**: Unique identifier for this specific session
- **`state`**: Initial data to store in the session

**UUID Generation:**
- `uuid.uuid4()` creates a random, unique identifier
- Ensures no session conflicts
- Format: `12345678-1234-1234-1234-123456789abc`

### 4. Agent Configuration (`question_answering_agent/agent.py`)

```python
question_answering_agent = Agent(
    name="question_answering_agent",
    model="gemini-2.0-flash",
    description="Question answering agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: {user_name}
    Preferences: {user_preferences}
    """,
)
```

**Template Variables:**
- **`{user_name}`**: Will be replaced with the actual user name from session state
- **`{user_preferences}`**: Will be replaced with the user's preferences
- **Automatic injection**: ADK handles the replacement process
- **Dynamic content**: Instructions change based on session state

### 5. Runner Setup

```python
runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)
```

**Runner Configuration:**
- **`agent`**: The agent to execute
- **`app_name`**: Must match the session's app name
- **`session_service`**: Service for managing sessions

### 6. Message Creation

```python
new_message = types.Content(
    role="user",
    parts=[types.Part(text="What is shrihari's favorite TV show?")]
)
```

**Message Structure:**
- **`role="user"`**: Identifies the message sender
- **`parts`**: Array of message components
- **`types.Part`**: Individual message part with text content

### 7. Agent Execution

```python
for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")
```

**Event Processing:**
- **`runner.run()`**: Executes the agent with session context
- **Event loop**: Processes multiple events during execution
- **`is_final_response()`**: Identifies the final agent response
- **Response extraction**: Gets the actual response text

### 8. Session State Retrieval

```python
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")
```

**State Inspection:**
- **`get_session()`**: Retrieves the current session
- **State iteration**: Shows all stored data
- **Debugging**: Helps understand what data is maintained

## How Stateful Sessions Work

### 1. Session Lifecycle

```
Session Creation → State Initialization → Agent Execution → State Retrieval
       ↓                    ↓                    ↓                ↓
   Create session      Set initial data    Process with      Inspect final
   with unique ID      and preferences     session state     session state
```

### 2. Template Variable Injection Process

```
1. Agent receives message
2. Runner retrieves session state
3. Template variables in instructions are identified
4. State values replace template variables
5. Agent processes with personalized instructions
6. Response is generated based on injected context
```

### 3. State Persistence

- **In-memory storage**: Data persists during the application lifecycle
- **Session isolation**: Each session has independent state
- **User separation**: Different users have separate sessions
- **Application boundaries**: Sessions are scoped to specific applications

## Running the Example

### 1. Navigate to Directory
```bash
cd 4-state-sessions
```

### 2. Execute the Script
```bash
python basic-stateful-session.py
```

### 3. Expected Output
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

## Understanding the Output

### Session Creation Confirmation
- **Session ID**: Unique identifier for tracking
- **Creation status**: Confirms successful session creation

### Agent Response
- **Contextual answer**: Response based on session state
- **Personalized content**: Uses stored user information
- **Accurate information**: Reflects the stored preferences

### Session State Display
- **Complete state**: Shows all stored data
- **Data integrity**: Verifies state persistence
- **Debugging information**: Helps understand session contents

## Advanced Features

### 1. State Updates
You can modify session state during execution:
```python
# Update session state
session.state["last_interaction"] = "2024-01-15"
session.state["interaction_count"] = session.state.get("interaction_count", 0) + 1
```

### 2. Multiple Sessions
Create and manage multiple sessions:
```python
# Create session for different user
session2 = session_service_stateful.create_session(
    app_name="shrihari_bot",
    user_id="another_user",
    session_id=str(uuid.uuid4()),
    state={"user_name": "Jane Doe", "user_preferences": "..."}
)
```

### 3. Complex State Structures
Store complex data in sessions:
```python
complex_state = {
    "user_profile": {
        "name": "shrihari nair",
        "age": 30,
        "location": "San Francisco"
    },
    "preferences": {
        "sports": ["Pickleball", "Disc Golf", "Tennis"],
        "food": "Mexican",
        "entertainment": {
            "tv_shows": ["Game of Thrones"],
            "youtube": "Likes and subscribes"
        }
    },
    "conversation_history": []
}
```

### 4. Template Variable Nesting
Access nested state values:
```python
instruction="""
User Profile:
Name: {user_profile.name}
Age: {user_profile.age}
Location: {user_profile.location}

Sports: {preferences.sports}
"""
```

## Use Cases

### 1. Personal Assistants
- Remember user preferences and habits
- Provide personalized recommendations
- Track user goals and progress
- Maintain conversation context

### 2. Customer Support
- Store customer information and history
- Track support ticket progress
- Remember previous interactions
- Provide consistent service experience

### 3. Educational Bots
- Track learning progress and preferences
- Remember user's knowledge level
- Adapt content based on learning history
- Maintain study session context

### 4. Shopping Assistants
- Remember shopping cart and preferences
- Track purchase history
- Provide personalized recommendations
- Maintain shopping session context

### 5. Healthcare Applications
- Store patient information securely
- Track treatment progress
- Remember medical preferences
- Maintain consultation context

## Troubleshooting

### Common Issues and Solutions

#### 1. Session Not Found
**Problem**: `SessionNotFoundError` when retrieving session
**Solution**: 
- Verify session was created successfully
- Check app_name, user_id, and session_id match
- Ensure session service is properly configured

#### 2. Template Variables Not Replaced
**Problem**: Template variables appear unchanged in agent instructions
**Solution**:
- Verify template variable names match session state keys
- Check that session state contains the expected data
- Ensure runner is using the correct session service

#### 3. State Not Persisting
**Problem**: Session state is lost between interactions
**Solution**:
- Use the same session_id for multiple interactions
- Verify session service is properly configured
- Check for session expiration or cleanup

#### 4. Memory Issues
**Problem**: High memory usage with many sessions
**Solution**:
- Implement session cleanup for old sessions
- Use database-backed session service for production
- Monitor session count and memory usage

#### 5. API Key Errors
**Problem**: Authentication failures
**Solution**:
- Verify GOOGLE_API_KEY is set correctly
- Check API key permissions and quotas
- Ensure .env file is in the correct location

### Debugging Tips

1. **Print session state**: Always log session contents for debugging
2. **Verify template variables**: Check that variable names match state keys
3. **Test with simple state**: Start with basic state structure
4. **Monitor session lifecycle**: Track session creation and retrieval
5. **Check error messages**: Look for specific error details

## Best Practices

### 1. State Design
- **Use descriptive keys**: Make state keys self-explanatory
- **Structure data logically**: Organize related information together
- **Keep state minimal**: Only store necessary information
- **Use consistent naming**: Follow naming conventions

### 2. Session Management
- **Generate unique IDs**: Use UUID for session identification
- **Handle session cleanup**: Implement proper session lifecycle management
- **Monitor session count**: Track active sessions to prevent memory issues
- **Use appropriate storage**: Choose storage backend based on requirements

### 3. Template Variables
- **Use clear names**: Make template variables descriptive
- **Validate state**: Ensure required state fields exist
- **Handle missing data**: Provide fallbacks for missing state values
- **Test thoroughly**: Verify template variable replacement works correctly

### 4. Error Handling
- **Catch session errors**: Handle session creation and retrieval failures
- **Validate state**: Check state structure and content
- **Provide fallbacks**: Handle missing or invalid state gracefully
- **Log errors**: Record issues for debugging

### 5. Security Considerations
- **Sanitize state data**: Validate and clean user-provided data
- **Limit state size**: Prevent excessive memory usage
- **Secure storage**: Use appropriate security measures for sensitive data
- **Session isolation**: Ensure sessions are properly isolated

## Extending the Example

### 1. Adding New State Fields
```python
# Add new fields to initial state
initial_state = {
    "user_name": "shrihari nair",
    "user_preferences": "...",
    "last_interaction": datetime.now().isoformat(),
    "interaction_count": 0,
    "preferred_language": "English",
    "timezone": "America/Los_Angeles"
}
```

### 2. Creating State Update Functions
```python
def update_user_preferences(session, new_preferences):
    """Update user preferences in session state"""
    session.state["user_preferences"] = new_preferences
    session.state["last_updated"] = datetime.now().isoformat()

def increment_interaction_count(session):
    """Increment interaction counter"""
    current_count = session.state.get("interaction_count", 0)
    session.state["interaction_count"] = current_count + 1
```

### 3. Implementing Session Cleanup
```python
def cleanup_old_sessions(session_service, max_age_hours=24):
    """Remove sessions older than specified age"""
    current_time = datetime.now()
    for session in session_service.list_sessions():
        created_time = datetime.fromisoformat(session.created_at)
        if (current_time - created_time).total_seconds() > max_age_hours * 3600:
            session_service.delete_session(session.session_id)
```

### 4. Adding Database Storage
```python
from google.adk.sessions import DatabaseSessionService

# Use database-backed session service for production
database_session_service = DatabaseSessionService(
    database_url="postgresql://user:password@localhost/adk_sessions"
)
```

### 5. Creating Multi-User Applications
```python
def create_user_session(user_id, user_data):
    """Create session for specific user"""
    session_id = str(uuid.uuid4())
    initial_state = {
        "user_id": user_id,
        "user_data": user_data,
        "created_at": datetime.now().isoformat(),
        "last_active": datetime.now().isoformat()
    }
    
    return session_service.create_session(
        app_name="multi_user_app",
        user_id=user_id,
        session_id=session_id,
        state=initial_state
    )
```

## Conclusion

Stateful sessions are a powerful feature that enables building sophisticated, personalized AI applications. This example demonstrates the fundamental concepts and provides a foundation for creating more complex stateful applications.

Key takeaways:
- **Session management** enables context persistence
- **Template variables** provide dynamic, personalized content
- **State design** is crucial for effective applications
- **Proper error handling** ensures robust applications
- **Security considerations** are important for production use

Use this example as a starting point for building your own stateful AI applications! 
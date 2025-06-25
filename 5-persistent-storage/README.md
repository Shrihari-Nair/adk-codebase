# Persistent Storage Example - Database-Backed Sessions

This example demonstrates advanced persistent storage capabilities in ADK using database-backed session services. Unlike in-memory sessions, this implementation stores all session data in a SQLite database, ensuring data persistence across application restarts.

## Overview

This persistent storage example showcases:
- **Database-Backed Sessions**: SQLite database for persistent data storage
- **Smart Reminder Management**: Full CRUD operations for reminders
- **Session Continuity**: Resume conversations across application restarts
- **Interactive CLI**: Rich terminal interface with colored output
- **State Visualization**: Real-time display of session state changes
- **Tool Integration**: Custom tools for state manipulation

## Prerequisites

1. **Python 3.8 or higher**
2. **Google API key for Gemini model**
3. **Understanding of stateful sessions** (from previous example)

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Configuration
Create a `.env` file in the `5-persistent-storage` directory:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 3. Database Setup
The SQLite database (`my_agent_data.db`) will be created automatically on first run.

## Project Structure

```
5-persistent-storage/
├── main.py                    # Main execution script with session management
├── utils.py                   # Utility functions for CLI and state display
├── memory_agent/              # Agent package directory
│   ├── __init__.py           # Imports the agent module
│   └── agent.py              # Agent definition with custom tools
├── my_agent_data.db          # SQLite database (created automatically)
└── README.md                 # This guide
```

## Key Components

### 1. Database Session Service
```python
db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)
```
- Creates a database-backed session service using SQLite
- Automatically creates database tables and schema
- Provides persistent storage for all session data

### 2. Session Discovery and Continuity
```python
existing_sessions = session_service.list_sessions(app_name=APP_NAME, user_id=USER_ID)
if existing_sessions and len(existing_sessions.sessions) > 0:
    SESSION_ID = existing_sessions.sessions[0].id  # Continue existing session
else:
    new_session = session_service.create_session(...)  # Create new session
```
- Automatically finds existing sessions
- Resumes previous conversations
- Creates new sessions when needed

### 3. Agent Tools
The agent includes five custom tools for state management:

#### Add Reminder Tool
```python
def add_reminder(reminder: str, tool_context: ToolContext) -> dict:
    reminders = tool_context.state.get("reminders", [])
    reminders.append(reminder)
    tool_context.state["reminders"] = reminders
    return {"action": "add_reminder", "reminder": reminder}
```

#### View Reminders Tool
```python
def view_reminders(tool_context: ToolContext) -> dict:
    reminders = tool_context.state.get("reminders", [])
    return {"action": "view_reminders", "reminders": reminders, "count": len(reminders)}
```

#### Update Reminder Tool
```python
def update_reminder(index: int, updated_text: str, tool_context: ToolContext) -> dict:
    reminders = tool_context.state.get("reminders", [])
    if 1 <= index <= len(reminders):
        reminders[index - 1] = updated_text
        tool_context.state["reminders"] = reminders
        return {"action": "update_reminder", "index": index, "updated_text": updated_text}
```

#### Delete Reminder Tool
```python
def delete_reminder(index: int, tool_context: ToolContext) -> dict:
    reminders = tool_context.state.get("reminders", [])
    if 1 <= index <= len(reminders):
        deleted_reminder = reminders.pop(index - 1)
        tool_context.state["reminders"] = reminders
        return {"action": "delete_reminder", "index": index, "deleted_reminder": deleted_reminder}
```

#### Update User Name Tool
```python
def update_user_name(name: str, tool_context: ToolContext) -> dict:
    old_name = tool_context.state.get("user_name", "")
    tool_context.state["user_name"] = name
    return {"action": "update_user_name", "old_name": old_name, "new_name": name}
```

### 4. Interactive CLI Interface
- **Colored Output**: ANSI color codes for better readability
- **State Visualization**: Before/after state display
- **Event Processing**: Detailed event logging
- **Error Handling**: Graceful error management

## Running the Example

### 1. Navigate to Directory
```bash
cd 5-persistent-storage
```

### 2. Execute the Script
```bash
python main.py
```

### 3. Interactive Session
```
Welcome to Memory Agent Chat!
Your reminders will be remembered across conversations.
Type 'exit' or 'quit' to end the conversation.

You: Hi, my name is John
[Agent processes and updates name]

You: Add a reminder to buy groceries
[Agent adds reminder to state]

You: What are my reminders?
[Agent displays current reminders]

You: exit
Ending conversation. Your data has been saved to the database.
```

## Understanding the Output

### Session Management Messages
- **"Created new session: [ID]"**: New session created
- **"Continuing existing session: [ID]"**: Resuming previous session

### State Visualization
```
---------- State BEFORE processing ----------
👤 User: John
📝 Reminders: None
------------------------------------------

---------- State AFTER processing ----------
👤 User: John
📝 Reminders:
  1. buy groceries
  2. call mom
------------------------------------------
```

### Agent Responses
```
╔══ AGENT RESPONSE ═════════════════════════════════════════
Hello John! I've added a reminder to buy groceries. 
I can remember your information across conversations.
╚═════════════════════════════════════════════════════════════
```

## Advanced Features

### 1. Session Continuity
- **Automatic Discovery**: Finds existing sessions
- **State Restoration**: Resumes previous conversations
- **User Recognition**: Remembers user preferences
- **Data Persistence**: Survives application restarts

### 2. Smart Reminder Management
- **Natural Language**: "Add a reminder to buy milk"
- **Content Matching**: "Delete my meeting reminder"
- **Index Support**: "Update reminder 2 to call mom"
- **Relative Positions**: "Delete the first reminder"

### 3. Database Operations
- **Automatic Schema**: Tables created automatically
- **Transaction Support**: ACID compliance
- **Connection Management**: Efficient database access
- **Data Integrity**: Consistent state storage

## Use Cases

### 1. Personal Assistant Applications
- Remember user preferences and habits
- Track daily tasks and reminders
- Maintain conversation context
- Provide personalized responses

### 2. Customer Support Systems
- Store customer information and history
- Track support ticket progress
- Remember previous interactions
- Provide consistent service experience

### 3. Task Management Systems
- Store and manage user tasks
- Track task completion status
- Maintain task priorities
- Provide task recommendations

## Troubleshooting

### Common Issues and Solutions

#### 1. Database Connection Errors
**Problem**: `DatabaseConnectionError` or similar
**Solution**:
- Verify SQLite is installed
- Check file permissions for database directory
- Ensure sufficient disk space

#### 2. Session Not Found
**Problem**: Session not persisting between runs
**Solution**:
- Check database file exists and is writable
- Verify session creation was successful
- Ensure consistent app_name and user_id

#### 3. Tool Execution Errors
**Problem**: Tools not updating state correctly
**Solution**:
- Verify tool_context parameter is passed
- Check state field names match expectations
- Ensure proper error handling in tools

### Debugging Tips

1. **Check Database File**: Verify `my_agent_data.db` exists and has content
2. **Monitor State Changes**: Use the before/after state display
3. **Check Tool Execution**: Look for tool call messages in output
4. **Verify Session IDs**: Ensure consistent session identification

## Best Practices

### 1. Database Management
- **Regular Backups**: Backup database file regularly
- **Size Monitoring**: Monitor database file size
- **Cleanup Procedures**: Implement session cleanup for old data

### 2. State Design
- **Minimal State**: Only store necessary information
- **Structured Data**: Use consistent data structures
- **Validation**: Validate state data before storage

### 3. Tool Implementation
- **Error Handling**: Implement proper error handling in tools
- **State Validation**: Validate state before modifications
- **Return Values**: Provide meaningful return values

### 4. Security Considerations
- **Data Sanitization**: Validate and sanitize user input
- **Access Control**: Implement appropriate access controls
- **Data Encryption**: Consider encryption for sensitive data

## Extending the Example

### 1. Adding New State Fields
```python
initial_state = {
    "user_name": "Shrihari",
    "reminders": [],
    "preferences": {
        "language": "English",
        "timezone": "America/Los_Angeles"
    },
    "conversation_history": []
}
```

### 2. Creating New Tools
```python
def add_preference(key: str, value: str, tool_context: ToolContext) -> dict:
    """Add or update user preference"""
    preferences = tool_context.state.get("preferences", {})
    preferences[key] = value
    tool_context.state["preferences"] = preferences
    return {"action": "add_preference", "key": key, "value": value}
```

### 3. Implementing Session Cleanup
```python
def cleanup_old_sessions(session_service, max_age_days=30):
    """Remove sessions older than specified age"""
    from datetime import datetime, timedelta
    
    cutoff_date = datetime.now() - timedelta(days=max_age_days)
    sessions = session_service.list_sessions()
    
    for session in sessions.sessions:
        created_date = datetime.fromisoformat(session.created_at.replace('Z', '+00:00'))
        if created_date < cutoff_date:
            session_service.delete_session(session.id)
```

## Conclusion

This persistent storage example demonstrates how to build production-ready applications with ADK using database-backed session services. Key takeaways:

- **Database Integration**: Use DatabaseSessionService for persistent storage
- **Session Continuity**: Implement session discovery and restoration
- **Tool Development**: Create custom tools for state management
- **User Experience**: Build rich interactive interfaces
- **Data Persistence**: Ensure data survives application restarts

Use this example as a foundation for building sophisticated, persistent AI applications that can handle real-world usage patterns and provide reliable data storage.

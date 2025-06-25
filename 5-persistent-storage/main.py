# Persistent Storage Example - Main Execution Script
# This script demonstrates database-backed session management with ADK
# It creates persistent sessions that survive application restarts

import asyncio  # For asynchronous execution

# Import environment variable management
from dotenv import load_dotenv

# Import ADK components for running agents and managing sessions
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService

# Import our custom memory agent
from memory_agent.agent import memory_agent

# Import utility functions for agent interaction and state display
from utils import call_agent_async

# Load environment variables from .env file
load_dotenv()

# ===== PART 1: Initialize Persistent Session Service =====
# Using SQLite database for persistent storage instead of in-memory storage
# This ensures data survives application restarts and crashes
db_url = "sqlite:///./my_agent_data.db"  # SQLite database file in current directory
session_service = DatabaseSessionService(db_url=db_url)  # Create database-backed session service


# ===== PART 2: Define Initial State =====
# This state will only be used when creating a new session
# For existing sessions, the stored state will be loaded from the database
initial_state = {
    "user_name": "Shrihari",  # Default user name
    "reminders": [],          # Empty list to store user reminders
}


async def main_async():
    """Main asynchronous function that orchestrates the persistent storage example."""
    
    # Setup constants for session management
    APP_NAME = "Memory Agent"  # Application identifier
    USER_ID = "shrihari"       # User identifier

    # ===== PART 3: Session Management - Find or Create =====
    # Check for existing sessions for this user in the database
    # This enables session continuity across application restarts
    existing_sessions = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    # If there's an existing session, use it, otherwise create a new one
    # This provides seamless user experience across restarts
    if existing_sessions and len(existing_sessions.sessions) > 0:
        # Use the most recent session (first in the list)
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Continuing existing session: {SESSION_ID}")
        print("Your previous data and reminders have been restored!")
    else:
        # Create a new session with initial state
        # This happens for first-time users or when no sessions exist
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,  # Pass the initial state
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")
        print("Welcome! Starting fresh with a new session.")

    # ===== PART 4: Agent Runner Setup =====
    # Create a runner with the memory agent and database session service
    # The runner manages the interaction between the agent and persistent storage
    runner = Runner(
        agent=memory_agent,                    # Our custom memory agent
        app_name=APP_NAME,                     # Must match session app_name
        session_service=session_service,       # Database-backed session service
    )

    # ===== PART 5: Interactive Conversation Loop =====
    # Provide user-friendly interface and instructions
    print("\nWelcome to Memory Agent Chat!")
    print("Your reminders will be remembered across conversations.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    # Main conversation loop - continues until user exits
    while True:
        # Get user input from command line
        user_input = input("You: ")

        # Check if user wants to exit the conversation
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Your data has been saved to the database.")
            print("You can restart the application and your data will be restored!")
            break

        # Process the user query through the agent asynchronously
        # This handles the agent execution and state updates
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)


# Entry point for the script
if __name__ == "__main__":
    # Run the main asynchronous function
    # This starts the persistent storage example
    asyncio.run(main_async())
# Import required libraries for session management and state handling
import uuid  # For generating unique session IDs

# Import environment variable loading functionality
from dotenv import load_dotenv

# Import ADK components for running agents and managing sessions
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

# Import Google GenAI types for message handling
from google.genai import types

# Import our custom question answering agent
from question_answering_agent.agent import question_answering_agent

# Load environment variables from .env file
load_dotenv()


# --- Session Service Setup ---
# Create an in-memory session service to store conversation state
# This service will persist data across multiple interactions
session_service_stateful = InMemorySessionService()

# --- Initial State Definition ---
# Define the initial state that will be stored in the session
# This state contains user information that the agent can access
initial_state = {
    # Store the user's name for personalization
    "user_name": "shrihari nair",
    
    # Store user preferences as a multi-line string
    # This information will be available to the agent during conversations
    "user_preferences": """
        I like to play Pickleball, Disc Golf, and Tennis.
        My favorite food is Mexican.
        My favorite TV show is Game of Thrones.
        Loves it when people like and subscribe to his YouTube channel.
    """,
}

# --- Session Creation ---
# Define session parameters
APP_NAME = "shrihari_bot"      # Name of the application
USER_ID = "shrihari_nair"      # Unique identifier for the user
SESSION_ID = str(uuid.uuid4()) # Generate a unique session ID

# Create a new session with the initial state
# This session will persist across multiple interactions
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,  # Pass the initial state to the session
)

# Print session creation confirmation
print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

# --- Runner Setup ---
# Create a runner that will execute the agent with session management
runner = Runner(
    agent=question_answering_agent,  # The agent to run
    app_name=APP_NAME,               # Application name
    session_service=session_service_stateful,  # Session service for state management
)

# --- Message Creation ---
# Create a user message to send to the agent
new_message = types.Content(
    role="user",  # Specify that this is a user message
    parts=[types.Part(text="What is shrihari's favorite TV show?")]  # The actual message content
)

# --- Agent Execution ---
# Run the agent with the session and message
# This will process the message and maintain state
for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    # Check if this is the final response from the agent
    if event.is_final_response():
        # Extract and print the agent's response
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

# --- Session State Exploration ---
print("==== Session Event Exploration ====")

# Retrieve the current session to examine its state
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# --- Final State Logging ---
# Print the final state of the session after the interaction
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")
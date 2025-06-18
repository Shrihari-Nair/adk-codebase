# Import the Agent class from Google's ADK
# This is the main class for creating agents
from google.adk.agents import Agent

# Create the root agent for question answering
# This agent will have access to session state and can answer questions about user preferences
question_answering_agent = Agent(
    # A unique identifier for this agent
    name="question_answering_agent",
    
    # Specify which LLM to use for processing
    # gemini-2.0-flash is a fast and efficient model from Google
    model="gemini-2.0-flash",
    
    # A brief description of what this agent does
    # This helps other agents understand when to route tasks to this agent
    description="Question answering agent",
    
    # The core instructions that define the agent's behavior
    # This template uses placeholders that will be filled with session state
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
    # Note: {user_name} and {user_preferences} are template variables
    # that will be automatically replaced with values from the session state
    # when the agent processes a message
)
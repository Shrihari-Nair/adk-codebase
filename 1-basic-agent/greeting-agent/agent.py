# Import the Agent class from Google's ADK (Agent Development Kit)
# This is the main class we'll use to create our agent
from google.adk.agents import Agent

# Create an instance of the Agent class
# This is the root agent that will handle all interactions
root_agent = Agent(
    # A unique identifier for this agent
    # This name will appear in the web UI dropdown menu
    name="greeting_agent",

    # Specify which LLM (Large Language Model) to use
    # gemini-2.0-flash is a fast and efficient model from Google
    # More models can be found at: https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",

    # A brief description of what this agent does
    # This helps other agents understand when to route tasks to this agent
    description="Greeting agent",

    # The core instructions that define the agent's behavior
    # This is where we tell the agent how to interact with users
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)
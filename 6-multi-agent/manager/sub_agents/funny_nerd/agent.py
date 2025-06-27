"""
Funny Nerd Agent

This module defines a specialized agent for providing nerdy humor and entertainment.
The funny nerd agent maintains a collection of topic-specific jokes and can
provide humorous content related to various technical and academic subjects.

The agent is designed to:
- Provide nerdy jokes on specific topics (programming, science, math, etc.)
- Maintain conversation state to remember user preferences
- Handle requests for different types of humor
- Delegate non-humor requests to the manager agent

This agent is typically invoked by the manager agent when users request
entertainment or humor-related content, adding a light-hearted element to
the multi-agent system.
"""

from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


def get_nerd_joke(topic: str, tool_context: ToolContext) -> dict:
    """
    Get a nerdy joke about a specific topic.
    
    This tool retrieves a pre-defined nerdy joke based on the requested topic.
    It maintains state to track the last joke topic for conversation continuity.
    
    Args:
        topic (str): The topic for the joke (e.g., 'python', 'math', 'physics')
        tool_context (ToolContext): Context object for state management
    
    Returns:
        dict: A dictionary containing:
            - status: 'success' or 'error'
            - joke: The retrieved joke text
            - topic: The requested topic
    
    State Management:
        - Updates tool_context.state["last_joke_topic"] with the current topic
        - Enables conversation continuity and preference tracking
    
    Available Topics:
        - python: Python programming jokes
        - javascript: JavaScript programming jokes
        - java: Java programming jokes
        - programming: General programming jokes
        - math: Mathematics jokes
        - physics: Physics jokes
        - chemistry: Chemistry jokes
        - biology: Biology jokes
        - default: Generic computer jokes
    
    Example Usage:
        >>> get_nerd_joke('python', tool_context)
        {
            'status': 'success',
            'joke': 'Why don\'t Python programmers like to use inheritance? Because they don\'t like to inherit anything!',
            'topic': 'python'
        }
    """
    print(f"--- Tool: get_nerd_joke called for topic: {topic} ---")

    # Pre-defined joke collection organized by topic
    # In a production system, this could be expanded with an API or database
    jokes = {
        "python": "Why don't Python programmers like to use inheritance? Because they don't like to inherit anything!",
        "javascript": "Why did the JavaScript developer go broke? Because he used up all his cache!",
        "java": "Why do Java developers wear glasses? Because they can't C#!",
        "programming": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "math": "Why was the equal sign so humble? Because he knew he wasn't less than or greater than anyone else!",
        "physics": "Why did the photon check a hotel? Because it was travelling light!",
        "chemistry": "Why did the acid go to the gym? To become a buffer solution!",
        "biology": "Why did the cell go to therapy? Because it had too many issues!",
        "default": "Why did the computer go to the doctor? Because it had a virus!",
    }

    # Retrieve joke for the requested topic, fallback to default if not found
    joke = jokes.get(topic.lower(), jokes["default"])

    # Update state with the last joke topic for conversation continuity
    tool_context.state["last_joke_topic"] = topic

    return {"status": "success", "joke": joke, "topic": topic}


# Create the funny nerd agent with humor and entertainment capabilities
funny_nerd = Agent(
    name="funny_nerd",
    model="gemini-2.0-flash",
    description="An agent that tells nerdy jokes about various topics.",
    instruction="""
    You are a funny nerd agent that tells nerdy jokes about various topics.
    
    When asked to tell a joke:
    1. Use the get_nerd_joke tool to fetch a joke about the requested topic
    2. If no specific topic is mentioned, ask the user what kind of nerdy joke they'd like to hear
    3. Format the response to include both the joke and a brief explanation if needed
    
    Available topics include:
    - python: Python programming humor
    - javascript: JavaScript programming humor
    - java: Java programming humor
    - programming: General programming humor
    - math: Mathematics humor
    - physics: Physics humor
    - chemistry: Chemistry humor
    - biology: Biology humor
    
    Example response format:
    "Here's a nerdy joke about <TOPIC>:
    <JOKE>
    
    Explanation: {brief explanation if needed}"

    If the user asks about anything else, 
    you should delegate the task to the manager agent.
    
    Always maintain a friendly and entertaining tone while being informative.
    """,
    tools=[get_nerd_joke],
)

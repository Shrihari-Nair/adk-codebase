# Memory Agent - Persistent Storage Agent with Custom Tools
# This agent demonstrates how to create custom tools that can read and write session state
# It provides a complete reminder management system with persistent storage

from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


def add_reminder(reminder: str, tool_context: ToolContext) -> dict:
    """
    Add a new reminder to the user's reminder list.
    
    This tool demonstrates how to read from and write to session state.
    It retrieves the current reminders list, adds a new reminder, and
    updates the session state with the modified list.
    
    Args:
        reminder: The reminder text to add to the user's list
        tool_context: Context object that provides access to session state
        
    Returns:
        dict: A confirmation message with the action performed and reminder added
    """
    print(f"--- Tool: add_reminder called for '{reminder}' ---")

    # Get current reminders from session state
    # Use .get() with default empty list to handle cases where reminders don't exist yet
    reminders = tool_context.state.get("reminders", [])

    # Add the new reminder to the list
    reminders.append(reminder)

    # Update the session state with the new list of reminders
    # This change will be automatically persisted to the database
    tool_context.state["reminders"] = reminders

    # Return a structured response that the agent can use
    return {
        "action": "add_reminder",
        "reminder": reminder,
        "message": f"Added reminder: {reminder}",
    }


def view_reminders(tool_context: ToolContext) -> dict:
    """
    View all current reminders in the user's list.
    
    This tool demonstrates how to read from session state without modifying it.
    It retrieves the current reminders list and returns it along with a count.
    
    Args:
        tool_context: Context object that provides access to session state
        
    Returns:
        dict: The list of reminders and count, along with the action performed
    """
    print("--- Tool: view_reminders called ---")

    # Get reminders from session state
    # Use .get() with default empty list to handle cases where reminders don't exist yet
    reminders = tool_context.state.get("reminders", [])

    # Return the reminders list and count for the agent to use
    return {
        "action": "view_reminders", 
        "reminders": reminders, 
        "count": len(reminders)
    }


def update_reminder(index: int, updated_text: str, tool_context: ToolContext) -> dict:
    """
    Update an existing reminder in the user's list.
    
    This tool demonstrates how to modify existing data in session state.
    It validates the index, updates the reminder, and persists the change.
    
    Args:
        index: The 1-based index of the reminder to update (user-friendly indexing)
        updated_text: The new text for the reminder
        tool_context: Context object that provides access to session state
        
    Returns:
        dict: A confirmation message with the action performed and update details
    """
    print(
        f"--- Tool: update_reminder called for index {index} with '{updated_text}' ---"
    )

    # Get current reminders from session state
    reminders = tool_context.state.get("reminders", [])

    # Check if the index is valid (1-based indexing for user-friendliness)
    # Validate that the list exists, index is at least 1, and index is within bounds
    if not reminders or index < 1 or index > len(reminders):
        return {
            "action": "update_reminder",
            "status": "error",
            "message": f"Could not find reminder at position {index}. Currently there are {len(reminders)} reminders.",
        }

    # Update the reminder (adjusting for 0-based list indexing)
    # Store the old reminder text for the response
    old_reminder = reminders[index - 1]
    reminders[index - 1] = updated_text

    # Update the session state with the modified list
    # This change will be automatically persisted to the database
    tool_context.state["reminders"] = reminders

    # Return a structured response with the update details
    return {
        "action": "update_reminder",
        "index": index,
        "old_text": old_reminder,
        "updated_text": updated_text,
        "message": f"Updated reminder {index} from '{old_reminder}' to '{updated_text}'",
    }


def delete_reminder(index: int, tool_context: ToolContext) -> dict:
    """
    Delete a reminder from the user's list.
    
    This tool demonstrates how to remove data from session state.
    It validates the index, removes the reminder, and persists the change.
    
    Args:
        index: The 1-based index of the reminder to delete (user-friendly indexing)
        tool_context: Context object that provides access to session state
        
    Returns:
        dict: A confirmation message with the action performed and deletion details
    """
    print(f"--- Tool: delete_reminder called for index {index} ---")

    # Get current reminders from session state
    reminders = tool_context.state.get("reminders", [])

    # Check if the index is valid (1-based indexing for user-friendliness)
    # Validate that the list exists, index is at least 1, and index is within bounds
    if not reminders or index < 1 or index > len(reminders):
        return {
            "action": "delete_reminder",
            "status": "error",
            "message": f"Could not find reminder at position {index}. Currently there are {len(reminders)} reminders.",
        }

    # Remove the reminder (adjusting for 0-based list indexing)
    # Store the deleted reminder text for the response
    deleted_reminder = reminders.pop(index - 1)

    # Update the session state with the modified list
    # This change will be automatically persisted to the database
    tool_context.state["reminders"] = reminders

    # Return a structured response with the deletion details
    return {
        "action": "delete_reminder",
        "index": index,
        "deleted_reminder": deleted_reminder,
        "message": f"Deleted reminder {index}: '{deleted_reminder}'",
    }


def update_user_name(name: str, tool_context: ToolContext) -> dict:
    """
    Update the user's name in the session state.
    
    This tool demonstrates how to update simple string values in session state.
    It stores the old name and updates to the new name.
    
    Args:
        name: The new name for the user
        tool_context: Context object that provides access to session state
        
    Returns:
        dict: A confirmation message with the action performed and name change details
    """
    print(f"--- Tool: update_user_name called with '{name}' ---")

    # Get current name from session state
    # Use .get() with default empty string to handle cases where name doesn't exist yet
    old_name = tool_context.state.get("user_name", "")

    # Update the name in session state
    # This change will be automatically persisted to the database
    tool_context.state["user_name"] = name

    # Return a structured response with the name change details
    return {
        "action": "update_user_name",
        "old_name": old_name,
        "new_name": name,
        "message": f"Updated your name to: {name}",
    }


# Create the persistent memory agent with custom tools
# This agent combines natural language understanding with state management capabilities
memory_agent = Agent(
    # Basic agent configuration
    name="memory_agent",
    model="gemini-2.0-flash",  # Fast and efficient model for real-time interactions
    description="A smart reminder agent with persistent memory",
    
    # Core instructions that define the agent's behavior and capabilities
    instruction="""
    You are a friendly reminder assistant that remembers users across conversations.
    
    The user's information is stored in state:
    - User's name: {user_name}
    - Reminders: {reminders}
    
    You can help users manage their reminders with the following capabilities:
    1. Add new reminders
    2. View existing reminders
    3. Update reminders
    4. Delete reminders
    5. Update the user's name
    
    Always be friendly and address the user by name. If you don't know their name yet,
    use the update_user_name tool to store it when they introduce themselves.
    
    **REMINDER MANAGEMENT GUIDELINES:**
    
    When dealing with reminders, you need to be smart about finding the right reminder:
    
    1. When the user asks to update or delete a reminder but doesn't provide an index:
       - If they mention the content of the reminder (e.g., "delete my meeting reminder"), 
         look through the reminders to find a match
       - If you find an exact or close match, use that index
       - Never clarify which reminder the user is referring to, just use the first match
       - If no match is found, list all reminders and ask the user to specify
    
    2. When the user mentions a number or position:
       - Use that as the index (e.g., "delete reminder 2" means index=2)
       - Remember that indexing starts at 1 for the user
    
    3. For relative positions:
       - Handle "first", "last", "second", etc. appropriately
       - "First reminder" = index 1
       - "Last reminder" = the highest index
       - "Second reminder" = index 2, and so on
    
    4. For viewing:
       - Always use the view_reminders tool when the user asks to see their reminders
       - Format the response in a numbered list for clarity
       - If there are no reminders, suggest adding some
    
    5. For addition:
       - Extract the actual reminder text from the user's request
       - Remove phrases like "add a reminder to" or "remind me to"
       - Focus on the task itself (e.g., "add a reminder to buy milk" → add_reminder("buy milk"))
    
    6. For updates:
       - Identify both which reminder to update and what the new text should be
       - For example, "change my second reminder to pick up groceries" → update_reminder(2, "pick up groceries")
    
    7. For deletions:
       - Confirm deletion when complete and mention which reminder was removed
       - For example, "I've deleted your reminder to 'buy milk'"
    
    Remember to explain that you can remember their information across conversations.

    IMPORTANT:
    - use your best judgement to determine which reminder the user is referring to. 
    - You don't have to be 100% correct, but try to be as close as possible.
    - Never ask the user to clarify which reminder they are referring to.
    """,
    
    # List of custom tools that the agent can use
    # These tools provide the agent with the ability to read and write session state
    tools=[
        add_reminder,      # Tool to add new reminders
        view_reminders,    # Tool to view all reminders
        update_reminder,   # Tool to update existing reminders
        delete_reminder,   # Tool to delete reminders
        update_user_name,  # Tool to update user's name
    ],
)
# Utility Functions for Persistent Storage Example
# This module provides helper functions for CLI interaction, state visualization, and agent communication

from google.genai import types  # For creating message content


# ANSI color codes for terminal output
# These provide rich formatting for better user experience
class Colors:
    """ANSI color codes for terminal output formatting."""
    
    # Reset all formatting
    RESET = "\033[0m"
    
    # Text formatting
    BOLD = "\033[1m"        # Make text bold
    UNDERLINE = "\033[4m"   # Underline text

    # Foreground colors (text colors)
    BLACK = "\033[30m"      # Black text
    RED = "\033[31m"        # Red text
    GREEN = "\033[32m"      # Green text
    YELLOW = "\033[33m"     # Yellow text
    BLUE = "\033[34m"       # Blue text
    MAGENTA = "\033[35m"    # Magenta text
    CYAN = "\033[36m"       # Cyan text
    WHITE = "\033[37m"      # White text

    # Background colors
    BG_BLACK = "\033[40m"   # Black background
    BG_RED = "\033[41m"     # Red background
    BG_GREEN = "\033[42m"   # Green background
    BG_YELLOW = "\033[43m"  # Yellow background
    BG_BLUE = "\033[44m"    # Blue background
    BG_MAGENTA = "\033[45m" # Magenta background
    BG_CYAN = "\033[46m"    # Cyan background
    BG_WHITE = "\033[47m"   # White background


def display_state(
    session_service, app_name, user_id, session_id, label="Current State"
):
    """
    Display the current session state in a formatted way.
    
    This function retrieves the session from the database and displays
    the user information and reminders in a user-friendly format.
    
    Args:
        session_service: The database session service
        app_name: Application name for session lookup
        user_id: User ID for session lookup
        session_id: Session ID for session lookup
        label: Label to display above the state information
    """
    try:
        # Retrieve the session from the database
        session = session_service.get_session(
            app_name=app_name, user_id=user_id, session_id=session_id
        )

        # Format the output with clear sections and visual separators
        print(f"\n{'-' * 10} {label} {'-' * 10}")

        # Display user information
        # Get user name from state, default to "Unknown" if not found
        user_name = session.state.get("user_name", "Unknown")
        print(f"👤 User: {user_name}")

        # Display reminders
        # Get reminders list from state, default to empty list if not found
        reminders = session.state.get("reminders", [])
        if reminders:
            print("📝 Reminders:")
            # Display each reminder with a numbered list (1-based indexing for user-friendliness)
            for idx, reminder in enumerate(reminders, 1):
                print(f"  {idx}. {reminder}")
        else:
            print("📝 Reminders: None")

        # Add visual separator at the end
        print("-" * (22 + len(label)))
        
    except Exception as e:
        # Handle any errors that occur during state retrieval or display
        print(f"Error displaying state: {e}")


async def process_agent_response(event):
    """
    Process and display agent response events.
    
    This function handles different types of events from the agent,
    including tool executions, code generation, and final responses.
    It provides detailed logging and formatted output for better debugging.
    
    Args:
        event: The event object from the agent runner
        
    Returns:
        str or None: The final response text if available, None otherwise
    """
    # Log basic event information for debugging
    print(f"Event ID: {event.id}, Author: {event.author}")

    # Check for specific parts first (tools, code execution, etc.)
    has_specific_part = False
    
    if event.content and event.content.parts:
        for part in event.content.parts:
            # Handle executable code (when agent generates code)
            if hasattr(part, "executable_code") and part.executable_code:
                # Access the actual code string via .code
                print(
                    f"  Debug: Agent generated code:\n```python\n{part.executable_code.code}\n```"
                )
                has_specific_part = True
                
            # Handle code execution results (output from executed code)
            elif hasattr(part, "code_execution_result") and part.code_execution_result:
                # Access outcome and output correctly
                print(
                    f"  Debug: Code Execution Result: {part.code_execution_result.outcome} - Output:\n{part.code_execution_result.output}"
                )
                has_specific_part = True
                
            # Handle tool responses (output from tool execution)
            elif hasattr(part, "tool_response") and part.tool_response:
                # Print tool response information
                print(f"  Tool Response: {part.tool_response.output}")
                has_specific_part = True
                
            # Also print any text parts found in any event for debugging
            elif hasattr(part, "text") and part.text and not part.text.isspace():
                print(f"  Text: '{part.text.strip()}'")

    # Check for final response after specific parts
    # The final response contains the agent's main response to the user
    final_response = None
    if event.is_final_response():
        if (
            event.content
            and event.content.parts
            and hasattr(event.content.parts[0], "text")
            and event.content.parts[0].text
        ):
            # Extract the final response text
            final_response = event.content.parts[0].text.strip()
            
            # Use colors and formatting to make the final response stand out
            # This creates a visually appealing box around the agent's response
            print(
                f"\n{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD}╔══ AGENT RESPONSE ═════════════════════════════════════════{Colors.RESET}"
            )
            print(f"{Colors.CYAN}{Colors.BOLD}{final_response}{Colors.RESET}")
            print(
                f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD}╚═════════════════════════════════════════════════════════════{Colors.RESET}\n"
            )
        else:
            # Handle case where final response has no text content
            print(
                f"\n{Colors.BG_RED}{Colors.WHITE}{Colors.BOLD}==> Final Agent Response: [No text content in final event]{Colors.RESET}\n"
            )

    return final_response


async def call_agent_async(runner, user_id, session_id, query):
    """
    Call the agent asynchronously with the user's query.
    
    This function orchestrates the entire agent interaction process:
    1. Creates a message from the user's query
    2. Displays the current state before processing
    3. Runs the agent with the query
    4. Processes all events from the agent
    5. Displays the updated state after processing
    
    Args:
        runner: The agent runner instance
        user_id: User ID for the session
        session_id: Session ID for the session
        query: The user's input query
        
    Returns:
        str or None: The final response text from the agent
    """
    # Create a message object from the user's query
    # This formats the query for the agent to process
    content = types.Content(role="user", parts=[types.Part(text=query)])
    
    # Display the query being processed with visual formatting
    print(
        f"\n{Colors.BG_GREEN}{Colors.BLACK}{Colors.BOLD}--- Running Query: {query} ---{Colors.RESET}"
    )
    
    final_response_text = None

    # Display state before processing the message
    # This shows what the session state looks like before the agent processes the query
    display_state(
        runner.session_service,
        runner.app_name,
        user_id,
        session_id,
        "State BEFORE processing",
    )

    try:
        # Run the agent asynchronously with the user's query
        # This processes the query through the agent and updates the session state
        async for event in runner.run_async(
            user_id=user_id, session_id=session_id, new_message=content
        ):
            # Process each event and get the final response if available
            # Events can include tool executions, code generation, and the final response
            response = await process_agent_response(event)
            if response:
                final_response_text = response
                
    except Exception as e:
        # Handle any errors that occur during agent execution
        print(f"Error during agent call: {e}")

    # Display state after processing the message
    # This shows how the session state changed after the agent processed the query
    display_state(
        runner.session_service,
        runner.app_name,
        user_id,
        session_id,
        "State AFTER processing",
    )

    return final_response_text
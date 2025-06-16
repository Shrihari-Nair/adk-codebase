# Import the LlmAgent class from Google's ADK
# LlmAgent is used when we need structured output with a defined schema
from google.adk.agents import LlmAgent

# Import Pydantic's BaseModel and Field for creating structured data models
# BaseModel provides data validation and serialization
# Field allows us to add metadata to model fields
from pydantic import BaseModel, Field


# --- Define Output Schema ---
# This class defines the structure of the email output
# It inherits from BaseModel to get Pydantic's validation features
class EmailContent(BaseModel):
    # Define the subject field with validation and description
    # The Field class adds metadata to the field
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    
    # Define the body field with validation and description
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )


# --- Create Email Generator Agent ---
# Create an instance of LlmAgent (instead of regular Agent)
# LlmAgent is used when we need structured output with a defined schema
root_agent = LlmAgent(
    # A unique identifier for this agent
    name="email_agent",

    # Specify which LLM to use
    # gemini-2.0-flash is a fast and efficient model from Google
    model="gemini-2.0-flash",

    # Detailed instructions for the agent
    # These instructions tell the agent how to generate emails
    instruction="""
        You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }

        DO NOT include any explanations or additional text outside the JSON response.
    """,

    # A brief description of what this agent does
    description="Generates professional emails with structured subject and body",

    # Specify the output schema using our EmailContent Pydantic model
    # This ensures the agent's output matches our defined structure
    output_schema=EmailContent,

    # The key under which the output will be stored
    # This is used when the output is returned as part of a larger response
    output_key="email",
)
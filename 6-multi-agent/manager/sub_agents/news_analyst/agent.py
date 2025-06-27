"""
News Analyst Agent

This module defines a specialized agent for news analysis and information retrieval.
The news analyst agent leverages Google Search capabilities to find and analyze
current news articles and information on various topics.

The agent is designed to:
- Search for current news and information using Google Search
- Provide summaries and analysis of news articles
- Handle time-sensitive queries with current timestamp context
- Integrate with the multi-agent system for comprehensive information gathering

This agent is typically used as a tool by the manager agent when users request
news-related information or current events analysis.
"""

from google.adk.agents import Agent
from google.adk.tools import google_search

# Create the news analyst agent with search and analysis capabilities
news_analyst = Agent(
    name="news_analyst",
    model="gemini-2.0-flash",
    description="News analyst agent that searches for and analyzes current news and information",
    instruction="""
    You are a helpful assistant that can analyze news articles and provide a summary of the news.

    When asked about news, you should use the google_search tool to search for the news.

    If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query.
    
    Always provide:
    - Current and relevant information
    - Multiple sources when available
    - Context and background information
    - Timestamps for when information was retrieved
    """,
    tools=[google_search],
)

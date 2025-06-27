"""
Multi-Agent System Manager Agent

This module defines the main manager agent that orchestrates a multi-agent system
consisting of specialized sub-agents and tools. The manager acts as a coordinator
that delegates tasks to appropriate agents based on the nature of the request.

Architecture Overview:
- Manager Agent: Central coordinator that routes requests to appropriate sub-agents
- Sub-Agents: Specialized agents for specific domains (stock analysis, humor)
- Tools: Utility functions and external service integrations (news analysis, time)

The manager uses a delegation strategy to:
1. Analyze incoming requests
2. Determine the most appropriate agent or tool for the task
3. Route the request accordingly
4. Aggregate and present results to the user

This pattern enables complex workflows where different types of requests
are handled by domain-specific agents while maintaining a unified interface.
"""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# Import sub-agents for delegation
from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst

# Import utility tools
from .tools.tools import get_current_time

# Main manager agent that coordinates the multi-agent system
root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent that coordinates and delegates tasks to specialized sub-agents",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    # Sub-agents that can be delegated to directly
    sub_agents=[stock_analyst, funny_nerd],
    # Tools available for direct use by the manager
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)

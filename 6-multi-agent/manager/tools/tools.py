"""
Utility Tools Module for Multi-Agent System

This module provides utility functions that can be used across the multi-agent system.
These tools provide common functionality that multiple agents might need, such as
time retrieval, data formatting, and other shared utilities.

The tools in this module are designed to be:
- Stateless: No persistent state between calls
- Reusable: Can be used by multiple agents
- Simple: Focused on single, well-defined tasks
- Reliable: Handle errors gracefully and provide consistent output
"""

from datetime import datetime


def get_current_time() -> dict:
    """
    Get the current time in a standardized format.
    
    This tool provides the current system time in a consistent format that can be
    used across the multi-agent system for timestamping, logging, and time-based
    operations.
    
    Returns:
        dict: A dictionary containing the current time in YYYY-MM-DD HH:MM:SS format
              Example: {"current_time": "2024-04-21 16:30:00"}
    
    Use Cases:
        - Timestamping agent responses
        - Time-based search queries
        - Logging and debugging
        - Scheduling and time-sensitive operations
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

"""
Stock Analyst Agent

This module defines a specialized agent for stock market analysis and price tracking.
The stock analyst agent provides real-time stock price information and basic market
data using the Yahoo Finance API through the yfinance library.

The agent is designed to:
- Fetch current stock prices for any publicly traded company
- Provide timestamped price data for tracking purposes
- Handle errors gracefully when stock data is unavailable
- Format responses in a user-friendly manner

This agent is typically invoked by the manager agent when users request
stock-related information or market analysis.
"""

from datetime import datetime

import yfinance as yf
from google.adk.agents import Agent


def get_stock_price(ticker: str) -> dict:
    """
    Retrieves current stock price and saves to session state.
    
    This tool fetches real-time stock price data from Yahoo Finance for the
    specified ticker symbol. It handles various error conditions and provides
    consistent response formatting.
    
    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL', 'GOOGL', 'TSLA')
    
    Returns:
        dict: A dictionary containing:
            - status: 'success' or 'error'
            - ticker: The requested ticker symbol
            - price: Current stock price (if successful)
            - timestamp: When the price was fetched
            - error_message: Error details (if failed)
    
    Error Handling:
        - Invalid ticker symbols
        - Network connectivity issues
        - API rate limiting
        - Missing or unavailable stock data
    
    Example Usage:
        >>> get_stock_price('AAPL')
        {
            'status': 'success',
            'ticker': 'AAPL',
            'price': 175.34,
            'timestamp': '2024-04-21 16:30:00'
        }
    """
    print(f"--- Tool: get_stock_price called for {ticker} ---")

    try:
        # Fetch stock data using Yahoo Finance API
        stock = yf.Ticker(ticker)
        current_price = stock.info.get("currentPrice")

        if current_price is None:
            return {
                "status": "error",
                "error_message": f"Could not fetch price for {ticker}",
            }

        # Get current timestamp for data freshness tracking
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "status": "success",
            "ticker": ticker,
            "price": current_price,
            "timestamp": current_time,
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching stock data: {str(e)}",
        }


# Create the stock analyst agent with specialized stock market capabilities
stock_analyst = Agent(
    name="stock_analyst",
    model="gemini-2.0-flash",
    description="An agent that can look up stock prices and track them over time.",
    instruction="""
    You are a helpful stock market assistant that helps users track their stocks of interest.
    
    When asked about stock prices:
    1. Use the get_stock_price tool to fetch the latest price for the requested stock(s)
    2. Format the response to show each stock's current price and the time it was fetched
    3. If a stock price couldn't be fetched, mention this in your response
    
    Example response format:
    "Here are the current prices for your stocks:
    - GOOG: $175.34 (updated at 2024-04-21 16:30:00)
    - TSLA: $156.78 (updated at 2024-04-21 16:30:00)
    - META: $123.45 (updated at 2024-04-21 16:30:00)"
    
    Always provide context about the data freshness and mention that prices
    are real-time from Yahoo Finance.
    """,
    tools=[get_stock_price],
)

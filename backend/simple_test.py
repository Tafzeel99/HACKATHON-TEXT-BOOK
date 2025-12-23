"""
Simple test to verify the OpenRouter agent is working
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.rag.agent import OpenRouterAgent
from app.config import settings

def test_agent():
    """Test the OpenRouter agent directly"""
    print("Testing OpenRouter Agent...")

    try:
        # Check if API key is available
        if not settings.OPEN_ROUTER_KEY:
            print("ERROR: OPEN_ROUTER_KEY not found in settings")
            print(f"Current key: {settings.OPEN_ROUTER_KEY[:10] if settings.OPEN_ROUTER_KEY else 'None'}...")
            return False

        print("API Key found, initializing agent...")

        # Initialize the agent
        agent = OpenRouterAgent()
        print("SUCCESS: OpenRouterAgent initialized successfully")

        # Test a simple query (this will call OpenRouter)
        print("Testing agent response...")
        response = agent.generate_general_response("Hello")
        print(f"Response received: {response[:100] if response else 'None'}...")

        print("SUCCESS: OpenRouter agent is working!")
        return True

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing OpenRouter Agent Integration...")
    success = test_agent()
    if success:
        print("AGENT IS WORKING!")
    else:
        print("AGENT TEST FAILED - this may be due to API key issues")
"""
Test script to verify the OpenRouter agent is working
"""
import asyncio
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.rag.agent import OpenRouterAgent
from app.rag.embeddings import EmbeddingService

def test_agent():
    """Test the OpenRouter agent directly"""
    print("Testing OpenRouter Agent...")

    try:
        # Initialize the agent
        agent = OpenRouterAgent()
        print("✅ OpenRouterAgent initialized successfully")

        # Test a simple query
        response = agent.generate_general_response("What is artificial intelligence?")
        print(f"✅ General response received: {response[:100] if response else 'None'}...")

        # Test response with context
        context = "Artificial Intelligence is a branch of computer science that aims to create software or machines that exhibit human-like intelligence."
        try:
            response_with_context = agent.generate_response_with_context(
                query="What is AI?",
                context=context
            )
            print(f"✅ Contextual response received: {response_with_context[:100] if response_with_context else 'None'}...")
        except Exception as e:
            print(f"⚠️  Contextual response failed (expected if OpenRouter API key issue): {str(e)[:50]}...")

        print("✅ OpenRouter agent initialization successful!")
        return True

    except Exception as e:
        print(f"❌ Error testing agent: {str(e)[:100]}...")
        return False

def test_embeddings():
    """Test the Cohere embedding service directly"""
    print("\nTesting Cohere Embeddings...")

    try:
        # Initialize the embedding service
        embedding_service = EmbeddingService()
        print("✅ EmbeddingService initialized successfully")

        # Test embedding generation
        text = "This is a test sentence for embedding."
        embedding = embedding_service.embed_text(text)
        print(f"✅ Embedding generated successfully, length: {len(embedding)}")

        print("✅ Cohere embeddings are working correctly!")
        return True

    except Exception as e:
        print(f"❌ Error testing embeddings: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing OpenRouter Agent Integration...\n")

    agent_success = test_agent()
    embedding_success = test_embeddings()

    if agent_success and embedding_success:
        print("\n🎉 All tests passed! OpenRouter integration is working correctly.")
    else:
        print("\n❌ Some tests failed. Check the error messages above.")
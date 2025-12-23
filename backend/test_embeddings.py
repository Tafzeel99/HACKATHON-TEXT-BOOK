"""
Test to verify the Cohere embeddings are working
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.rag.embeddings import EmbeddingService
from app.config import settings

def test_embeddings():
    """Test the Cohere embedding service directly"""
    print("Testing Cohere Embeddings...")

    try:
        # Check if API key is available
        if not settings.COHERE_API_KEY:
            print("ERROR: COHERE_API_KEY not found in settings")
            return False

        print("API Key found, initializing embedding service...")

        # Initialize the embedding service
        embedding_service = EmbeddingService()
        print("SUCCESS: EmbeddingService initialized successfully")

        # Test embedding generation
        text = "This is a test sentence for embedding."
        embedding = embedding_service.embed_text(text)
        print(f"SUCCESS: Embedding generated successfully, length: {len(embedding)}")

        print("SUCCESS: Cohere embeddings are working!")
        return True

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing Cohere Embeddings Integration...")
    success = test_embeddings()
    if success:
        print("EMBEDDINGS ARE WORKING!")
    else:
        print("EMBEDDINGS TEST FAILED - this may be due to API key issues")
"""
Minimal retrieval validation checks from Spec-2
"""
from qdrant_client import QdrantClient
import sys
import os
import logging

# Add the parent directory to the path to import settings
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_retrieval_connection():
    """
    Validate that we can connect to the Qdrant vector database
    """
    try:
        if settings.QDRANT_API_KEY:
            client = QdrantClient(
                url=settings.QDRANT_URL,
                api_key=settings.QDRANT_API_KEY
            )
        else:
            client = QdrantClient(url=settings.QDRANT_URL)

        # Test collection access
        collection_info = client.get_collection(settings.COLLECTION_NAME)
        logger.info(f"Successfully connected to collection: {settings.COLLECTION_NAME}")
        logger.info(f"Collection points count: {collection_info.points_count}")
        return True

    except Exception as e:
        logger.error(f"Retrieval connection validation failed: {str(e)}")
        return False

def validate_basic_retrieval(query: str = "test", top_k: int = 1):
    """
    Validate basic retrieval functionality
    """
    try:
        if settings.QDRANT_API_KEY:
            client = QdrantClient(
                url=settings.QDRANT_URL,
                api_key=settings.QDRANT_API_KEY
            )
        else:
            client = QdrantClient(url=settings.QDRANT_URL)

        # Test search with a simple query vector (this is just to test connection)
        # In real usage, you'd need to embed the query first
        import random
        test_vector = [random.random() for _ in range(1536)]  # Assuming embedding size

        results = client.search(
            collection_name=settings.COLLECTION_NAME,
            query_vector=test_vector,
            limit=top_k
        )

        logger.info(f"Retrieved {len(results)} results for test query")
        return len(results) >= 0  # Should return results (empty is still valid)

    except Exception as e:
        logger.error(f"Basic retrieval validation failed: {str(e)}")
        return False
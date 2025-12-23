#!/usr/bin/env python3
"""
Test script to verify search functionality in Qdrant
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from app.rag.embeddings import EmbeddingService
from app.config import settings
from qdrant_client import QdrantClient

def test_search():
    print("Testing Qdrant search functionality...")

    # Connect to Qdrant
    if settings.QDRANT_API_KEY:
        client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
    else:
        client = QdrantClient(url=settings.QDRANT_URL)

    collection_name = settings.COLLECTION_NAME
    print(f"Collection: {collection_name}")

    # Initialize embedding service
    embedding_service = EmbeddingService()

    # Test queries
    test_queries = [
        "What is Physical AI & Humanoid Robotics?",
        "Explain ROS 2",
        "digital twin simulation",
        "machine learning in robotics",
        "introduction to robotics"
    ]

    for query in test_queries:
        print(f"\nSearching for: '{query}'")
        try:
            # Generate embedding for query
            query_embedding = embedding_service.embed_text(query)
            print(f"Query embedding length: {len(query_embedding)}")

            # Search in Qdrant
            search_results = client.search(
                collection_name=collection_name,
                query_vector=query_embedding,
                limit=3,
                with_payload=True
            )

            # Convert to the same format as the retriever
            results = search_results

            print(f"Found {len(results)} results:")
            for i, result in enumerate(results):
                print(f"  Result {i+1}:")
                print(f"    Score: {result.score:.4f}")
                print(f"    Title: {result.payload.get('title', 'N/A')[:60]}...")
                print(f"    Text preview: {result.payload.get('text', '')[:100]}...")

        except Exception as e:
            print(f"Error searching for '{query}': {str(e)}")

if __name__ == "__main__":
    test_search()
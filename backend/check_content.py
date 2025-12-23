#!/usr/bin/env python3
"""
Script to verify content in Qdrant
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from app.config import settings
from qdrant_client import QdrantClient

def check_qdrant_content():
    print("Checking Qdrant collection...")

    # Connect to Qdrant
    if settings.QDRANT_API_KEY:
        client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
    else:
        client = QdrantClient(url=settings.QDRANT_URL)

    collection_name = settings.COLLECTION_NAME
    print(f"Collection name: {collection_name}")

    try:
        # Get collection info
        collection_info = client.get_collection(collection_name)
        print(f"Collection exists: {collection_info.config.params.vectors.size} dimensional vectors")
        print(f"Points count: {collection_info.points_count}")

        if collection_info.points_count > 0:
            # Sample some points to see what's in there
            points, next_offset = client.scroll(
                collection_name=collection_name,
                limit=3
            )

            print("\nSample points from collection:")
            for i, point in enumerate(points):
                print(f"\nPoint {i+1}:")
                print(f"  ID: {point.id}")
                print(f"  Payload keys: {list(point.payload.keys()) if point.payload else 'None'}")
                if point.payload:
                    print(f"  Title: {point.payload.get('title', 'N/A')[:50]}...")
                    print(f"  Text preview: {point.payload.get('text', '')[:100]}...")

                if i >= 2:  # Just show first 3 points
                    break
        else:
            print("Collection is empty!")

    except Exception as e:
        print(f"Error accessing Qdrant: {str(e)}")

if __name__ == "__main__":
    check_qdrant_content()
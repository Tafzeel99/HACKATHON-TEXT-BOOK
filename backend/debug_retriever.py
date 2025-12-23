#!/usr/bin/env python3
"""
Debug script to check if the retriever is working properly
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from app.rag.retriever import QdrantRetriever

def debug_retriever():
    print("Debugging QdrantRetriever...")

    try:
        # Initialize the retriever
        retriever = QdrantRetriever()
        print("[SUCCESS] QdrantRetriever initialized successfully")

        # Test search
        query = "What is Physical AI & Humanoid Robotics?"
        print(f"Testing search for: '{query}'")

        sources = retriever.search(query, top_k=3)
        print(f"[SEARCH] Found {len(sources)} sources")

        for i, source in enumerate(sources):
            print(f"  Source {i+1}:")
            print(f"    Title: {source.title}")
            print(f"    Score: {source.score}")
            print(f"    Content preview: {source.content[:100]}...")

        if len(sources) == 0:
            print("[ERROR] No sources found - this explains why context_used is false")

            # Let's try a simple keyword search to see if any content exists
            print("\nTrying broader search for 'robotics'...")
            sources2 = retriever.search("robotics", top_k=3)
            print(f"Found {len(sources2)} sources for 'robotics'")

            for i, source in enumerate(sources2):
                print(f"  Source {i+1}:")
                print(f"    Title: {source.title}")
                print(f"    Score: {source.score}")
                print(f"    Content preview: {source.content[:100]}...")
        else:
            print("[SUCCESS] Sources found - the issue might be elsewhere")

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_retriever()
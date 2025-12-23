"""
Test script to check if the server is responding
"""
import requests
import time

def test_server():
    try:
        print("Testing server connection...")

        # Wait a bit for server to be ready
        time.sleep(2)

        # Test health endpoint
        response = requests.get("http://localhost:8000/health", timeout=10)
        print(f"Health status: {response.status_code}")
        print(f"Health response: {response.json()}")

        # Test query endpoint
        query_data = {
            "query": "hello",
            "include_context": True
        }
        query_response = requests.post(
            "http://localhost:8000/query",
            json=query_data,
            timeout=30
        )
        print(f"Query status: {query_response.status_code}")
        print(f"Query response: {query_response.json()}")

        print("Server is responding correctly!")
        return True

    except requests.exceptions.ConnectionError:
        print("❌ Connection error - server might not be accessible")
        return False
    except requests.exceptions.Timeout:
        print("❌ Timeout - server might be slow to respond")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_server()
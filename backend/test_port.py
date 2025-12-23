"""
Test if port 8000 is accessible
"""
import socket

def test_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('localhost', 8000))
        print("Port 8000 is open and accessible")
        return True
    except socket.error as e:
        print(f"Port 8000 is not accessible: {e}")
        return False
    finally:
        s.close()

if __name__ == "__main__":
    test_port()
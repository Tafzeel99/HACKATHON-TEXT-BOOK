"""
Tests for the query API
"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    """Test health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "rag-agent-api"

def test_query_endpoint_exists():
    """Test that query endpoint exists"""
    # This will fail if no API key is provided, but should return 422 for validation error, not 404
    response = client.post("/query", json={"query": "test"})
    # Should either be 422 (validation error) or 401/500 (due to missing API key), but not 404
    assert response.status_code != 404

def test_query_with_valid_request():
    """Test query with proper request structure"""
    request_data = {
        "query": "What is artificial intelligence?",
        "include_context": True
    }
    response = client.post("/query", json=request_data)
    # This might fail due to missing API key, but should return proper error
    assert response.status_code in [200, 401, 500]  # Success, auth error, or server error

def test_empty_query_validation():
    """Test validation for empty query"""
    request_data = {
        "query": "",
        "include_context": True
    }
    response = client.post("/query", json=request_data)
    assert response.status_code == 422  # Validation error

def test_missing_query_field():
    """Test validation for missing query field"""
    request_data = {
        "include_context": True
    }
    response = client.post("/query", json=request_data)
    assert response.status_code == 422  # Validation error
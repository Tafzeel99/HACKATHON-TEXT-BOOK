# Quickstart: RAG Retrieval Validation

## Overview
This guide explains how to run the RAG retrieval validation system to test the semantic search pipeline for the textbook content.

## Prerequisites
- Python 3.11 or higher
- Access to Cohere API (with valid API key)
- Access to Qdrant vector database (with valid API key and URL)
- The RAG ingestion pipeline must have already run and populated the vector database

## Setup

### 1. Environment Configuration
```bash
# Navigate to the backend directory
cd backend/

# Install required dependencies (if not already installed)
pip install -r requirements.txt
```

### 2. Environment Variables
Create or update your `.env` file in the `backend/` directory:
```env
COHERE_API_KEY="your_cohere_api_key_here"
QDRANT_URL="https://your-qdrant-instance.com:6333"
QDRANT_API_KEY="your_qdrant_api_key_here"
```

### 3. Verify Database Population
Ensure the RAG ingestion pipeline has successfully populated the vector database with textbook content before running validation.

## Running Validation

### Basic Validation
```bash
# Run the complete validation suite
python validate_retrieval.py
```

The validation script will run through all test categories and provide detailed output about the results.

### Validation Components

The validation system tests the following aspects:

1. **Connectivity Validation**
   - Tests connection to the Qdrant vector database
   - Verifies the "rag_embedding" collection exists
   - Ensures basic search functionality works

2. **Semantic Relevance Validation**
   - Tests queries like "ROS 2 architecture patterns" and "digital twin simulation"
   - Verifies that returned passages are semantically related to the query
   - Uses basic heuristics to assess relevance

3. **Result Ranking Validation**
   - Confirms that results are properly ranked by similarity score
   - Verifies scores are in descending order
   - Tests with various query types

4. **Metadata Validation**
   - Ensures all retrieved passages include proper URL, module, and section information
   - Validates metadata completeness and accuracy
   - Checks for proper data formatting

5. **Edge Case Validation**
   - Tests empty queries, malformed input, and unusual search terms
   - Ensures the system handles edge cases gracefully
   - Verifies error handling without crashing

6. **Performance Validation**
   - Measures query response time across multiple requests
   - Validates that 99% of requests complete under 2 seconds
   - Reports average, min, max, and standard deviation of response times

## Expected Output

The validation script will produce output similar to:

```
INFO:__main__:Starting complete RAG retrieval pipeline validation...
INFO:__main__:Validating vector database connectivity...
INFO:__main__:Successfully connected to vector database. Found 1 test results.
...
============================================================
VALIDATION RESULTS SUMMARY
============================================================
Connectivity          : PASS
Semantic Relevance    : PASS
Ranking               : PASS
Metadata              : PASS
Edge Cases            : PASS
Latency               : PASS
------------------------------------------------------------
Overall Status: PASS
============================================================
```

## Troubleshooting

### Common Issues

1. **Connection Errors**
   - Verify your QDRANT_URL, QDRANT_API_KEY, and COHERE_API_KEY are correct
   - Ensure your API keys have not expired
   - Check network connectivity to the services

2. **Empty Results**
   - Verify the RAG ingestion pipeline has completed successfully
   - Confirm the "rag_embedding" collection contains data
   - Check that the vector database is properly populated

3. **Performance Issues**
   - If latency tests fail, check network conditions
   - Verify that the Qdrant instance has sufficient resources
   - Consider that initial queries may be slower due to cold caches

### Validation Failure Response

If validation fails:
1. Check the detailed logs for specific error messages
2. Verify all prerequisites are met
3. Ensure the vector database is properly populated with textbook content
4. Confirm API keys and endpoints are correct and accessible

## Integration with Development Workflow

### Continuous Validation
Run validation as part of your CI/CD pipeline to ensure the RAG retrieval pipeline maintains quality standards.

### Pre-deployment Checks
Execute the full validation suite before deploying changes to production to catch any regressions in retrieval quality.

### Monitoring
Consider running periodic validation checks in production to monitor the ongoing quality of the RAG system.
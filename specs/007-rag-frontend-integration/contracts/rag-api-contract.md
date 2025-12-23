# RAG API Contract

## Query Endpoint

### Request
```
POST /api/query
Content-Type: application/json
```

**Request Body**:
```json
{
  "message": "string, the user's question",
  "sessionId": "string, optional session identifier",
  "context": "string, optional context from selected text"
}
```

**Example Request**:
```json
{
  "message": "What is the main concept of this chapter?",
  "sessionId": "abc123",
  "context": "The main concept of this chapter is artificial intelligence..."
}
```

### Response
**Success Response (200 OK)**:
```json
{
  "answer": "string, the answer to the user's question",
  "sources": [
    {
      "content": "string, the source content",
      "metadata": {
        "page": "number, page number",
        "chapter": "string, chapter identifier",
        "section": "string, section identifier"
      }
    }
  ],
  "session_id": "string, optional session identifier"
}
```

**Example Response**:
```json
{
  "answer": "The main concept of this chapter is reinforcement learning...",
  "sources": [
    {
      "content": "Reinforcement learning is a type of machine learning...",
      "metadata": {
        "page": 45,
        "chapter": "3",
        "section": "3.1"
      }
    }
  ],
  "session_id": "abc123"
}
```

**Error Response (4xx/5xx)**:
```json
{
  "detail": "string, error description"
}
```

## Frontend Service Interface

### sendMessage(message: string, context?: string): Promise<MessageResponse>

**Parameters**:
- `message`: The user's question
- `context`: Optional context from selected text

**Returns**:
```typescript
{
  response: string,      // The answer from the backend
  sources: string[],     // Array of source citations
  sessionId?: string,    // Updated session ID if returned
  error?: string         // Error message if request failed
}
```
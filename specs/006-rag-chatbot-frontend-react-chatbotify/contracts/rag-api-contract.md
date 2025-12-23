# API Contract: RAG Backend Communication

## Overview
This contract defines the interface between the react-chatbotify frontend and the RAG backend API.

## Base URL
`{API_BASE_URL}` - Configurable via environment variable `REACT_APP_RAG_API_URL`

## Endpoints

### POST /api/chat
Send a user message to the RAG backend and receive a response.

**Request**:
```json
{
  "message": "string (the user's message)",
  "sessionId": "string (optional session identifier)"
}
```

**Response (Success)**:
```json
{
  "response": "string (the AI's response)",
  "sources": ["string (references to book content)"],
  "sessionId": "string (session identifier)"
}
```

**Response (Error)**:
```json
{
  "error": "string (error message)",
  "sessionId": "string (session identifier, if available)"
}
```

**Headers**:
- `Content-Type: application/json`
- `Accept: application/json`

**Status Codes**:
- `200`: Success - Response contains the AI's answer
- `400`: Bad Request - Invalid request format
- `500`: Internal Server Error - Backend processing failed

## Message Flow

1. User types message in react-chatbotify input
2. Frontend sends POST request to `/api/chat` with message content
3. Backend processes message using RAG system
4. Backend responds with AI-generated answer and source citations
5. Frontend displays response in chat interface using react-chatbotify

## Error Handling

The frontend should handle these scenarios:
- Network errors: Display appropriate message to user
- Backend errors: Show error in chat interface
- Timeout (>10 seconds): Display timeout message
- Empty responses: Handle gracefully

## Performance Requirements

- API response time: <3 seconds for 95% of requests
- Connection timeout: 10 seconds
- Retry logic: Implement exponential backoff for failed requests
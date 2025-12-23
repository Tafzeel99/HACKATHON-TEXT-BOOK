# Data Model: RAG Backend API Integration

## Entities

### Query
- **Fields**:
  - `message` (string): The user's question text
  - `sessionId` (string, optional): Identifier for maintaining conversation context
  - `context` (string, optional): Selected text or page context passed to the backend
- **Validation**:
  - Message must not be empty
  - SessionId must be a valid string if provided
- **Relationships**: None

### Response
- **Fields**:
  - `response` (string): The answer text from the RAG backend
  - `sources` (string[]): Array of source citations showing where information originated
  - `sessionId` (string, optional): Updated session identifier from backend
  - `error` (string, optional): Error message if the request failed
- **Validation**:
  - Response must be provided when no error occurs
  - Sources array should not exceed 10 items
- **Relationships**: None

### RAGApiResponse (Backend Response Format)
- **Fields**:
  - `answer` (string): The answer text from the backend
  - `sources` (array): Array of source objects containing content and metadata
  - `session_id` (string, optional): Session identifier from the backend
- **Validation**:
  - Answer must be provided when no error occurs
- **Relationships**: None

## State Transitions

### Chat Message State
- `pending` → `loading` (when message is sent to backend)
- `loading` → `received` (when response is received successfully)
- `loading` → `error` (when backend request fails)
- `error` → `pending` (when user retries after error)

### Chat Interface State
- `closed` → `open` (when user clicks chat launcher)
- `open` → `closed` (when user closes chat)
- `open` → `loading` (when processing user request)
- `loading` → `open` (when response is received)
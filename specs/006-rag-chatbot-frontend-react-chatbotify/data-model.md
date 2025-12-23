# Data Model: RAG Chatbot Frontend using react-chatbotify

## Core Entities

### ChatMessage
Represents a single message in the conversation

**Fields**:
- `id`: string - Unique identifier for the message
- `content`: string - The text content of the message
- `sender`: 'user' | 'bot' - Indicates the sender of the message
- `timestamp`: Date - When the message was created/sent
- `status`: 'sent' | 'pending' | 'error' - Status of message delivery (for user messages)

**Validation Rules**:
- `content` must not be empty or exceed 1000 characters
- `sender` must be either 'user' or 'bot'
- `timestamp` must be a valid date

### ChatConfig
Configuration for the chatbot interface

**Fields**:
- `headerTitle`: string - Title displayed in the chat header (default: "AI Book Assistant")
- `botAvatar`: string - URL or path to bot avatar image
- `userAvatar`: string - URL or path to user avatar image
- `primaryColor`: string - Primary theme color (hex format)
- `secondaryColor`: string - Secondary theme color (hex format)
- `backgroundColor`: string - Background theme color (hex format)

**Validation Rules**:
- `headerTitle` must not be empty
- Color fields must be valid hex color codes
- Avatar URLs must be valid image URLs

### ChatSession
Represents a single instance of the chat interface during a user's interaction

**Fields**:
- `sessionId`: string - Unique identifier for the session (not persisted)
- `messages`: ChatMessage[] - Array of messages in the current session
- `isOpen`: boolean - Whether the chat interface is currently open
- `createdAt`: Date - When the session was started

**Validation Rules**:
- `sessionId` must be unique per active session
- `messages` array must not exceed 100 messages in memory
- `isOpen` must be a boolean value

## API Contract Types

### MessageRequest
Type for sending messages to the RAG backend

**Fields**:
- `message`: string - The message content to send to the backend
- `sessionId`: string - Optional session identifier (for backend tracking)

**Validation Rules**:
- `message` must not be empty
- `message` must not exceed 1000 characters

### MessageResponse
Type for receiving responses from the RAG backend

**Fields**:
- `response`: string - The response content from the backend
- `sources`: string[] - Array of source references (for citation)
- `error?: string` - Optional error message if the request failed

**Validation Rules**:
- `response` must not be empty when no error occurred
- `sources` array items must be valid references to book content
// TypeScript interfaces for the RAG Chatbot Frontend

export interface ChatMessage {
  id: string;
  content: string;
  sender: 'user' | 'bot';
  timestamp: Date;
  status?: 'sent' | 'pending' | 'error'; // For user messages only
}

export interface ChatConfig {
  headerTitle: string; // Default: "AI Book Assistant"
  botAvatar: string; // URL or path to bot avatar image
  userAvatar: string; // URL or path to user avatar image
  primaryColor: string; // Primary theme color (hex format)
  secondaryColor: string; // Secondary theme color (hex format)
  backgroundColor: string; // Background theme color (hex format)
}

export interface ChatSession {
  sessionId: string; // Unique identifier for the session (not persisted)
  messages: ChatMessage[]; // Array of messages in the current session
  isOpen: boolean; // Whether the chat interface is currently open
  createdAt: Date; // When the session was started
}

// API Contract Types
export interface MessageRequest {
  message: string; // The message content to send to the backend
  sessionId?: string; // Optional session identifier (for backend tracking)
  context?: string; // Optional context from selected text
}

export interface SourceMetadata {
  content: string; // The source content
  metadata: {
    page?: number; // Page number
    chapter?: string; // Chapter identifier
    section?: string; // Section identifier
    [key: string]: any; // Allow additional metadata properties
  };
}

export interface MessageResponse {
  response: string; // The response content from the backend
  sources: SourceMetadata[]; // Array of source references (for citation)
  error?: string; // Optional error message if the request failed
  sessionId?: string; // Session identifier returned from backend
}
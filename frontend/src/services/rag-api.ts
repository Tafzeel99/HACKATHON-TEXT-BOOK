// services/rag-api.ts - Service for communicating with RAG backend API

import axios from 'axios';

// Define TypeScript interfaces for API requests and responses
interface MessageRequest {
  query: string; // Backend expects 'query' field
  include_context: boolean; // Backend expects 'include_context' field
}

interface MessageResponse {
  response: string;
  sources: Array<{
    content: string;
    metadata: Record<string, any>;
  }>;
  sessionId?: string;
  error?: string;
}

interface RAGApiResponse {
  response: string;
  sources: Array<{
    url: string;
    title: string;
    content: string;
    score: number;
  }>;
  query_type: string;      // "book-related" or "general"
  context_used: boolean;   // Whether context was used
}

class RAGApiService {
  private sessionId: string | null = null;

  constructor() {
    // For Docusaurus, we'll set the base URL dynamically in each request
    // since environment variables are processed at build time
  }

  private getBaseUrl(): string {
    // Try multiple approaches to get the API URL
    if (typeof window !== 'undefined' && (window as any).env?.REACT_APP_RAG_API_URL) {
      // Check for custom window environment
      return (window as any).env.REACT_APP_RAG_API_URL;
    } else if (typeof process !== 'undefined' && process.env?.REACT_APP_RAG_API_URL) {
      // Build-time environment variable
      return process.env.REACT_APP_RAG_API_URL;
    } else {
      // Default fallback
      return 'http://localhost:8000';
    }
  }

  // Method to send a message to the RAG backend
  async sendMessage(message: string): Promise<MessageResponse> {
    try {
      const requestBody: MessageRequest = {
        query: message,  // Backend expects 'query' field
        include_context: true  // Backend expects 'include_context' field
      };

      const response = await axios.post<RAGApiResponse>(`${this.getBaseUrl()}/query`, requestBody, {
        headers: {
          'Content-Type': 'application/json'
        },
      });

      // Transform sources to match expected format
      const transformedSources = response.data.sources.map(source => ({
        content: source.content,
        metadata: {
          page: source.title, // Using title as page
          chapter: source.title, // Using title as chapter
          url: source.url,
          score: source.score
        }
      }));

      return {
        response: response.data.response,
        sources: transformedSources,
      };
    } catch (error: any) {
      console.error('Error communicating with RAG backend:', error);

      return {
        response: '',
        sources: [],
        error: error.response?.data?.detail || error.message || 'Failed to get response from backend',
      };
    }
  }

  // Method to get or set session ID
  getSessionId(): string | null {
    return this.sessionId;
  }

  setSessionId(sessionId: string): void {
    this.sessionId = sessionId;
  }

  // Method to clear session
  clearSession(): void {
    this.sessionId = null;
  }
}

export const ragApiService = new RAGApiService();
export type { MessageRequest, MessageResponse, RAGApiResponse };
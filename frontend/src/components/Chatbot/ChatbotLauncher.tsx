import React, { useState, useRef, useEffect } from 'react';
import './ChatbotLauncher.css';

// Dynamically import ragApiService to handle potential initialization issues
let ragApiService = null;
let ragApiServiceInitialized = false;

// Initialize the service safely
try {
  // We'll initialize the service later in the component to avoid module-level issues
  ragApiServiceInitialized = true;
} catch (error) {
  console.error('Failed to load RAG API service initially:', error);
}

// Define a type for the service to maintain TypeScript compatibility
interface MessageRequest {
  query: string;
  include_context: boolean;
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

interface RAGApiService {
  sendMessage(message: string): Promise<MessageResponse>;
  getSessionId(): string | null;
  setSessionId(sessionId: string): void;
  clearSession(): void;
}

const ChatbotLauncher: React.FC = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);
  // Define the message type with optional sources
  interface ChatMessage {
    id: string;
    text: string;
    sender: 'user' | 'bot';
    sources?: Array<{
      content: string;
      metadata: Record<string, any>;
    }>;
  }

  const [messages, setMessages] = useState<ChatMessage[]>([
    { id: '1', text: "Hello! I'm your AI assistant. How can I help you with the book?", sender: 'bot' }
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const toggleChat = () => {
    setIsChatOpen(!isChatOpen);
  };

  const sendMessage = async () => {
    if (inputRef.current && inputRef.current.value.trim() !== '') {
      const userMessage = {
        id: Date.now().toString(),
        text: inputRef.current.value,
        sender: 'user' as const
      };

      // Add user message
      setMessages(prev => [...prev, userMessage]);

      // Clear input
      inputRef.current.value = '';

      // Show loading state
      setIsLoading(true);
      setError(null);

      try {
        // Dynamically import the RAG API service to avoid initialization issues
        if (!ragApiService) {
          const { ragApiService: importedService } = await import('../../services/rag-api');
          ragApiService = importedService;
        }

        // Call the RAG API service
        const response = await ragApiService.sendMessage(userMessage.text);

        if (response.error) {
          // Handle error response
          setError(response.error);

          // Add error message to chat
          const errorMessage = {
            id: Date.now().toString(),
            text: `Error: ${response.error}`,
            sender: 'bot' as const
          };
          setMessages(prev => [...prev, errorMessage]);
        } else {
          // Apply rendering safety guard
          let botMessageText = response.response;

          // Check if response contains problematic content
          if (
            response.response.includes("Sources:") ||
            response.response.length > 500 ||
            (response.response.match(/\n/g) || []).length > 4 || // More than 4 line breaks
            response.response.toLowerCase().includes("page:") ||
            response.response.toLowerCase().includes("chapter:")
          ) {
            botMessageText = "Additional details are available in sources.";
          }

          const botMessage = {
            id: Date.now().toString(),
            text: botMessageText,
            sender: 'bot' as const,
            sources: response.sources // Store sources separately for display
          };
          setMessages(prev => [...prev, botMessage]);
        }
      } catch (err) {
        console.error('Error sending message:', err);
        setError('Failed to get response from backend');

        // Add error message to chat
        const errorMessage = {
          id: Date.now().toString(),
          text: 'Error: Failed to get response from backend',
          sender: 'bot' as const
        };
        setMessages(prev => [...prev, errorMessage]);
      } finally {
        // Hide loading state
        setIsLoading(false);
      }
    }
  };

  const retrySendMessage = async () => {
    if (inputRef.current && inputRef.current.value.trim() !== '') {
      // Show loading state
      setIsLoading(true);
      setError(null);

      try {
        // Dynamically import the RAG API service to avoid initialization issues
        if (!ragApiService) {
          const { ragApiService: importedService } = await import('../../services/rag-api');
          ragApiService = importedService;
        }

        // Call the RAG API service
        const response = await ragApiService.sendMessage(inputRef.current.value);

        if (response.error) {
          // Handle error response
          setError(response.error);

          // Add error message to chat
          const errorMessage = {
            id: Date.now().toString(),
            text: `Error: ${response.error}`,
            sender: 'bot' as const
          };
          setMessages(prev => [...prev, errorMessage]);
        } else {
          // Apply rendering safety guard
          let botMessageText = response.response;

          // Check if response contains problematic content
          if (
            response.response.includes("Sources:") ||
            response.response.length > 500 ||
            (response.response.match(/\n/g) || []).length > 4 || // More than 4 line breaks
            response.response.toLowerCase().includes("page:") ||
            response.response.toLowerCase().includes("chapter:")
          ) {
            botMessageText = "Additional details are available in sources.";
          }

          const botMessage = {
            id: Date.now().toString(),
            text: botMessageText,
            sender: 'bot' as const,
            sources: response.sources // Store sources separately for display
          };
          setMessages(prev => [...prev, botMessage]);
        }
      } catch (err) {
        console.error('Error sending message:', err);
        setError('Failed to get response from backend');

        // Add error message to chat
        const errorMessage = {
          id: Date.now().toString(),
          text: 'Error: Failed to get response from backend',
          sender: 'bot' as const
        };
        setMessages(prev => [...prev, errorMessage]);
      } finally {
        // Hide loading state
        setIsLoading(false);
      }
    }
  };

  const closeChat = () => {
    setIsChatOpen(false);
  };

  useEffect(() => {
    // Scroll to bottom when messages change
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);


  return (
    <div className="chatbot-launcher-container">
      {/* Floating launcher button positioned at bottom-right */}
      {!isChatOpen && (
        <button
          className="chatbot-launcher-btn"
          onClick={toggleChat}
          aria-label="Open chatbot"
          title="Open AI Book Assistant"
        >
          <img
            src="/img/chatbot-avatar.png"
            alt="Chatbot"
            width="80"
            height="80"
            style={{ width: '80px', height: '80px' }}
          />
        </button>
      )}

      {/* Simple chat interface */}
      {isChatOpen && (
        <div className={`chatbot-interface ${isChatOpen ? 'open' : 'closed'}`}>
          <div style={{
            width: '100%',
            maxWidth: '380px',
            height: '500px',
            maxHeight: '70vh',
            backgroundColor: 'white',
            borderRadius: '12px',
            boxShadow: '0 10px 25px rgba(0, 0, 0, 0.2)',
            display: 'flex',
            flexDirection: 'column',
            zIndex: 10000,
            margin: '0 auto' // Center the chat interface
          }}>
            <div style={{
              backgroundColor: '#301934',
              color: 'white',
              padding: '12px',
              borderTopLeftRadius: '12px',
              borderTopRightRadius: '12px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h3>AI Book Assistant</h3>
                <button
                  onClick={closeChat}
                  style={{
                    background: 'none',
                    border: 'none',
                    color: 'white',
                    fontSize: '18px',
                    cursor: 'pointer'
                  }}
                >
                  ×
                </button>
              </div>
            </div>
            <div style={{
              flex: 1,
              padding: '12px',
              overflowY: 'auto',
              backgroundColor: '#f9fafb',
              minHeight: '0' // Needed for flex child to be scrollable
            }}>
              {messages.map((message) => (
                <div key={message.id}>
                  <div
                    key={message.id}
                    style={{
                      marginBottom: '12px',
                      padding: '8px 12px',
                      backgroundColor: message.sender === 'user' ? '#d1c0c7' : '#d1d5db', // Darker colors for better visibility
                      color: '#333', // Dark text for better readability
                      borderRadius: message.sender === 'user'
                        ? '18px 18px 4px 18px'
                        : '18px 18px 18px 4px',
                      maxWidth: '85%', // Increased for better mobile use
                      marginLeft: message.sender === 'user' ? 'auto' : '0',
                      marginRight: message.sender === 'user' ? '0' : 'auto',
                      wordWrap: 'break-word', // Ensure long words break properly
                      overflowWrap: 'break-word',
                      hyphens: 'auto' // Enable hyphenation for better text wrapping
                    }}
                  >
                    {message.text}
                  </div>
                  {/* Render sources separately if available and not from user */}
                  {message.sender === 'bot' && message.sources && message.sources.length > 0 && (
                    <div
                      style={{
                        marginBottom: '12px',
                        padding: '8px 12px',
                        backgroundColor: '#e5e7eb', // Light gray for sources
                        color: '#4b5563', // Darker text for sources
                        borderRadius: '8px',
                        maxWidth: '85%', // Increased for better mobile use
                        marginLeft: '0',
                        marginRight: 'auto',
                        fontSize: '12px',
                        borderLeft: '3px solid #9ca3af', // Subtle border to distinguish sources
                        wordWrap: 'break-word', // Ensure long words break properly
                        overflowWrap: 'break-word'
                      }}
                    >
                      <details>
                        <summary style={{ cursor: 'pointer', fontWeight: 'bold', marginBottom: '4px' }}>
                          Sources ({message.sources.length})
                        </summary>
                        <div style={{ marginTop: '4px' }}>
                          {message.sources.map((source, index) => (
                            <div key={index} style={{ marginBottom: '8px', paddingLeft: '8px', borderLeft: '2px solid #d1d5db' }}>
                              <div style={{ fontWeight: '500', fontSize: '11px' }}>
                                {source.metadata?.page || source.metadata?.chapter || `Source ${index + 1}`}
                              </div>
                              <div style={{ fontSize: '11px', color: '#6b7280', overflow: 'hidden', textOverflow: 'ellipsis', display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical' }}>
                                {source.content.substring(0, 100)}...
                              </div>
                              {source.metadata?.score && (
                                <div style={{ fontSize: '10px', color: '#9ca3af', marginTop: '2px' }}>
                                  Score: {source.metadata.score.toFixed(3)}
                                </div>
                              )}
                            </div>
                          ))}
                        </div>
                      </details>
                    </div>
                  )}
                </div>
              ))}
              {isLoading && (
                <div
                  style={{
                    marginBottom: '12px',
                    padding: '8px 12px',
                    backgroundColor: '#d1d5db', // Darker color for better visibility
                    color: '#333', // Dark text for better readability
                    borderRadius: '18px 18px 18px 4px',
                    maxWidth: '80%',
                    marginLeft: '0',
                    marginRight: 'auto'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center' }}>
                    <div>Thinking...</div>
                    <div style={{
                      marginLeft: '8px',
                      display: 'flex'
                    }}>
                    </div>
                  </div>
                </div>
              )}
            </div>
            <div ref={messagesEndRef} />
            <div style={{
              padding: '12px',
              borderTop: '1px solid #e5e7eb',
              backgroundColor: 'white',
              display: 'flex',
              gap: '8px',
              flexDirection: 'row' // Ensure proper layout on mobile
            }}>
              <input
                ref={inputRef}
                type="text"
                placeholder="Ask about the book..."
                style={{
                  flex: 1,
                  padding: '10px 12px',
                  border: '1px solid #d1d5db',
                  borderRadius: '24px',
                  fontSize: '14px',
                  minWidth: '0', // Allow flex item to shrink below content size
                  wordWrap: 'break-word'
                }}
                onKeyPress={(e) => {
                  if (e.key === 'Enter') {
                    sendMessage();
                  }
                }}
              />
              <button
                onClick={sendMessage}
                style={{
                  padding: '10px 16px',
                  backgroundColor: '#301934',
                  color: 'white',
                  border: 'none',
                  borderRadius: '24px',
                  cursor: 'pointer',
                  fontSize: '14px',
                  whiteSpace: 'nowrap' // Prevent button text from wrapping
                }}
              >
                Send
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatbotLauncher;
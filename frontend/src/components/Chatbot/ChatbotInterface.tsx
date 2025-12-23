import React from 'react';
import Chatbot, { type ChatbotProps } from 'react-chatbotify';
import { DEFAULT_CHAT_CONFIG } from './config';

interface ChatbotInterfaceProps {
  isOpen: boolean;
  onClose: () => void;
  config?: Partial<ChatbotProps>;
}

const ChatbotInterface: React.FC<ChatbotInterfaceProps> = ({
  isOpen,
  onClose,
  config = {}
}) => {
  // Basic configuration for react-chatbotify
  const chatbotConfig: ChatbotProps = {
    ...config,
    theme: {
      primaryColor: DEFAULT_CHAT_CONFIG.primaryColor,
      secondaryColor: DEFAULT_CHAT_CONFIG.secondaryColor,
      borderRadius: '12px',
      fontFamily: 'system-ui, -apple-system, sans-serif',
    },
    bot: {
      avatarSrc: DEFAULT_CHAT_CONFIG.botAvatar,
      name: DEFAULT_CHAT_CONFIG.headerTitle,
    },
    header: {
      title: DEFAULT_CHAT_CONFIG.headerTitle,
    },
    launcher: {
      onClick: onClose, // When opened, clicking launcher closes it
      className: 'custom-launcher-button',
    },
    placeholder: 'Ask about the book...',
    chatHistory: [],
    onSubmit: (message) => {
      console.log('Message sent:', message);
      // In a real implementation, this would connect to your backend
      // For now, we'll just log the message and in a real scenario you would
      // make an API call to your backend to get a response
    },
  };

  return (
    <div className="chatbot-interface-container">
      <Chatbot
        {...chatbotConfig}
        isOpen={isOpen}
        onClose={onClose}
      />
    </div>
  );
};

export default ChatbotInterface;
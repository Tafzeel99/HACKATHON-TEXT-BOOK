import { ChatConfig } from '../../types/chatbot-types';

// Default configuration for the RAG Chatbot
export const DEFAULT_CHAT_CONFIG: ChatConfig = {
  headerTitle: 'AI Book Assistant',

  // ✅ Bot avatar SVG
  botAvatar: '',

  // Optional: keep default user avatar
  userAvatar: '',

  primaryColor: '#301934', // Dark purple/brown
  secondaryColor: '#4a2a4d',
  backgroundColor: '#ffffff',
};

export const CHATBOT_SETTINGS = {
  launcherPosition: 'bottom-right' as const,
  initialOpenState: false,
  maxMessageLength: 2000,
  animationDuration: 300,
};

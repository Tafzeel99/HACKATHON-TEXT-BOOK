# Quickstart: RAG Chatbot Frontend using react-chatbotify

## Prerequisites

- Node.js 18+ installed
- Docusaurus project already set up
- Access to RAG backend API

## Installation

1. **Install dependencies**:
   ```bash
   cd frontend
   npm install react-chatbotify axios
   ```

2. **Add the chatbot component to your Docusaurus project**:
   - Create the component structure in `src/components/Chatbot/`
   - Update `src/theme/Root.js` to include the global chatbot component

## Configuration

1. **Set up the API service** in `src/services/api/rag-api.ts`:
   ```typescript
   const API_BASE_URL = process.env.REACT_APP_RAG_API_URL || 'http://localhost:8000';
   ```

2. **Configure chatbot settings** in the component:
   - Header title: "AI Book Assistant"
   - Customize colors to match your theme
   - Set up bot and user avatars

## Integration

1. **Update Docusaurus configuration** in `docusaurus.config.js` if needed

2. **Add the component to your Root** in `src/theme/Root.js`:
   ```jsx
   import Chatbot from '@site/src/components/Chatbot';

   export default function Root({ children }) {
     return (
       <>
         {children}
         <Chatbot />
       </>
     );
   }
   ```

## Running the Chatbot

1. **Start your Docusaurus development server**:
   ```bash
   cd frontend
   npm run start
   ```

2. **The chatbot launcher should appear at the bottom-left** of all pages

3. **Click the launcher** to open the chat interface

## API Communication

The chatbot will automatically handle communication with the RAG backend:
- Messages sent by users are forwarded to the backend API
- Typing indicators are shown while waiting for responses
- Responses are displayed in the chat interface with source citations

## Customization

All customization should be done through react-chatbotify's supported props and styling hooks. Do not implement custom UI components outside of the library's supported options.
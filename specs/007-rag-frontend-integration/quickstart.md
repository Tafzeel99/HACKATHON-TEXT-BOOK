# Quickstart: RAG Backend API Integration

## Prerequisites
- Node.js 18+ installed
- Docusaurus project set up
- FastAPI RAG backend running on localhost:8000

## Setup

1. **Start the backend service**
   ```bash
   # In backend directory
   uvicorn main:app --reload
   ```

2. **Start the frontend development server**
   ```bash
   cd frontend
   npm start
   ```

3. **Verify the integration**
   - Open your browser to http://localhost:3000
   - Click the chatbot launcher in the bottom-right corner
   - Ask a question to test the backend integration

## API Configuration

The RAG API service is configured to:
- Connect to backend at `http://localhost:8000` by default
- Use `/api/query` endpoint for sending questions
- Handle session management automatically
- Display source citations with responses

## Troubleshooting

**Issue**: "Failed to connect to backend"
**Solution**: Verify that the FastAPI backend is running on localhost:8000

**Issue**: "CORS error"
**Solution**: Ensure the backend allows requests from localhost:3000

**Issue**: "No response received"
**Solution**: Check browser console for error messages and verify network connectivity
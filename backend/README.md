# Hybrid RAG Chatbot Backend

A clean, minimal backend for a hybrid RAG chatbot that answers both book-related and general questions.

## Features

- ✅ FastAPI web framework
- ✅ OpenAI SDK for intelligent responses
- ✅ Qdrant vector database for book content retrieval
- ✅ Hybrid routing logic (book vs general questions)
- ✅ Source attribution for book answers
- ✅ Selected-text support (optional context)
- ✅ Basic logging and error handling
- ✅ Simple environment-based configuration

## Architecture

```
backend/
├── app/
│   ├── main.py            # FastAPI entry
│   ├── api.py             # /query, /health
│   ├── schemas.py         # Request/response models
│   ├── config.py          # Env config
│   ├── router.py          # Hybrid decision logic
│   └── rag/
│       ├── agent.py       # OpenAI agent logic
│       ├── retriever.py   # Qdrant retrieval
│       └── grounding.py   # Enforce grounded answers
├── validation/            # Retrieval checks
├── tests/                 # API tests
├── requirements.txt
├── Dockerfile
└── README.md
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env`:
```env
OPEN_ROUTER_KEY=your_openrouter_api_key
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your_qdrant_api_key  # if using cloud
COHERE_API_KEY=your_cohere_api_key  # for embeddings
COLLECTION_NAME=book_content
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /query` - Main query endpoint
- `GET /health` - Health check

## Usage

Send a POST request to `/query` with JSON:

```json
{
  "query": "What is ROS 2?",
  "include_context": true
}
```

The system will automatically determine if your query is book-related or general and respond accordingly.

## Validation

Run validation checks:
```bash
python -m validation.retrieval_checks
```

## Testing

Run tests:
```bash
pytest tests/
```
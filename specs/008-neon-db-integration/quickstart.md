# Quickstart: Neon DB Integration Development

## Prerequisites

1. **Python Environment**: Python 3.13+ with virtual environment
2. **Neon Postgres Account**: Free tier account with serverless database
3. **Environment Variables**:
   - `NEON_DB_URL`: Your Neon Postgres connection string
   - `DATABASE_POOL_MIN_SIZE`: Minimum connection pool size (default: 1)
   - `DATABASE_POOL_MAX_SIZE`: Maximum connection pool size (default: 10)

## Setup

### 1. Clone and Navigate
```bash
git clone <repository>
cd <repository>/backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install asyncpg  # For Neon Postgres
```

### 4. Environment Configuration
Create a `.env` file in the backend directory:
```env
NEON_DB_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
DATABASE_POOL_MIN_SIZE=1
DATABASE_POOL_MAX_SIZE=10
```

## Development Workflow

### 1. Database Schema Setup
The Neon database tables will be created automatically by the connection layer. The schema includes:
- `book_modules`: For module/chapter information
- `book_chapters`: For detailed chapter content
- `definitions`: For canonical definitions
- `glossary`: For terminology
- `toc_index`: For table of contents indexing

### 2. Running the Application
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

### 3. Testing the Integration
```bash
# Test basic query
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is module 2?", "include_context": true}'

# Test with debug info
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "define Physical AI", "include_context": true, "debug_context": true}'
```

## Key Files to Modify

### 1. Neon Client
- **File**: `app/db/neon_client.py`
- **Purpose**: Handle all Neon Postgres operations
- **Key Function**: `query_neon_structured_knowledge(query: str) -> Optional[NeonResult]`

### 2. Router Logic
- **File**: `app/router.py`
- **Purpose**: Implement priority-based routing logic
- **Priority Order**: user-selected → neon → qdrant → general

### 3. API Schema
- **File**: `app/schemas.py`
- **Purpose**: Update QueryResponse to include context_source and confidence

## Testing

### Unit Tests
```bash
# Run all tests
pytest tests/

# Run specific test for Neon integration
pytest tests/test_neon_integration.py
```

### Integration Tests
```bash
# Test the full query flow
python -c "
from app.router import HybridRouter
from app.schemas import QueryRequest
import asyncio

async def test_neon_integration():
    router = HybridRouter()
    request = QueryRequest(query='What is module 2?', include_context=True)
    result = await router.route_query(request)
    print(f'Context source: {result.context_source}')
    print(f'Response: {result.response[:100]}...')

asyncio.run(test_neon_integration())
"
```

## Configuration Options

### Confidence Threshold
- **Variable**: `NEON_CONFIDENCE_THRESHOLD`
- **Default**: 0.7
- **Purpose**: Minimum confidence for Neon results to be used exclusively

### Connection Pool Settings
- **Min Pool Size**: `DATABASE_POOL_MIN_SIZE` (default: 1)
- **Max Pool Size**: `DATABASE_POOL_MAX_SIZE` (default: 10)

## Troubleshooting

### Database Connection Issues
1. Verify `NEON_DB_URL` is correct
2. Check that Neon database is active (serverless databases may pause)
3. Ensure firewall rules allow connections

### Query Routing Not Working
1. Check the priority order in the router
2. Verify Neon client is returning results properly
3. Confirm Qdrant integration still works

## Development Tips

1. **Local Development**: Use debug_context=true to see routing traces
2. **Performance**: Monitor query times with and without Neon integration
3. **Testing**: Create test data in Neon DB that matches your book content
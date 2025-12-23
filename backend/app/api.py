"""
API endpoints for the RAG agent
"""
from fastapi import APIRouter, Depends
from .schemas import QueryRequest, QueryResponse
from .router import HybridRouter
from .config import settings
from .db.neon_client import NeonClient
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

# Initialize the hybrid router once
logger.info("Initializing HybridRouter...")
hybrid_router = HybridRouter()
logger.info("HybridRouter initialized successfully")

# Initialize Neon client
logger.info("Initializing NeonClient...")
neon_client = NeonClient()
logger.info("NeonClient initialized successfully")

@router.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest) -> QueryResponse:
    """
    Main query endpoint that handles both book-related and general questions
    """
    logger.info(f"Query endpoint hit: {request.query[:50]}...")
    logger.info(f"Include context: {request.include_context}")
    try:
        result = await hybrid_router.route_query(request)
        logger.info(f"Query processed successfully - Sources: {len(result.sources)}, Context used: {result.context_used}")
        return result
    except Exception as e:
        logger.error(f"Error in query endpoint: {str(e)}")
        import traceback
        traceback.print_exc()

        # Return a fallback response
        from .schemas import QueryResponse
        return QueryResponse(
            response="I'm sorry, I encountered an error processing your request.",
            sources=[],
            query_type="general",
            context_used=False
        )

@router.get("/health/neon")
async def neon_health_check():
    """
    Health check endpoint for Neon DB connection
    """
    try:
        # Test if we can connect to Neon DB
        if neon_client.pool is None:
            # Try to connect
            await neon_client.connect()

        # Perform a simple test query to verify the connection works
        # We'll just test that we can acquire a connection from the pool
        async with neon_client.pool.acquire() as connection:
            result = await connection.fetchval("SELECT 1")
            if result == 1:
                return {
                    "status": "healthy",
                    "service": "neon-db-connection",
                    "version": "1.0.0",
                    "connection": "available"
                }
            else:
                raise Exception("Unexpected test query result")
    except Exception as e:
        logger.error(f"Neon DB health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "service": "neon-db-connection",
            "version": "1.0.0",
            "error": str(e)
        }
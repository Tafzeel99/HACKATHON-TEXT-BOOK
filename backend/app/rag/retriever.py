"""
Qdrant retriever for RAG
"""
from qdrant_client import QdrantClient
from typing import List
from ..config import settings
from ..schemas import Source
from .embeddings import EmbeddingService
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QdrantRetriever:
    def __init__(self):
        import logging
        logger = logging.getLogger(__name__)

        logger.info("Connecting to Qdrant at %s", settings.QDRANT_URL)
        if settings.QDRANT_API_KEY:
            self.client = QdrantClient(
                url=settings.QDRANT_URL,
                api_key=settings.QDRANT_API_KEY
            )
        else:
            self.client = QdrantClient(url=settings.QDRANT_URL)

        logger.info("Qdrant connection established")

        self.collection_name = settings.COLLECTION_NAME
        logger.info("Initializing embedding service...")
        self.embedding_service = EmbeddingService()
        logger.info("QdrantRetriever initialized successfully")

    def search(self, query: str, top_k: int = 5) -> List[Source]:
        """
        Search for relevant passages in Qdrant
        """
        try:
            logger.info(f"Starting search for query: {query[:50]}...")

            # Generate embedding for the query using embedding service
            query_vector = self.embedding_service.embed_text(query)
            logger.info(f"Generated query embedding of length: {len(query_vector)}")

            # Search in Qdrant - using the correct API method for newer Qdrant versions
            query_response = self.client.query_points(
                collection_name=self.collection_name,
                query=query_vector,
                limit=top_k,
                with_payload=True
            )

            logger.info(f"Qdrant returned {len(query_response.points)} results")

            # Convert results to Source objects
            # query_points returns QueryResponse object with points attribute containing ScoredPoint objects
            sources = []
            for i, scored_point in enumerate(query_response.points):  # Access the points attribute
                if scored_point.payload:
                    logger.info(f"Processing result {i+1}: score={scored_point.score}, title='{scored_point.payload.get('title', 'N/A')[:30]}...'")
                    source = Source(
                        url=scored_point.payload.get('url', ''),
                        title=scored_point.payload.get('title', ''),
                        content=scored_point.payload.get('text', ''),
                        score=scored_point.score  # Use the score from the ScoredPoint
                    )
                    sources.append(source)

            logger.info(f"Final: Retrieved {len(sources)} sources for query: {query[:50]}...")
            return sources

        except Exception as e:
            logger.error(f"Error searching in Qdrant: {str(e)}")
            return []

    def verify_connection(self) -> bool:
        """
        Verify connection to Qdrant
        """
        try:
            # Try to get collection info
            collection_info = self.client.get_collection(self.collection_name)
            return True
        except Exception as e:
            logger.error(f"Qdrant connection verification failed: {str(e)}")
            return False
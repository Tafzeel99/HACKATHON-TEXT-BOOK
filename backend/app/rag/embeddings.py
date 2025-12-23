"""
Embedding utilities for the RAG system
"""
import cohere
from ..config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmbeddingService:
    def __init__(self):
        if not settings.COHERE_API_KEY:
            raise ValueError("COHERE_API_KEY environment variable is required")

        self.client = cohere.Client(api_key=settings.COHERE_API_KEY)

    def embed_text(self, text: str) -> list:
        """
        Generate embedding for text using Cohere
        """
        try:
            response = self.client.embed(
                texts=[text],
                model=settings.EMBEDDING_MODEL,  # Cohere embedding model
                input_type="search_query"  # Specify the input type for better embeddings
            )
            return response.embeddings[0]
        except Exception as e:
            logger.error(f"Error generating embedding: {str(e)}")
            raise

    def embed_texts(self, texts: list[str]) -> list:
        """
        Generate embeddings for multiple texts
        """
        try:
            response = self.client.embed(
                texts=texts,
                model=settings.EMBEDDING_MODEL,
                input_type="search_document"  # For documents, use search_document type
            )
            return response.embeddings
        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            raise
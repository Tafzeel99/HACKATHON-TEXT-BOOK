"""
Configuration settings
"""
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # API Settings
    COHERE_API_KEY: str = os.getenv('COHERE_API_KEY', '')
    OPEN_ROUTER_KEY: str = os.getenv('OPEN_ROUTER_KEY', '')
    QDRANT_URL: str = os.getenv('QDRANT_URL', 'http://localhost:6333')
    QDRANT_API_KEY: str = os.getenv('QDRANT_API_KEY', '')

    # Model Settings
    LLM_MODEL: str = os.getenv('LLM_MODEL', 'xiaomi/mimo-v2-flash:free')
    EMBEDDING_MODEL: str = os.getenv('EMBEDDING_MODEL', 'embed-english-v3.0')  # Cohere embedding model
    EMBEDDING_DIMENSION: int = int(os.getenv('EMBEDDING_DIMENSION', '1024'))  # Cohere embedding dimension

    # App Settings
    API_TITLE: str = "Hybrid RAG Chatbot API"
    API_DESCRIPTION: str = "API for book-related and general questions"
    API_VERSION: str = "1.0.0"

    # Qdrant Settings
    COLLECTION_NAME: str = os.getenv('COLLECTION_NAME', 'book_content')

    # Neon DB Settings
    NEON_DB_URL: str = os.getenv('NEON_DB_URL', '')
    DATABASE_POOL_MIN_SIZE: int = int(os.getenv('DATABASE_POOL_MIN_SIZE', '1'))
    DATABASE_POOL_MAX_SIZE: int = int(os.getenv('DATABASE_POOL_MAX_SIZE', '10'))

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore extra fields in .env that aren't defined

settings = Settings()
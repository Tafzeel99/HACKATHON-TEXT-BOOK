"""
Debug version of the main FastAPI application to troubleshoot startup issues
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router
from .config import settings
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("Creating FastAPI app...")
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION
)

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Including router...")
app.include_router(router)

@app.get("/health")
async def health_check():
    logger.info("Health check called")
    return {"status": "healthy", "service": "rag-agent-api"}

logger.info("Main app created successfully")
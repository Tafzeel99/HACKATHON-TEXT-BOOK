"""
Error handling
"""
from fastapi import HTTPException, Request, Response
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

class RAGException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

async def exception_handler(request: Request, exc: RAGException):
    logger.error(f"RAG Exception: {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message}
    )

async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"General Exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )
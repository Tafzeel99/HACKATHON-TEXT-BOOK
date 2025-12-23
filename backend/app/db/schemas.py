"""
Pydantic schemas for database operations
"""
from pydantic import BaseModel
from typing import Optional


class NeonResult(BaseModel):
    """
    Result from Neon DB query
    """
    answer: str
    source: str
    confidence: float
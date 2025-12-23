"""
Pydantic models for request/response
"""
from pydantic import BaseModel, Field
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000, description="User query")
    include_context: bool = Field(default=True, description="Whether to include context in response")
    selected_text: Optional[str] = Field(default=None, description="User-selected text context (highest priority)")
    debug_context: Optional[bool] = Field(default=False, description="Include routing trace for debugging")


class Source(BaseModel):
    url: str
    title: str
    content: str
    score: float


class QueryResponse(BaseModel):
    response: str
    sources: List[Source] = []
    query_type: str  # "book-related" or "general"
    context_used: bool
    context_source: str = "general"  # "user", "neon", "qdrant", "combined", "general"
    confidence: Optional[float] = None  # Confidence level when context used
    debug_info: Optional[dict] = None  # Debug information when debug_context=true
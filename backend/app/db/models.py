"""
Database models for Neon structured knowledge entities
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class BookModule(BaseModel):
    """
    Model for book modules/chapters
    """
    id: UUID
    title: str
    keyword: str
    short_answer: str
    chapter: Optional[str] = None
    page: Optional[int] = None
    confidence_score: float
    created_at: datetime
    updated_at: datetime


class BookChapter(BaseModel):
    """
    Model for book chapters
    """
    id: UUID
    title: str
    keyword: str
    short_answer: str
    chapter_number: str
    page_range: Optional[str] = None
    confidence_score: float
    created_at: datetime
    updated_at: datetime


class Definition(BaseModel):
    """
    Model for canonical definitions
    """
    id: UUID
    term: str
    keyword: Optional[str] = None
    definition: str
    category: Optional[str] = None
    confidence_score: float
    source: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class Glossary(BaseModel):
    """
    Model for glossary entries
    """
    id: UUID
    term: str
    keyword: Optional[str] = None
    explanation: str
    category: Optional[str] = None
    confidence_score: float
    created_at: datetime
    updated_at: datetime


class TocIndex(BaseModel):
    """
    Model for table of contents index
    """
    id: UUID
    title: str
    keyword: str
    summary: str
    chapter: Optional[str] = None
    section: Optional[str] = None
    page: Optional[int] = None
    confidence_score: float
    created_at: datetime
    updated_at: datetime
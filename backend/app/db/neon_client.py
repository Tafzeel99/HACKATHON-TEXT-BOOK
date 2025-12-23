"""
Neon Postgres client for structured knowledge retrieval
"""
import asyncpg
import logging
from typing import Optional, List, Dict, Any
from ..config import settings
from .schemas import NeonResult

logger = logging.getLogger(__name__)


class NeonClient:
    """
    Client for interacting with Neon Postgres database
    """
    def __init__(self):
        self.pool = None
        logger.info("Initializing NeonClient...")

    async def connect(self):
        """
        Establish connection to Neon Postgres
        """
        try:
            self.pool = await asyncpg.create_pool(
                settings.NEON_DB_URL,
                min_size=settings.DATABASE_POOL_MIN_SIZE,
                max_size=settings.DATABASE_POOL_MAX_SIZE,
                command_timeout=30,
                ssl=True
            )
            logger.info("Successfully connected to Neon Postgres")
        except Exception as e:
            logger.error(f"Failed to connect to Neon Postgres: {str(e)}")
            raise

    async def disconnect(self):
        """
        Close connection to Neon Postgres
        """
        if self.pool:
            await self.pool.close()
            logger.info("Disconnected from Neon Postgres")

    async def query_neon_structured_knowledge(self, query: str, confidence_threshold: float = 0.5) -> Optional[NeonResult]:
        """
        Query Neon DB for structured knowledge based on the input query
        """
        if not self.pool:
            logger.warning("Neon DB not connected")
            return None

        try:
            # First, try to match keywords in all structured knowledge tables
            # Search across book_modules, book_chapters, definitions, glossary, toc_index
            async with self.pool.acquire() as connection:
                # Search across all tables in order of priority
                # 1. Check definitions table
                search_query = """
                    SELECT
                        'definition' as source_type,
                        term as title,
                        definition as content,
                        confidence_score
                    FROM definitions
                    WHERE LOWER(term) LIKE LOWER($1) OR LOWER(definition) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 1;
                """

                result = await connection.fetchrow(search_query, f"%{query}%")
                if result and result['confidence_score'] >= confidence_threshold:
                    return NeonResult(
                        answer=result['content'],
                        source=f"{result['source_type']}: {result['title']}",
                        confidence=result['confidence_score']
                    )

                # 2. Check glossary table
                search_query = """
                    SELECT
                        'glossary' as source_type,
                        term as title,
                        explanation as content,
                        confidence_score
                    FROM glossary
                    WHERE LOWER(term) LIKE LOWER($1) OR LOWER(explanation) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 1;
                """

                result = await connection.fetchrow(search_query, f"%{query}%")
                if result and result['confidence_score'] >= confidence_threshold:
                    return NeonResult(
                        answer=result['content'],
                        source=f"{result['source_type']}: {result['title']}",
                        confidence=result['confidence_score']
                    )

                # 3. Check book_modules table
                search_query = """
                    SELECT
                        'module' as source_type,
                        title as title,
                        short_answer as content,
                        confidence_score
                    FROM book_modules
                    WHERE LOWER(title) LIKE LOWER($1) OR LOWER(keyword) LIKE LOWER($1) OR LOWER(short_answer) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 1;
                """

                result = await connection.fetchrow(search_query, f"%{query}%")
                if result and result['confidence_score'] >= confidence_threshold:
                    return NeonResult(
                        answer=result['content'],
                        source=f"{result['source_type']}: {result['title']}",
                        confidence=result['confidence_score']
                    )

                # 4. Check book_chapters table
                search_query = """
                    SELECT
                        'chapter' as source_type,
                        title as title,
                        short_answer as content,
                        confidence_score
                    FROM book_chapters
                    WHERE LOWER(title) LIKE LOWER($1) OR LOWER(keyword) LIKE LOWER($1) OR LOWER(short_answer) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 1;
                """

                result = await connection.fetchrow(search_query, f"%{query}%")
                if result and result['confidence_score'] >= confidence_threshold:
                    return NeonResult(
                        answer=result['content'],
                        source=f"{result['source_type']}: {result['title']}",
                        confidence=result['confidence_score']
                    )

                # 5. Check toc_index table
                search_query = """
                    SELECT
                        'toc' as source_type,
                        title as title,
                        summary as content,
                        confidence_score
                    FROM toc_index
                    WHERE LOWER(title) LIKE LOWER($1) OR LOWER(keyword) LIKE LOWER($1) OR LOWER(summary) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 1;
                """

                result = await connection.fetchrow(search_query, f"%{query}%")
                if result and result['confidence_score'] >= confidence_threshold:
                    return NeonResult(
                        answer=result['content'],
                        source=f"{result['source_type']}: {result['title']}",
                        confidence=result['confidence_score']
                    )

                # If no results found with sufficient confidence in any table
                return None

        except Exception as e:
            logger.error(f"Error querying Neon DB: {str(e)}")
            return None

    async def search_book_modules(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for book modules by keyword
        """
        if not self.pool:
            logger.warning("Neon DB not connected")
            return []

        try:
            async with self.pool.acquire() as connection:
                search_query = """
                    SELECT
                        id,
                        title,
                        keyword,
                        short_answer,
                        chapter,
                        page,
                        confidence_score,
                        created_at,
                        updated_at
                    FROM book_modules
                    WHERE LOWER(title) LIKE LOWER($1) OR LOWER(keyword) LIKE LOWER($1) OR LOWER(short_answer) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 5;
                """

                rows = await connection.fetch(search_query, f"%{query}%")
                return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Error searching book modules: {str(e)}")
            return []

    async def search_book_chapters(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for book chapters by keyword
        """
        if not self.pool:
            logger.warning("Neon DB not connected")
            return []

        try:
            async with self.pool.acquire() as connection:
                search_query = """
                    SELECT
                        id,
                        title,
                        keyword,
                        short_answer,
                        chapter_number,
                        page_range,
                        confidence_score,
                        created_at,
                        updated_at
                    FROM book_chapters
                    WHERE LOWER(title) LIKE LOWER($1) OR LOWER(keyword) LIKE LOWER($1) OR LOWER(short_answer) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 5;
                """

                rows = await connection.fetch(search_query, f"%{query}%")
                return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Error searching book chapters: {str(e)}")
            return []

    async def search_definitions(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for definitions by keyword
        """
        if not self.pool:
            logger.warning("Neon DB not connected")
            return []

        try:
            async with self.pool.acquire() as connection:
                search_query = """
                    SELECT
                        id,
                        term,
                        keyword,
                        definition,
                        category,
                        confidence_score,
                        source,
                        created_at,
                        updated_at
                    FROM definitions
                    WHERE LOWER(term) LIKE LOWER($1) OR LOWER(definition) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 5;
                """

                rows = await connection.fetch(search_query, f"%{query}%")
                return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Error searching definitions: {str(e)}")
            return []

    async def search_glossary(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for glossary entries by keyword
        """
        if not self.pool:
            logger.warning("Neon DB not connected")
            return []

        try:
            async with self.pool.acquire() as connection:
                search_query = """
                    SELECT
                        id,
                        term,
                        keyword,
                        explanation,
                        category,
                        confidence_score,
                        created_at,
                        updated_at
                    FROM glossary
                    WHERE LOWER(term) LIKE LOWER($1) OR LOWER(explanation) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 5;
                """

                rows = await connection.fetch(search_query, f"%{query}%")
                return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Error searching glossary: {str(e)}")
            return []

    async def search_toc_index(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for table of contents entries by keyword
        """
        if not self.pool:
            logger.warning("Neon DB not connected")
            return []

        try:
            async with self.pool.acquire() as connection:
                search_query = """
                    SELECT
                        id,
                        title,
                        keyword,
                        summary,
                        chapter,
                        section,
                        page,
                        confidence_score,
                        created_at,
                        updated_at
                    FROM toc_index
                    WHERE LOWER(title) LIKE LOWER($1) OR LOWER(keyword) LIKE LOWER($1) OR LOWER(summary) LIKE LOWER($1)
                    ORDER BY confidence_score DESC
                    LIMIT 5;
                """

                rows = await connection.fetch(search_query, f"%{query}%")
                return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Error searching TOC index: {str(e)}")
            return []
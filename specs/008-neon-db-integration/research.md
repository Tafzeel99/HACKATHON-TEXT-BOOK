# Research: Neon DB Integration

## Overview
This research document captures the findings and decisions for integrating Neon Serverless Postgres as a structured knowledge layer in the RAG chatbot system.

## Decision: Neon Postgres Connection Approach
**Rationale**: Neon Serverless Postgres will be integrated using the official `asyncpg` library for asynchronous operations to maintain compatibility with the existing FastAPI async framework. This provides efficient connection pooling and handles the serverless nature of Neon with automatic scaling.

**Alternatives considered**:
1. `psycopg3` - Modern but has more complex async support
2. `SQLAlchemy` - More complex ORM than needed for this use case
3. `asyncpg` (selected) - Lightweight, fast, and well-suited for async operations

## Decision: Database Schema Design
**Rationale**: The schema will follow a read-optimized approach with dedicated tables for different types of structured knowledge (book_modules, book_chapters, definitions, glossary, toc_index). Each table includes id, title/keyword, short_answer (max 3 sentences), chapter, page, and confidence_score fields as specified.

**Alternatives considered**:
1. Single unified table - Less efficient for targeted queries
2. JSONB fields for flexibility - Would sacrifice query performance
3. Separate tables per knowledge type (selected) - Optimal for targeted queries

## Decision: Query Routing Logic
**Rationale**: The routing logic will be implemented in the backend router layer with a strict priority order: user-selected text → Neon structured answer → Qdrant context → general LLM fallback. This ensures the system respects the priority requirements while maintaining existing functionality.

**Alternatives considered**:
1. Agent-based routing - Would complicate the agent's role and violate the non-goal of letting agent decide retrieval logic
2. Backend routing (selected) - Clean separation of concerns, easier to maintain

## Decision: Confidence Threshold Implementation
**Rationale**: A configurable confidence threshold will be implemented to determine when to use Neon results alone vs. falling back to Qdrant. The threshold will be set to 0.7 initially but configurable via settings.

**Alternatives considered**:
1. Fixed threshold - Less flexible for different content types
2. Configurable threshold (selected) - Allows tuning based on performance

## Decision: Error Handling Strategy
**Rationale**: The system will gracefully degrade when Neon DB is unavailable, falling back to existing Qdrant-only behavior to ensure no regression when Neon is disabled or unavailable.

**Alternatives considered**:
1. Fail fast - Would break functionality when Neon is down
2. Graceful degradation (selected) - Maintains system availability

## Technology Stack Integration
- **Neon Postgres**: Serverless Postgres for structured knowledge storage
- **asyncpg**: Async PostgreSQL adapter for Python
- **FastAPI**: Existing framework with async support
- **Pydantic**: For data validation and serialization
- **Environment variables**: For connection string management
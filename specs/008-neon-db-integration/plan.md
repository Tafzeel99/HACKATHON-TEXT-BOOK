# Implementation Plan: Neon DB Integration

**Branch**: `008-neon-db-integration` | **Date**: 2025-12-23 | **Spec**: [link](spec.md)
**Input**: Feature specification from `/specs/008-neon-db-integration/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan implements the Neon Serverless Postgres integration as a structured knowledge layer for the existing RAG chatbot. The implementation will add a new database layer to complement the existing Qdrant vector search, allowing the system to answer short, exact queries precisely (e.g. "module 2") while preserving existing Qdrant functionality. The system will follow a strict priority order: user-selected text → Neon structured answers → Qdrant context → general LLM fallback, ensuring enhanced answer precision and reduced hallucinations while maintaining the existing working RAG flow.

## Technical Context

**Language/Version**: Python 3.13.1
**Primary Dependencies**: FastAPI, OpenAI SDK, Qdrant client, Cohere, Neon Postgres connector
**Storage**: Qdrant Cloud (vector storage), Neon Serverless Postgres (structured knowledge), local JSON files (configuration)
**Testing**: pytest for backend testing
**Target Platform**: Linux server (backend API)
**Project Type**: Web application (backend API with FastAPI)
**Performance Goals**: Sub-3 second response time even when querying both knowledge sources, 95% of definition queries return within 2 seconds
**Constraints**: Must respect user-selected text boundaries, no hallucinations, cite chapter/section in responses, preserve existing Qdrant-only behavior when Neon is disabled
**Scale/Scope**: Single backend API serving RAG chatbot queries with multiple knowledge sources

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

1. **Technical Accuracy**: Integration with Neon Postgres must follow official documentation and best practices for database connections
2. **Clarity and Accessibility**: Implementation must be understandable for advanced undergraduate to graduate level students
3. **Reproducibility**: All database schemas and API contracts must be clearly documented and reproducible
4. **AI-Native, Spec-Driven Development**: Implementation must follow the spec-driven approach with proper documentation
5. **RAG Chatbot Constraints**:
   - Must respect user-selected text boundaries (FR-002)
   - No hallucinations (FR-009)
   - Cite chapter/section in responses (FR-008)
   - Stack includes Neon Postgres as specified
6. **No breaking changes**: Existing Qdrant functionality must remain intact (Non-goal: Do NOT replace Qdrant)

## Project Structure

### Documentation (this feature)

```text
specs/008-neon-db-integration/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── checklists/          # Quality checklist
    └── requirements.md
```

### Source Code (repository root)

```text
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api.py
│   ├── router.py
│   ├── config.py
│   ├── schemas.py
│   ├── db/              # New directory for database operations
│   │   ├── __init__.py
│   │   └── neon_client.py
│   └── rag/
│       ├── __init__.py
│       ├── agent.py
│       ├── embeddings.py
│       ├── grounding.py
│       └── retriever.py
├── tests/
│   ├── __init__.py
│   └── test_query_api.py
├── requirements.txt
├── .env
└── README.md
```

**Structure Decision**: Web application with backend API (FastAPI) structure. The Neon DB integration will be added to the existing backend structure in a new `app/db/` directory. This maintains the existing architecture while adding the new structured knowledge layer capability.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [None] | [No violations identified] | [All constitution requirements met] |

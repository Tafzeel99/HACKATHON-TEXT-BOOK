# Tasks: Neon DB Integration

**Feature**: Neon DB Integration for RAG Chatbot
**Branch**: 008-neon-db-integration
**Generated**: 2025-12-23
**Based on**: spec.md, plan.md, data-model.md, contracts/query-api-v1.yaml

## Dependencies

User Story 1 (P1) → User Story 2 (P1) → User Story 3 (P2)

## Parallel Execution Examples

- **User Story 1**: T010-T020 can run in parallel with T025-T030
- **User Story 2**: T035-T040 can run in parallel with T045-T050
- **User Story 3**: T055 can run in parallel with T060-T065

## Implementation Strategy

MVP: Complete User Story 1 (Query Neon DB for Structured Knowledge) to provide basic functionality. Then incrementally add User Stories 2 and 3 for enhanced functionality.

---

## Phase 1: Setup

**Goal**: Initialize project structure and dependencies for Neon DB integration

- [X] T001 Create app/db directory structure in backend/app/db/
- [X] T002 Install asyncpg dependency for Neon Postgres connection
- [X] T003 Update requirements.txt with asyncpg and neon dependencies
- [X] T004 Create initial neon_client.py file in backend/app/db/
- [X] T005 Add Neon DB configuration to backend/app/config.py
- [X] T006 Update .env.example with NEON_DB_URL variable

## Phase 2: Foundational Components

**Goal**: Implement core Neon DB infrastructure components

- [X] T010 Create NeonResult Pydantic model in backend/app/db/schemas.py
- [X] T015 Implement NeonClient class with connection pooling in backend/app/db/neon_client.py
- [X] T020 Create Neon database schema migration files
- [X] T025 Implement query_neon_structured_knowledge function in backend/app/db/neon_client.py
- [X] T030 Add connection health check endpoint to backend/app/api.py

## Phase 3: User Story 1 - Query Neon DB for Structured Knowledge (Priority: P1)

**Goal**: As a user of the RAG chatbot, when I ask questions about book metadata, chapter summaries, definitions, or FAQs, the system should retrieve authoritative information from the Neon Postgres database to provide accurate, verified answers.

**Independent Test**: Can be fully tested by querying the system with specific metadata questions (e.g., "What is the definition of Physical AI?") and verifying the response comes from Neon DB with proper citations.

- [X] T035 [P] [US1] Create BookModules table model in backend/app/db/models.py
- [X] T040 [P] [US1] Create BookChapters table model in backend/app/db/models.py
- [X] T045 [P] [US1] Create Definitions table model in backend/app/db/models.py
- [X] T050 [P] [US1] Create Glossary table model in backend/app/db/models.py
- [X] T055 [US1] Create TocIndex table model in backend/app/db/models.py
- [X] T060 [US1] Implement keyword search function for all Neon entities
- [X] T065 [US1] Update HybridRouter to call Neon when appropriate
- [ ] T070 [US1] Test: Verify "What is the definition of Physical AI?" returns Neon DB result

## Phase 4: User Story 2 - Intelligent Context Selection Between Qdrant and Neon (Priority: P1)

**Goal**: As a user of the RAG chatbot, when I ask complex questions, the system should intelligently decide whether to use Qdrant vector search, Neon Postgres structured knowledge, or combine both to provide the best answer.

**Independent Test**: Can be tested by asking questions that require both vector-based context and structured knowledge, verifying the system appropriately combines information from both sources.

- [X] T075 [P] [US2] Update QueryResponse schema to include context_source field in backend/app/schemas.py
- [X] T080 [P] [US2] Update QueryResponse schema to include confidence field in backend/app/schemas.py
- [X] T085 [US2] Implement priority routing logic in backend/app/router.py (user → neon → qdrant → general)
- [X] T090 [US2] Implement confidence threshold logic for Neon results
- [X] T095 [US2] Implement combined context handling in agent response generation
- [X] T100 [US2] Add debug context information when debug_context=true
- [ ] T105 [US2] Test: Verify query with weak Qdrant results falls back to Neon DB

## Phase 5: User Story 3 - Preserve User-Selected Context Priority (Priority: P2)

**Goal**: As a user who selects specific text in the chatbot interface, when I ask questions about that text, the system should prioritize answering only from my selected context rather than using general knowledge sources.

**Independent Test**: Can be tested by selecting text in the interface and asking follow-up questions, verifying the system only responds based on the selected text.

- [X] T110 [US3] Update QueryRequest schema to properly handle selected_text in backend/app/schemas.py
- [X] T115 [US3] Implement user-selected text priority in backend/app/router.py
- [ ] T120 [US3] Update agent to respect user-selected text context
- [ ] T125 [US3] Test: Verify selected text context is prioritized over other sources

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Complete integration and ensure all components work together

- [X] T130 Add comprehensive error handling for Neon DB connection failures
- [X] T135 Update OpenAPI documentation with new response fields
- [ ] T140 Add performance monitoring for Neon DB queries
- [ ] T145 Create integration tests for all user stories
- [ ] T150 Update README with Neon DB integration instructions
- [X] T155 Document environment variables for Neon DB configuration (done in .env.example)
- [ ] T160 Final end-to-end testing of all user stories
- [ ] T165 Performance testing to ensure sub-3-second response times
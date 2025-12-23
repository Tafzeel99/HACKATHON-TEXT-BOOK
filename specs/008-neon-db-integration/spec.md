# Feature Specification: Neon DB Integration

**Feature Branch**: `008-neon-db-integration`
**Created**: 2025-12-23
**Status**: Draft
**Input**: User description: "Integration of Neon Serverless Postgres as structured knowledge layer for RAG chatbot to provide vector-based retrieval (Qdrant), persistent structured knowledge (Neon DB), optional user-selected text context, and general reasoning capability"

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.

  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Query Neon DB for Structured Knowledge (Priority: P1)

As a user of the RAG chatbot, when I ask questions about book metadata, chapter summaries, definitions, or FAQs, the system should retrieve authoritative information from the Neon Postgres database to provide accurate, verified answers.

**Why this priority**: This provides the foundational structured knowledge layer that complements the vector search, ensuring users get canonical answers for well-defined topics.

**Independent Test**: Can be fully tested by querying the system with specific metadata questions (e.g., "What is the definition of Physical AI?") and verifying the response comes from Neon DB with proper citations.

**Acceptance Scenarios**:

1. **Given** a user asks for a definition that exists in Neon DB, **When** the query is processed, **Then** the system returns the canonical definition from the database with proper attribution
2. **Given** a user asks for chapter summaries, **When** the query is processed, **Then** the system retrieves and presents the structured summary from Neon DB

---

### User Story 2 - Intelligent Context Selection Between Qdrant and Neon (Priority: P1)

As a user of the RAG chatbot, when I ask complex questions, the system should intelligently decide whether to use Qdrant vector search, Neon Postgres structured knowledge, or combine both to provide the best answer.

**Why this priority**: This ensures the system maximizes the value of both knowledge sources, providing more comprehensive and accurate responses than either source alone.

**Independent Test**: Can be tested by asking questions that require both vector-based context and structured knowledge, verifying the system appropriately combines information from both sources.

**Acceptance Scenarios**:

1. **Given** a query with weak Qdrant results, **When** the system processes the request, **Then** it queries Neon DB for structured knowledge as a fallback
2. **Given** a query that benefits from both sources, **When** the system processes the request, **Then** it combines information from both Qdrant and Neon DB appropriately

---

### User Story 3 - Preserve User-Selected Context Priority (Priority: P2)

As a user who selects specific text in the chatbot interface, when I ask questions about that text, the system should prioritize answering only from my selected context rather than using general knowledge sources.

**Why this priority**: This ensures the system respects user intent when they specifically select text, preventing hallucinations and maintaining accuracy.

**Independent Test**: Can be tested by selecting text in the interface and asking follow-up questions, verifying the system only responds based on the selected text.

**Acceptance Scenarios**:

1. **Given** a user selects specific text and asks a question about it, **When** the query is processed, **Then** the system responds only using the selected text without adding external knowledge

---

### Edge Cases

- What happens when Neon DB is temporarily unavailable but Qdrant is accessible?
- How does the system handle queries when both Qdrant and Neon return no relevant results?
- What if the user provides selected text but also enables broader context inclusion?
- How does the system handle conflicting information between Qdrant results and Neon DB?
- What happens when Neon DB returns multiple matching records for a query?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST query Neon Postgres database for structured knowledge when Qdrant vector search returns weak or no results
- **FR-002**: System MUST prioritize user-selected text context over both Qdrant and Neon DB results when provided
- **FR-003**: System MUST use Qdrant context as primary source when include_context = true and sources are available
- **FR-004**: System MUST query Neon DB for canonical information (definitions, summaries, FAQs, book metadata)
- **FR-005**: System MUST combine information from both Qdrant and Neon DB when beneficial for comprehensive answers
- **FR-006**: System MUST preserve all retrieved sources in the final response and never silently drop them
- **FR-007**: System MUST clearly indicate when responses are based on general LLM knowledge (when both Qdrant and Neon fail)
- **FR-008**: System MUST treat Neon DB content as verified internal knowledge and cite it appropriately
- **FR-009**: System MUST not hallucinate information when responding from user-selected text context
- **FR-010**: System MUST maintain context_used = true when either Qdrant or Neon DB sources are utilized

### Key Entities

- **Neon DB Records**: Structured knowledge entries containing book metadata, chapter summaries, canonical explanations, definitions, FAQs, and verified explanations
- **Qdrant Sources**: Vector-searched document chunks with relevance scores and metadata
- **User Context**: Selected text provided by user that takes priority over other knowledge sources

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of definition and metadata queries return accurate answers from Neon DB within 2 seconds
- **SC-002**: System successfully combines Qdrant and Neon DB sources in 90% of complex queries that benefit from both sources
- **SC-003**: User-selected text context is prioritized correctly in 100% of cases where such context is provided
- **SC-004**: System properly indicates "based on general knowledge" when both Qdrant and Neon DB return no results, in 100% of such cases
- **SC-005**: No sources are silently dropped - all retrieved sources appear in final responses when available
- **SC-006**: Response accuracy for canonical information (definitions, summaries) improves by 40% compared to Qdrant-only approach
- **SC-007**: System maintains sub-3-second response time even when querying both knowledge sources

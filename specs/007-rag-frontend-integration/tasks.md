# Tasks: RAG Backend API Integration

**Feature**: RAG Backend API Integration
**Branch**: `007-rag-frontend-integration`
**Spec**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md)
**Created**: 2025-12-19

## Implementation Strategy

MVP approach: Implement User Story 1 (P1) first to deliver core value of asking questions with source citations. Subsequent stories add enhanced functionality. Each user story is independently testable.

## Dependencies

User stories are designed to be independent, but share foundational components:
- US1, US2, US3, US4 all depend on: rag-api.ts service implementation
- US1, US2, US3, US4 all depend on: chatbot UI state management

User Story Completion Order: Foundational → US1 → US2 → US3 → US4

## Parallel Execution Examples

Per User Story:
- **US1**: T015 [P] [US1] Update ChatbotLauncher state management, T016 [P] [US1] Modify sendMessage to use rag-api service
- **US2**: T020 [P] [US2] Implement loading state display, T021 [P] [US2] Update message rendering with sources
- **US3**: T025 [P] [US3] Add source citation display, T026 [P] [US3] Format source metadata for UI

## Phase 1: Setup

**Goal**: Initialize project structure and dependencies for RAG integration

- [X] T001 Create frontend/src/services directory if not exists
- [X] T002 Verify axios dependency is available in package.json
- [X] T003 Verify TypeScript configuration supports service imports
- [X] T004 Verify existing chatbot components are accessible

## Phase 2: Foundational

**Goal**: Prepare existing service layer and data structures needed by all user stories

- [X] T005 Verify frontend/src/services/rag-api.ts exists and has proper axios import
- [X] T006 Verify TypeScript interfaces for Query, Response, and RAGApiResponse exist per data-model.md
- [X] T007 Verify ragApiService class has proper baseUrl configuration
- [X] T008 Verify sendMessage method implements POST to /api/query endpoint
- [X] T009 Verify error handling exists for backend communication failures
- [X] T010 Verify session management functionality exists (get/set/clear session)
- [X] T011 Test basic API service connectivity with backend
- [X] T012 Update frontend/src/types/chatbot-types.ts with new interfaces if needed
- [X] T013 Add loading and error state management to ChatbotLauncher component
- [X] T014 Update chat message state transitions per data-model.md

## Phase 3: User Story 1 - Ask Questions from Book Content (Priority: P1)

**Goal**: Enable users to ask questions with selected text context and receive answers with source citations

**Independent Test**: Can be fully tested by selecting text, asking a question, and verifying the response comes with source metadata. Delivers immediate value by allowing users to clarify textbook concepts in real-time.

- [X] T015 [P] [US1] Update ChatbotLauncher state to capture selected text context
- [X] T016 [P] [US1] Modify sendMessage function to use ragApiService.sendMessage
- [X] T017 [US1] Add selected text capture functionality to work with book content
- [X] T018 [US1] Pass context parameter to backend API call when available
- [X] T019 [US1] Process backend response with sources array and display in chat
- [X] T020 [US1] Verify acceptance scenario 1: selected text + related question → contextual answer with citations
- [X] T021 [US1] Verify acceptance scenario 2: question without selected text → answer based on page content

## Phase 4: User Story 2 - Natural Language Query Submission (Priority: P1)

**Goal**: Enable users to submit natural language questions without necessarily selecting specific text

**Independent Test**: Can be fully tested by typing a question and receiving a response. Delivers core Q&A functionality.

- [X] T022 [P] [US2] Verify basic question submission without context works
- [X] T023 [P] [US2] Ensure default context is provided when no text is selected
- [X] T024 [US2] Update chat UI to handle responses without selected text context
- [X] T025 [US2] Verify acceptance scenario: opened Q&A interface + typed question → answer with source metadata

## Phase 5: User Story 3 - View Responses with Source Metadata (Priority: P2)

**Goal**: Display source citations showing where information originated in the book

**Independent Test**: Can be tested by asking a question and verifying that the response includes source citations. Enhances the educational value of the feature.

- [X] T026 [P] [US3] Format source metadata for display per contract specification
- [X] T027 [P] [US3] Add source citation display component to chat messages
- [X] T028 [US3] Show page/chapter/section references from metadata in citations
- [X] T029 [US3] Verify acceptance scenario 1: submitted question → response with source citations
- [X] T030 [US3] Verify acceptance scenario 2: response with multiple sources → all citations clearly displayed

## Phase 6: User Story 4 - Handle Loading and Error States (Priority: P2)

**Goal**: Show appropriate loading indicators and error messages during API communication

**Independent Test**: Can be tested by submitting questions and verifying loading states are shown. Can be tested by simulating errors and verifying appropriate error messages are displayed.

- [X] T031 [P] [US4] Add loading state display during backend request processing
- [X] T032 [P] [US4] Update UI to show visual feedback during API calls
- [X] T033 [US4] Implement error message display for backend failures
- [X] T034 [US4] Add retry functionality for failed requests
- [X] T035 [US4] Verify acceptance scenario 1: submitted question → loading indicator displayed
- [X] T036 [US4] Verify acceptance scenario 2: unavailable backend → appropriate error message

## Phase 7: Polish & Cross-Cutting Concerns

**Goal**: Final integration, testing, and optimization

- [X] T037 Add proper typing for all new functionality
- [X] T038 Update README or documentation with integration details
- [X] T039 Test end-to-end flow across all user stories
- [X] T040 Optimize API request performance and error handling
- [X] T041 Verify all success criteria from spec are met
- [X] T042 Clean up any temporary/development code
- [X] T043 Run full application to verify integration works in context
<!--
Sync Impact Report
Version change:  -> 0.1.0
List of modified principles:
  - PROJECT_NAME: AI-Native Physical Intelligence Book with Embedded RAG Chatbot
  - PRINCIPLE_1_NAME: Technical Accuracy
  - PRINCIPLE_1_DESCRIPTION: All factual and technical claims must be traceable to primary and official sources. Prefer official documentation, recognized standards, and peer-reviewed research.
  - PRINCIPLE_2_NAME: Clarity and Accessibility
  - PRINCIPLE_2_DESCRIPTION: All content must be accessible and understandable for advanced undergraduate to graduate level students in AI, Robotics, and Computer Science, prioritizing clarity and didactic value.
  - PRINCIPLE_3_NAME: Reproducibility
  - PRINCIPLE_3_DESCRIPTION: All code, architectural designs, and experimental results must be reproducible. Code must be executable or clearly labeled as pseudocode, and environments should be well-documented.
  - PRINCIPLE_4_NAME: AI-Native, Spec-Driven Development
  - PRINCIPLE_4_DESCRIPTION: The development process follows an AI-native, spec-driven approach where architectural decisions are explicitly justified and documented, guiding implementation.
  - SECTION_2_NAME: Content & Writing Guidelines
  - SECTION_2_CONTENT:
      - Format: Docusaurus book deployed to GitHub Pages
      - Tone: Precise, instructional, system-oriented
      - Audience: Advanced undergraduate to graduate level
      - Each module includes concepts, architecture, implementation, and constraints
  - SECTION_3_NAME: RAG Chatbot Constraints
  - SECTION_3_CONTENT:
      - Stack: OpenAI Agents/ChatKit, FastAPI, Neon Postgres, Qdrant Cloud
      - Answers only from indexed book content
      - Must respect user-selected text boundaries
      - No hallucinations; cite chapter/section in responses
  - GOVERNANCE_RULES: This constitution is the supreme governing document for the project. All amendments must be formally documented, approved by project leadership, and include a migration plan if applicable. Compliance with this constitution will be verified through code reviews and regular audits. Adherence to these principles is mandatory for all contributors.
Added sections:
  - Content & Writing Guidelines
  - RAG Chatbot Constraints
Removed sections:
  - None
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .specify/templates/commands/*.md: ⚠ pending (no files found in glob, but still need to check if any get created later)
Follow-up TODOs:
  - TODO(RATIFICATION_DATE): Original adoption date is unknown, please provide.
-->
# AI-Native Physical Intelligence Book with Embedded RAG Chatbot Constitution

## Core Principles

### Technical Accuracy
All factual and technical claims must be traceable to primary and official sources. Prefer official documentation, recognized standards, and peer-reviewed research.

### Clarity and Accessibility
All content must be accessible and understandable for advanced undergraduate to graduate level students in AI, Robotics, and Computer Science, prioritizing clarity and didactic value.

### Reproducibility
All code, architectural designs, and experimental results must be reproducible. Code must be executable or clearly labeled as pseudocode, and environments should be well-documented.

### AI-Native, Spec-Driven Development
The development process follows an AI-native, spec-driven approach where architectural decisions are explicitly justified and documented, guiding implementation.

## Content & Writing Guidelines

Format: Docusaurus book deployed to GitHub Pages
Tone: Precise, instructional, system-oriented
Audience: Advanced undergraduate to graduate level
Each module includes concepts, architecture, implementation, and constraints

## RAG Chatbot Constraints

Stack: OpenAI Agents/ChatKit, FastAPI, Neon Postgres, Qdrant Cloud
Answers only from indexed book content
Must respect user-selected text boundaries
No hallucinations; cite chapter/section in responses

## Governance

This constitution is the supreme governing document for the project. All amendments must be formally documented, approved by project leadership, and include a migration plan if applicable. Compliance with this constitution will be verified through code reviews and regular audits. Adherence to these principles is mandatory for all contributors.

**Version**: 0.1.0 | **Ratified**: TODO(RATIFICATION_DATE): Original adoption date is unknown, please provide. | **Last Amended**: 2025-12-15

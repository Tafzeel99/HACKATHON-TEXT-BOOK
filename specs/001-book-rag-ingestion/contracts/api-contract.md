# API Contract: Content-to-Vector Pipeline

## Overview
This contract defines the expected behavior and interfaces for the Content-to-Vector Pipeline system that extracts content from Docusaurus URLs, generates embeddings using Cohere, and stores them in Qdrant.

## Functional Requirements Mapping

### FR-001: Content Extraction
**Requirement**: System MUST extract clean text content from published Docusaurus book URLs while excluding navigation, headers, footers, and other non-content elements

**Implementation**: `extract_text_from_url(url)` function
- Input: URL string
- Output: Clean text content string
- Behavior: Uses BeautifulSoup to parse HTML and extract main content areas

### FR-002: Content Segmentation
**Requirement**: System MUST segment extracted content into appropriately sized chunks suitable for embedding generation

**Implementation**: `chunk_text(text, chunk_size=1000, overlap=100)` function
- Input: Text string, chunk size, overlap
- Output: List of text chunk strings
- Behavior: Splits text into overlapping chunks with word-boundary awareness

### FR-003: Embedding Generation
**Requirement**: System MUST generate vector embeddings from text segments using the Cohere embedding API

**Implementation**: `embed(texts)` function
- Input: List of text strings
- Output: List of embedding vectors
- Behavior: Calls Cohere's embed API with search_document input type

### FR-004: Vector Storage
**Requirement**: System MUST store generated embeddings in Qdrant vector database with associated metadata

**Implementation**: `save_chunk_to_qdrant(text_chunk, embedding, url, collection_name="rag_embedding")` function
- Input: Text chunk, embedding vector, source URL, collection name
- Output: None (side effect: storage in Qdrant)
- Behavior: Stores vector with metadata payload in Qdrant collection

### FR-005: Metadata Preservation
**Requirement**: System MUST preserve source document information and content hierarchy in the stored embeddings metadata

**Implementation**: Metadata stored in Qdrant payload includes:
- text: Original text content
- url: Source URL
- timestamp: Processing timestamp

### FR-006: Error Handling
**Requirement**: System MUST handle API rate limiting and errors from both Docusaurus source and Cohere embedding services gracefully

**Implementation**: Try-catch blocks with logging in all functions, graceful degradation strategies

### FR-007: Configurable Chunking
**Requirement**: System MUST support configurable chunk sizes for content segmentation with a default range of 500-1000 tokens

**Implementation**: `chunk_text()` function accepts configurable chunk_size parameter with 1000 default

### FR-008: Incremental Updates
**Requirement**: System MUST support incremental updates to reflect changes in source Docusaurus content over time

**Implementation**: Each chunk has unique ID and timestamp, allowing for tracking and updating of content over time

## Data Contracts

### Input: URL
- Type: String
- Format: Valid URL
- Required: Yes

### Output: Text Content
- Type: String
- Format: Clean text without HTML tags
- Required: Yes (empty string if extraction fails)

### Output: Embedding Vector
- Type: Array of floats
- Size: Determined by Cohere model (typically 1024 dimensions)
- Required: Yes (empty array if embedding fails)

### Storage Payload
- text: String (original content)
- url: String (source URL)
- timestamp: Float (Unix timestamp)
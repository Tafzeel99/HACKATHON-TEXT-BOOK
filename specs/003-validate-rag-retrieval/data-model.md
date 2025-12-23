# Data Model: Validate RAG Retrieval Pipeline

## Overview
This document describes the key data entities involved in the RAG retrieval validation system, based on the entities identified in the feature specification.

## Core Entities

### 1. Query
**Description**: Natural language input from user seeking specific textbook information, containing search terms and context
**Fields**:
- `text`: string - The actual query text submitted by the user
- `embedding`: List[float] - Vector representation of the query text
- `timestamp`: datetime - When the query was submitted
- `user_context`: string (optional) - Additional context provided by the user

**Validation Rules**:
- Text must not be empty (after trimming whitespace)
- Text length should be reasonable (e.g., < 1000 characters)
- Embedding must have the correct dimension (1024 for Cohere embed-english-v3.0)

### 2. Retrieved Passage
**Description**: Text segment from textbook that matches the query semantically, including content, metadata, and similarity score
**Fields**:
- `text`: string - The actual text content of the retrieved passage
- `url`: string - Source URL where the text originated
- `score`: float - Similarity score indicating relevance to the query
- `timestamp`: datetime - When the passage was originally indexed
- `module`: string (optional) - Module or section identifier
- `section`: string (optional) - Specific section identifier

**Validation Rules**:
- Text content must not be empty
- URL must be a valid URL format
- Score must be between 0 and 1 (or appropriate similarity range)
- All metadata fields should be present and accurate

### 3. Vector Database
**Description**: Storage system containing embedded textbook content with metadata for similarity search
**Fields**:
- `collection_name`: string - Name of the vector collection (e.g., "rag_embedding")
- `vector_size`: int - Dimension of the embedding vectors (e.g., 1024)
- `distance_metric`: string - Distance metric used for similarity (e.g., "cosine")
- `total_points`: int - Number of vectors stored in the collection

**Validation Rules**:
- Collection must exist and be accessible
- Vector dimensions must match expected size
- Database must be responsive to queries

### 4. Similarity Score
**Description**: Numerical measure indicating how semantically related a retrieved passage is to the original query
**Fields**:
- `value`: float - The actual similarity score value
- `confidence`: float (optional) - Confidence level in the score
- `algorithm`: string - Algorithm used to compute the similarity (e.g., "cosine_similarity")

**Validation Rules**:
- Value must be in the expected range (typically 0-1 or -1 to 1)
- Higher scores should correspond to more relevant results
- Scores should be consistently ordered in search results

## Relationships

### Query → Retrieved Passage
- **Relationship**: One-to-Many
- **Description**: A single query can return multiple retrieved passages
- **Constraint**: Passages are ranked by similarity score in descending order

### Retrieved Passage → Vector Database
- **Relationship**: Many-to-One
- **Description**: Multiple passages are stored within the same vector database
- **Constraint**: Each passage has a unique identifier within the database

### Query → Similarity Score
- **Relationship**: One-to-Many
- **Description**: A query generates similarity scores for each retrieved passage
- **Constraint**: Each score is specific to the query-passage pair

## State Transitions

### Query Processing States
1. **Submitted**: Query text is received but not yet processed
2. **Embedded**: Query has been converted to vector representation
3. **Searched**: Vector search has been performed against the database
4. **Ranked**: Results have been ordered by similarity scores
5. **Validated**: Results have been validated for quality and metadata accuracy
6. **Returned**: Results have been delivered to the user

## Validation Requirements

### Data Integrity
- All retrieved passages must have complete metadata (URL, module, section)
- Similarity scores must be properly ordered (descending)
- Query embeddings must match the expected dimension

### Quality Metrics
- At least 95% of queries should return semantically relevant passages
- Top-3 results should contain relevant information for 90% of test queries
- Metadata accuracy rate should be 99% or higher
- Similarity scores should be above 0.7 for relevant content in 98% of cases

### Performance Constraints
- Query response time must remain under 2 seconds for 99% of requests
- System must handle edge cases gracefully without crashing
- Database operations should maintain consistent performance
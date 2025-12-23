# Data Model: Neon DB Integration

## Entity: BookModules
**Description**: Stores information about book modules/chapters

**Fields**:
- `id`: UUID (Primary Key)
- `title`: String (Module/chapter title)
- `keyword`: String (Searchable keyword for the module)
- `short_answer`: Text (Maximum 3 sentences explanation)
- `chapter`: String (Chapter identifier)
- `page`: Integer (Page number reference)
- `confidence_score`: Float (0.0-1.0 confidence in the answer)
- `created_at`: DateTime (Timestamp of creation)
- `updated_at`: DateTime (Timestamp of last update)

**Validation**:
- `title` and `keyword` are required
- `short_answer` must be <= 3 sentences
- `confidence_score` must be between 0.0 and 1.0
- `page` must be positive integer

## Entity: BookChapters
**Description**: Stores detailed chapter information

**Fields**:
- `id`: UUID (Primary Key)
- `title`: String (Chapter title)
- `keyword`: String (Searchable keyword for the chapter)
- `short_answer`: Text (Maximum 3 sentences summary)
- `chapter_number`: String (Chapter identifier)
- `page_range`: String (Page range, e.g., "15-30")
- `confidence_score`: Float (0.0-1.0 confidence in the answer)
- `created_at`: DateTime (Timestamp of creation)
- `updated_at`: DateTime (Timestamp of last update)

**Validation**:
- `title` and `keyword` are required
- `short_answer` must be <= 3 sentences
- `confidence_score` must be between 0.0 and 1.0
- `chapter_number` is required

## Entity: Definitions
**Description**: Stores canonical definitions for key terms

**Fields**:
- `id`: UUID (Primary Key)
- `term`: String (The term being defined)
- `keyword`: String (Alternative search terms)
- `definition`: Text (Maximum 3 sentences definition)
- `category`: String (Category of the term)
- `confidence_score`: Float (0.0-1.0 confidence in the definition)
- `source`: String (Source reference, e.g., "Chapter 2, Page 45")
- `created_at`: DateTime (Timestamp of creation)
- `updated_at`: DateTime (Timestamp of last update)

**Validation**:
- `term` is required
- `definition` must be <= 3 sentences
- `confidence_score` must be between 0.0 and 1.0

## Entity: Glossary
**Description**: Stores glossary entries for book terminology

**Fields**:
- `id`: UUID (Primary Key)
- `term`: String (The term in the glossary)
- `keyword`: String (Alternative search terms)
- `explanation`: Text (Maximum 3 sentences explanation)
- `category`: String (Category of the term)
- `confidence_score`: Float (0.0-1.0 confidence in the explanation)
- `created_at`: DateTime (Timestamp of creation)
- `updated_at`: DateTime (Timestamp of last update)

**Validation**:
- `term` is required
- `explanation` must be <= 3 sentences
- `confidence_score` must be between 0.0 and 1.0

## Entity: TocIndex
**Description**: Table of contents index for quick navigation

**Fields**:
- `id`: UUID (Primary Key)
- `title`: String (Section title)
- `keyword`: String (Searchable keyword)
- `summary`: Text (Maximum 3 sentences summary)
- `chapter`: String (Chapter identifier)
- `section`: String (Section identifier)
- `page`: Integer (Page number)
- `confidence_score`: Float (0.0-1.0 confidence in the summary)
- `created_at`: DateTime (Timestamp of creation)
- `updated_at`: DateTime (Timestamp of last update)

**Validation**:
- `title` and `keyword` are required
- `summary` must be <= 3 sentences
- `confidence_score` must be between 0.0 and 1.0
- `page` must be positive integer

## Relationships
- No direct relationships between entities (read-optimized design)
- Each entity is independently searchable by keyword/title
- All entities support full-text search on relevant fields

## Database Schema Considerations
- All text fields use appropriate indexing for search performance
- Confidence scores enable ranking of results
- Timestamps support content freshness tracking
- UUID primary keys ensure global uniqueness
-- Migration: Create Neon DB tables for structured knowledge

-- Create book_modules table
CREATE TABLE IF NOT EXISTS book_modules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    keyword VARCHAR(255) NOT NULL,
    short_answer TEXT NOT NULL,
    chapter VARCHAR(100),
    page INTEGER,
    confidence_score DECIMAL(3,2) CHECK (confidence_score >= 0.0 AND confidence_score <= 1.0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create book_chapters table
CREATE TABLE IF NOT EXISTS book_chapters (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    keyword VARCHAR(255) NOT NULL,
    short_answer TEXT NOT NULL,
    chapter_number VARCHAR(50) NOT NULL,
    page_range VARCHAR(50),
    confidence_score DECIMAL(3,2) CHECK (confidence_score >= 0.0 AND confidence_score <= 1.0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create definitions table
CREATE TABLE IF NOT EXISTS definitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    term VARCHAR(255) NOT NULL,
    keyword VARCHAR(255),
    definition TEXT NOT NULL,
    category VARCHAR(100),
    confidence_score DECIMAL(3,2) CHECK (confidence_score >= 0.0 AND confidence_score <= 1.0),
    source VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create glossary table
CREATE TABLE IF NOT EXISTS glossary (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    term VARCHAR(255) NOT NULL,
    keyword VARCHAR(255),
    explanation TEXT NOT NULL,
    category VARCHAR(100),
    confidence_score DECIMAL(3,2) CHECK (confidence_score >= 0.0 AND confidence_score <= 1.0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create toc_index table
CREATE TABLE IF NOT EXISTS toc_index (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    keyword VARCHAR(255) NOT NULL,
    summary TEXT NOT NULL,
    chapter VARCHAR(100),
    section VARCHAR(100),
    page INTEGER,
    confidence_score DECIMAL(3,2) CHECK (confidence_score >= 0.0 AND confidence_score <= 1.0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better search performance
CREATE INDEX IF NOT EXISTS idx_book_modules_keyword ON book_modules(keyword);
CREATE INDEX IF NOT EXISTS idx_book_modules_title ON book_modules(title);
CREATE INDEX IF NOT EXISTS idx_book_chapters_keyword ON book_chapters(keyword);
CREATE INDEX IF NOT EXISTS idx_book_chapters_title ON book_chapters(title);
CREATE INDEX IF NOT EXISTS idx_definitions_keyword ON definitions(keyword);
CREATE INDEX IF NOT EXISTS idx_definitions_term ON definitions(term);
CREATE INDEX IF NOT EXISTS idx_glossary_keyword ON glossary(keyword);
CREATE INDEX IF NOT EXISTS idx_glossary_term ON glossary(term);
CREATE INDEX IF NOT EXISTS idx_toc_index_keyword ON toc_index(keyword);
CREATE INDEX IF NOT EXISTS idx_toc_index_title ON toc_index(title);

-- Create a full-text search index for content-based search
CREATE INDEX IF NOT EXISTS idx_definitions_fulltext ON definitions USING gin(to_tsvector('english', definition));
CREATE INDEX IF NOT EXISTS idx_glossary_fulltext ON glossary USING gin(to_tsvector('english', explanation));
CREATE INDEX IF NOT EXISTS idx_book_modules_fulltext ON book_modules USING gin(to_tsvector('english', short_answer));
CREATE INDEX IF NOT EXISTS idx_book_chapters_fulltext ON book_chapters USING gin(to_tsvector('english', short_answer));
CREATE INDEX IF NOT EXISTS idx_toc_index_fulltext ON toc_index USING gin(to_tsvector('english', summary));
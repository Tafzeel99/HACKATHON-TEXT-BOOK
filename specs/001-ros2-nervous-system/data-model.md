# Data Model

This document defines the key entities for the book.

## Module

A module is a collection of chapters on a related topic.

**Attributes**:
- `title`: The title of the module.
- `summary`: A brief summary of the module.

## Chapter

A chapter is a self-contained section of a module.

**Attributes**:
- `title`: The title of the chapter.
- `content`: The content of the chapter in Markdown format.
- `order`: The order of the chapter within the module.

**Relationships**:
- A `Module` has many `Chapters`.
- A `Chapter` belongs to one `Module`.

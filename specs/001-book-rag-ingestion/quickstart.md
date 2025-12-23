# Quickstart: Content-to-Vector Pipeline

## Prerequisites
- Python 3.8+
- Cohere API key
- Qdrant instance (local or cloud)

## Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env to add your Cohere API key
```

## Usage

Run the complete Content-to-Vector Pipeline:
```bash
python main.py
```

The pipeline will:
1. Fetch all URLs from the target Docusaurus site (https://physical-ai-robotics-one.vercel.app/cc)
2. Extract text content from each URL
3. Chunk the text into manageable pieces
4. Generate embeddings using Cohere
5. Store embeddings in Qdrant with metadata

## Configuration

- To change the target URL, modify the `target_url` variable in the `main()` function
- To adjust chunk size, modify parameters in the `chunk_text()` function call
- To change the Qdrant collection name, modify the `collection_name` parameter

## Functions Overview

- `get_all_urls(base_url)`: Discovers all pages from the target site
- `extract_text_from_url(url)`: Extracts clean text content from a URL
- `chunk_text(text, chunk_size, overlap)`: Splits text into overlapping chunks
- `embed(texts)`: Generates embeddings using Cohere API
- `create_collection(collection_name)`: Creates Qdrant collection named "rag_embedding"
- `save_chunk_to_qdrant(text_chunk, embedding, url, collection_name, chunk_id)`: Stores embeddings in Qdrant
- `main()`: Orchestrates the entire pipeline
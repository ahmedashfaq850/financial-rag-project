# RAG System

A Python retrieval-augmented generation (RAG) system built with [uv](https://docs.astral.sh/uv/).

## Features

- **Document ingestion** — `.txt`, `.md`, and `.pdf` files
- **Local embeddings** — [sentence-transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2` by default)
- **Vector store** — [ChromaDB](https://www.trychroma.com/) with persistent storage
- **LLM generation** — any OpenAI-compatible API (Ollama, OpenAI, etc.)
- **CLI** — ingest, query, status, and reset commands

## Quick Start

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- An LLM server (e.g. [Ollama](https://ollama.com/) running locally)

### Setup

```bash
# Install dependencies
uv sync

# Copy environment config (optional — defaults work with Ollama)
cp .env.example .env
```

### Usage

```bash
# Ingest documents from data/
uv run rag ingest

# Ask a question
uv run rag ask "What is RAG?"

# Retrieve context only (no LLM call)
uv run rag ask "What is RAG?" --retrieve-only

# Check index status
uv run rag status

# Clear the vector store
uv run rag reset
```

Add your own documents to the `data/` directory before running `rag ingest`.

## Project Structure

```
rag-project/
├── data/                  # Documents to ingest
├── chroma_db/             # Vector store (created on first ingest)
├── src/rag_system/
│   ├── config.py          # Settings (env vars)
│   ├── loader.py          # Document loading
│   ├── chunker.py         # Text splitting
│   ├── embedder.py        # Sentence embeddings
│   ├── store.py           # ChromaDB vector store
│   ├── generator.py       # LLM generation
│   ├── pipeline.py        # RAG orchestration
│   └── cli.py             # Typer CLI
├── pyproject.toml
└── .env.example
```

## Configuration

All settings can be overridden via environment variables or a `.env` file. See `.env.example` for the full list.

| Variable | Default | Description |
|---|---|---|
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Sentence-transformers model |
| `CHUNK_SIZE` | `512` | Characters per chunk |
| `CHUNK_OVERLAP` | `64` | Overlap between chunks |
| `TOP_K` | `4` | Chunks retrieved per query |
| `LLM_BASE_URL` | `http://localhost:11434/v1` | OpenAI-compatible API base URL |
| `LLM_MODEL` | `llama3.2` | Model name for generation |

## Development

```bash
uv sync          # install deps
uv run rag --help
```

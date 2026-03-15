# Dependencies Reference

## Core LangChain
| Package | Why |
|---|---|
| `langchain` | Core framework — chains, agents, tools |
| `langchain-core` | Base interfaces, LCEL |
| `langchain-community` | Community integrations (document loaders, etc.) |
| `langchain-groq` | Groq LLM integration |
| `langgraph` | Agent orchestration with state management |

## LLM & Embeddings
| Package | Why |
|---|---|
| `groq` | Groq SDK (needed by langchain-groq) |
| `sentence-transformers` | HuggingFace local embeddings |

## Document Processing
| Package | Why |
|---|---|
| `pypdf` | Read PDF files |
| `unstructured` | Parse complex docs (word, html, etc.) |
| `python-docx` | Read .docx files |

## Vector Store
| Package | Why |
|---|---|
| `chromadb` | Local vector database to store embeddings |

## API Layer
| Package | Why |
|---|---|
| `fastapi` | Serve the agent as REST API |
| `uvicorn` | ASGI server to run FastAPI |
| `python-multipart` | Handle file uploads in FastAPI |

## Config & Validation
| Package | Why |
|---|---|
| `pydantic-settings` | Load and validate env variables |
| `python-dotenv` | Load `.env` file |

## Dev Only
| Package | Why |
|---|---|
| `pytest` | Testing |
| `pytest-asyncio` | Async test support |
| `ruff` | Linter + formatter |
| `httpx` | Test FastAPI endpoints |

## Prod Only
| Package | Why |
|---|---|
| `gunicorn` | Production WSGI server |

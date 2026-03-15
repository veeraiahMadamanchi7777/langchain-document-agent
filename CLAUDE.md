i am a lerner and i want to learn how to use claude in langchain document agent.Learning

# Project: langchain-document-agent

## Overview
Enterprise-ready Document Q&A Agent built with LangChain.
Users upload documents (PDF/text), ask questions, get answers with sources.

## Tech Stack
- LangChain + LangGraph
- Groq (LLM — llama-3.3-70b, free tier)
- HuggingFace Embeddings (local, free — sentence-transformers/all-MiniLM-L6-v2)
- ChromaDB (Vector Store)
- FastAPI (API layer)
- Pydantic v2 (schemas)
- Python 3.11+

## Design Principles
- Embeddings are swappable via strategy pattern — add new providers in src/retrievers/
- LLM provider is swappable — add new providers in src/core/
- Never couple business logic to a specific model/provider

## Project Structure
See docs/project-structure.md for full layout.

## Dependencies
See docs/dependencies.md for full list with explanations.

## Coding Conventions
- One class per file
- All inputs/outputs must have Pydantic schemas in src/schemas/
- All prompts live in src/prompts/ — never hardcode prompts inline
- Use LCEL (pipe syntax) for all chains
- All config loaded via environment variables — never hardcode secrets
- Every public function must have type hints

## What NOT to do
- Do not put business logic in api/routes
- Do not hardcode model names — always load from config
- Do not use global state

## Environment
- Use .env.example as template — never commit .env
- Config files per environment in config/ folder

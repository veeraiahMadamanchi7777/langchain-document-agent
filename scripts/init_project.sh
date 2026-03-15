#!/bin/bash

echo "Initializing langchain-document-agent project structure..."

# Source directories
mkdir -p src/core
mkdir -p src/agents
mkdir -p src/tools
mkdir -p src/chains
mkdir -p src/prompts
mkdir -p src/schemas
mkdir -p src/utils
mkdir -p src/retrievers
mkdir -p src/memory
mkdir -p src/api/routes

# Tests
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p tests/e2e

# Other directories
mkdir -p config
mkdir -p docs
mkdir -p scripts
mkdir -p requirements

# __init__.py files
touch src/__init__.py
touch src/core/__init__.py
touch src/agents/__init__.py
touch src/tools/__init__.py
touch src/chains/__init__.py
touch src/prompts/__init__.py
touch src/schemas/__init__.py
touch src/utils/__init__.py
touch src/retrievers/__init__.py
touch src/memory/__init__.py
touch src/api/__init__.py
touch src/api/routes/__init__.py

# Requirement files
touch requirements/base.txt
touch requirements/dev.txt
touch requirements/prod.txt

# Root files
touch pyproject.toml
touch .env.example
touch .gitignore
touch README.md
touch docs/project-structure.md

echo "Project structure initialized successfully!"
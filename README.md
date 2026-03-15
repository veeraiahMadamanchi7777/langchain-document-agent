# LangChain Document Agent

An enterprise-ready Document Q&A Agent built with LangChain. Upload documents (PDF/text/docx), ask questions, get answers with sources.

## Tech Stack
- **LLM**: Groq (llama-3.3-70b) — free tier
- **Embeddings**: HuggingFace sentence-transformers (local, free)
- **Vector Store**: ChromaDB
- **API**: FastAPI
- **Orchestration**: LangGraph

## Project Structure
See [docs/project-structure.md](docs/project-structure.md)

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/veeraiahMadamanchi7777/langchain-document-agent.git
cd langchain-document-agent
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements/dev.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
# Add your GROQ_API_KEY to .env
```

### 5. Run the API
```bash
uvicorn src.api.main:app --reload
```

## Dependencies
See [docs/dependencies.md](docs/dependencies.md)

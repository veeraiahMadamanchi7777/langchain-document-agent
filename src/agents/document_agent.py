from src.agents.base_agent import BaseAgent
from src.chains.qa_chain import build_qa_chain
from src.retrievers.vector_store import VectorStore
from src.schemas.chat import ChatRequest, ChatResponse, Source
from src.utils.logger import get_logger

logger = get_logger(__name__)


class DocumentAgent(BaseAgent):

    def __init__(self):
        self._vector_store = VectorStore()

    async def run(self, request: ChatRequest) -> ChatResponse:
        logger.info(f"Running DocumentAgent for question: {request.question}")

        retriever = self._vector_store.get_retriever(
            document_id=request.document_id
        )

        chain = build_qa_chain(retriever)
        answer = await chain.ainvoke(request.question)

        sources = await self._get_sources(request)

        return ChatResponse(
            answer=answer,
            sources=sources,
            session_id=request.session_id or "default",
        )

    async def _get_sources(self, request: ChatRequest) -> list[Source]:
        retriever = self._vector_store.get_retriever(
            document_id=request.document_id
        )
        docs = await retriever.ainvoke(request.question)
        sources = []
        seen = set()

        for doc in docs:
            doc_id = doc.metadata.get("document_id", "unknown")
            filename = doc.metadata.get("filename", "unknown")
            page = doc.metadata.get("page", None)
            key = (doc_id, page)

            if key not in seen:
                seen.add(key)
                sources.append(Source(
                    document_id=doc_id,
                    filename=filename,
                    page=page,
                    content_preview=doc.page_content[:200],
                ))

        return sources

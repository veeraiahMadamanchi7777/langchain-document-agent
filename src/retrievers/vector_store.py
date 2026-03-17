from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever
from src.core.config import get_settings
from src.retrievers.embeddings import get_embedding_provider
from src.utils.logger import get_logger

logger = get_logger(__name__)


class VectorStore:
    def __init__(self):
        settings = get_settings()
        embeddings = get_embedding_provider().get_embeddings()
        self._store = Chroma(
            collection_name=settings.chroma_collection_name,
            embedding_function=embeddings,
            persist_directory=settings.chroma_db_path,
        )
        logger.info("VectorStore initialized")

    def add_documents(self, documents: list[Document], document_id: str) -> int:
        for doc in documents:
            doc.metadata["document_id"] = document_id
        self._store.add_documents(documents)
        logger.info(f"Added {len(documents)} chunks for document_id={document_id}")
        return len(documents)

    def get_retriever(self, document_id: str | None = None) -> VectorStoreRetriever:
        settings = get_settings()
        search_kwargs = {"k": settings.retriever_top_k}
        if document_id:
            search_kwargs["filter"] = {"document_id": document_id}
        return self._store.as_retriever(search_kwargs=search_kwargs)

    def delete_document(self, document_id: str) -> None:
        self._store.delete(where={"document_id": document_id})
        logger.info(f"Deleted document_id={document_id} from vector store")

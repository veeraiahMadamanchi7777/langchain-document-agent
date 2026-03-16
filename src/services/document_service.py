import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader, CSVLoader, UnstructuredHTMLLoader
from langchain_core.documents import Document
from src.core.config import get_settings
from src.retrievers.vector_store import VectorStore
from src.schemas.document import DocumentStatus, DocumentUploadResponse
from src.utils.file_validator import validate_file
from src.utils.id_generator import generate_document_id
from src.utils.text_splitter import split_documents
from src.utils.logger import get_logger

logger = get_logger(__name__)

LOADER_MAP = {
    "pdf": PyPDFLoader,
    "txt": TextLoader,
    "docx": Docx2txtLoader,
    "csv": CSVLoader,
    "html": UnstructuredHTMLLoader,
    "md": TextLoader,
}


class DocumentService:

    def __init__(self):
        self._vector_store = VectorStore()
        self._settings = get_settings()

    async def ingest(self, filename: str, file_bytes: bytes) -> DocumentUploadResponse:
        document_id = generate_document_id()
        logger.info(f"Ingesting document: {filename} | id={document_id}")

        # Validate
        is_valid, message = validate_file(filename, len(file_bytes))
        if not is_valid:
            return DocumentUploadResponse(
                document_id=document_id,
                filename=filename,
                status=DocumentStatus.FAILED,
                message=message,
            )

        # Save file temporarily
        upload_path = Path(self._settings.upload_dir)
        upload_path.mkdir(parents=True, exist_ok=True)
        file_path = upload_path / f"{document_id}_{filename}"
        file_path.write_bytes(file_bytes)

        try:
            # Load
            docs = self._load(str(file_path), filename)

            # Attach metadata
            for doc in docs:
                doc.metadata["document_id"] = document_id
                doc.metadata["filename"] = filename

            # Split
            chunks = split_documents(docs)

            # Store in vector DB
            chunk_count = self._vector_store.add_documents(chunks, document_id)

            logger.info(f"Document ingested: {filename} | chunks={chunk_count}")
            return DocumentUploadResponse(
                document_id=document_id,
                filename=filename,
                status=DocumentStatus.READY,
                message=f"Document processed successfully. {chunk_count} chunks indexed.",
            )

        except Exception as e:
            logger.error(f"Failed to ingest {filename}: {e}")
            return DocumentUploadResponse(
                document_id=document_id,
                filename=filename,
                status=DocumentStatus.FAILED,
                message=f"Processing failed: {str(e)}",
            )
        finally:
            if file_path.exists():
                os.remove(file_path)

    def _load(self, file_path: str, filename: str) -> list[Document]:
        ext = Path(filename).suffix.lower().lstrip(".")
        loader_class = LOADER_MAP.get(ext)
        if not loader_class:
            raise ValueError(f"No loader for extension: {ext}")
        loader = loader_class(file_path)
        return loader.load()

    def delete(self, document_id: str) -> None:
        self._vector_store.delete_document(document_id)
        logger.info(f"Document deleted: {document_id}")

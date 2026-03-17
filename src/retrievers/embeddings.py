from abc import ABC, abstractmethod
from langchain_core.embeddings import Embeddings
from langchain_huggingface import HuggingFaceEmbeddings
from src.core.config import get_settings
from src.utils.logger import get_logger

logger = get_logger(__name__)


class BaseEmbeddings(ABC):
    @abstractmethod
    def get_embeddings(self) -> Embeddings:
        pass


class HuggingFaceEmbeddingProvider(BaseEmbeddings):
    def get_embeddings(self) -> Embeddings:
        settings = get_settings()
        logger.info(f"Loading HuggingFace embeddings: {settings.embedding_model}")
        return HuggingFaceEmbeddings(
            model_name=settings.embedding_model,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )


def get_embedding_provider() -> BaseEmbeddings:
    settings = get_settings()
    providers = {
        "huggingface": HuggingFaceEmbeddingProvider,
    }
    provider_class = providers.get(settings.embedding_provider)
    if not provider_class:
        raise ValueError(f"Unknown embedding provider: {settings.embedding_provider}")
    return provider_class()

from langchain_groq import ChatGroq
from langchain_core.language_models import BaseChatModel
from src.core.config import get_settings
from src.utils.logger import get_logger

logger = get_logger(__name__)


def get_llm() -> BaseChatModel:
    settings = get_settings()
    logger.info(f"Loading LLM: {settings.llm_provider} / {settings.llm_model}")
    return ChatGroq(
        api_key=settings.groq_api_key,
        model=settings.llm_model,
        temperature=settings.llm_temperature,
        max_tokens=settings.llm_max_tokens,
    )

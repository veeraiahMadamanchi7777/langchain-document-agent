from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


def _get_env_files() -> tuple[Path, ...]:
    base_dir = Path(__file__).resolve().parents[2]
    env_file = base_dir / ".env"

    app_env = "development"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("APP_ENV="):
                app_env = line.split("=", 1)[1].strip()
                break

    config_file = base_dir / f"config/{app_env}.env"
    return (env_file, config_file)


class AppSettings(BaseSettings):
    # Application
    app_env: str = "development"
    app_name: str = "langchain-document-agent"
    app_version: str = "0.1.0"
    debug: bool = False

    # Logging
    log_level: str = "INFO"

    # Secrets
    groq_api_key: str

    # LLM
    llm_provider: str = "groq"
    llm_model: str = "llama-3.3-70b-versatile"
    llm_temperature: float = 0.0
    llm_max_tokens: int = 4096

    # Embeddings
    embedding_provider: str = "huggingface"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Vector Store
    chroma_db_path: str = "./chroma_db"
    chroma_collection_name: str = "documents"

    # Document Upload
    upload_dir: str = "./uploads"
    max_upload_size_mb: int = 50
    allowed_extensions: str = "pdf,txt,docx"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_workers: int = 1

    # Retrieval
    retriever_top_k: int = 5
    retriever_score_threshold: float = 0.5

    @property
    def allowed_extensions_list(self) -> list[str]:
        return [ext.strip() for ext in self.allowed_extensions.split(",")]

    model_config = SettingsConfigDict(
        env_file=_get_env_files(),
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()

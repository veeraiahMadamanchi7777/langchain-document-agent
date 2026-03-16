from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import documents, chat
from src.core.config import get_settings
from src.utils.logger import get_logger

logger = get_logger(__name__)


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Enterprise Document Q&A Agent powered by LangChain + Groq",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(documents.router, prefix="/api/v1")
    app.include_router(chat.router, prefix="/api/v1")

    @app.get("/health")
    def health():
        return {"status": "ok", "env": settings.app_env, "version": settings.app_version}

    logger.info(f"App created: {settings.app_name} v{settings.app_version}")
    return app

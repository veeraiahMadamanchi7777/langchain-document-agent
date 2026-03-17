from fastapi import APIRouter, HTTPException
from src.agents.document_agent import DocumentAgent
from src.schemas.chat import ChatRequest, ChatResponse
from src.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter(prefix="/chat", tags=["Chat"])
_agent = DocumentAgent()


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    logger.info(f"Chat request: {request.question}")
    try:
        response = await _agent.run(request)
        return response
    except Exception as e:
        logger.error(f"Chat failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

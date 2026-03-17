from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=1000)
    document_id: str | None = None  # None means search across all docs
    session_id: str | None = None   # for conversation memory


class Source(BaseModel):
    document_id: str
    filename: str
    page: int | None = None
    content_preview: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]
    session_id: str

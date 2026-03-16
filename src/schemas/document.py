from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class DocumentStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"


class DocumentUploadResponse(BaseModel):
    document_id: str
    filename: str
    status: DocumentStatus
    message: str


class DocumentInfo(BaseModel):
    document_id: str
    filename: str
    status: DocumentStatus
    chunk_count: int = 0
    created_at: datetime

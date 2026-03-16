from fastapi import APIRouter, UploadFile, File, HTTPException
from src.schemas.document import DocumentUploadResponse
from src.services.document_service import DocumentService
from src.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter(prefix="/documents", tags=["Documents"])
_service = DocumentService()


@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):
    logger.info(f"Upload request: {file.filename}")
    file_bytes = await file.read()
    result = await _service.ingest(filename=file.filename, file_bytes=file_bytes)
    return result


@router.delete("/{document_id}")
async def delete_document(document_id: str):
    try:
        _service.delete(document_id)
        return {"message": f"Document {document_id} deleted successfully"}
    except Exception as e:
        logger.error(f"Delete failed for {document_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

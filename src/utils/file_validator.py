from pathlib import Path
from src.core.config import get_settings
from src.utils.logger import get_logger

logger = get_logger(__name__)


def validate_file(filename: str, file_size_bytes: int) -> tuple[bool, str]:
    settings = get_settings()

    # Check extension
    ext = Path(filename).suffix.lower().lstrip(".")
    if ext not in settings.allowed_extensions_list:
        return False, f"File type '.{ext}' not allowed. Allowed: {settings.allowed_extensions}"

    # Check size
    max_bytes = settings.max_upload_size_mb * 1024 * 1024
    if file_size_bytes > max_bytes:
        return False, f"File too large. Max size: {settings.max_upload_size_mb}MB"

    logger.debug(f"File validated: {filename} ({file_size_bytes} bytes)")
    return True, "File is valid"

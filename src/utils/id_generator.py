import uuid


def generate_document_id() -> str:
    return f"doc_{uuid.uuid4().hex[:12]}"


def generate_session_id() -> str:
    return f"session_{uuid.uuid4().hex[:12]}"

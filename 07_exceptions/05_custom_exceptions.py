"""
Phase 1 - Exceptions: Custom Application Exception Hierarchy
"""

class AppBaseException(Exception):
    """Base exception for application domain errors."""
    pass

class ResourceNotFoundError(AppBaseException):
    def __init__(self, resource_type: str, resource_id: str):
        super().__init__(f"{resource_type} with ID '{resource_id}' was not found.")
        self.resource_type = resource_type
        self.resource_id = resource_id

class AuthorizationError(AppBaseException):
    pass

def fetch_document(doc_id: str, is_admin: bool):
    if not is_admin:
        raise AuthorizationError("Access denied: Administrative privileges required.")
    if doc_id != "doc_123":
        raise ResourceNotFoundError("Document", doc_id)
    return {"id": doc_id, "title": "SpeedRun Architecture Guide"}

try:
    fetch_document("doc_999", is_admin=True)
except ResourceNotFoundError as err:
    print(f"Caught custom error: {err}")

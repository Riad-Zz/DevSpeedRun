"""
Phase 1 - Functions: Complex Signatures and Parameter Ordering
"""

def event_dispatcher(event_type: str, *targets, priority: int = 1, **metadata):
    """
    Demonstrates full parameter ordering:
    1. Standard positional (event_type)
    2. *args (*targets)
    3. Keyword-only parameter (priority)
    4. **kwargs (**metadata)
    """
    print(f"Dispatching [{event_type.upper()}] Priority={priority}")
    print(f"  Targets: {targets}")
    print(f"  Metadata: {metadata}")

event_dispatcher(
    "deployment_success",
    "slack_channel", "admin_email",
    priority=5,
    commit_sha="792c5b9",
    environment="production"
)

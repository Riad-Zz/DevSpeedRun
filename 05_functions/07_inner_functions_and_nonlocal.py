"""
Phase 1 - Functions: Enclosing Scope and nonlocal Keyword
"""

def create_counter(start: int = 0):
    """Creates a stateful counter closure utilizing nonlocal."""
    count = start
    
    def increment(step: int = 1) -> int:
        nonlocal count
        count += step
        return count
    
    def get_current() -> int:
        return count
        
    return increment, get_current

inc, get_val = create_counter(10)
print(f"Initial: {get_val()}")
print(f"Step +1: {inc()}")
print(f"Step +5: {inc(5)}")
assert get_val() == 16
print("[OK] Nonlocal enclosure state verified.")

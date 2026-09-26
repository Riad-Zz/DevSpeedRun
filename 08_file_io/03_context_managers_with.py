"""
Phase 1 - File I/O: Custom Context Managers with __enter__ and __exit__
"""

class TimerContext:
    def __init__(self, block_name: str):
        self.block_name = block_name
        self.start_time = None

    def __enter__(self):
        import time
        self.start_time = time.perf_counter()
        print(f"[START] Entering context: {self.block_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = (time.perf_counter() - self.start_time) * 1000
        print(f"[EXIT] Finished context: {self.block_name} in {elapsed:.4f} ms")
        if exc_type is not None:
            print(f"[EXCEPTION HANDLED]: {exc_val}")
            return True  # Suppresses exception

with TimerContext("Calculation Block"):
    total = sum(i ** 2 for i in range(10000))
    print(f"Computed total: {total}")

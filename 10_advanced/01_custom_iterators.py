"""
Phase 1 - Advanced: Custom Iterator Protocol
"""

class CountdownIterator:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

cd = CountdownIterator(5)
print("Countdown iterator:")
for step in cd:
    print(f"Tick: {step}")

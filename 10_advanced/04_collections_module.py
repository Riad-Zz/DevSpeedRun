"""
Phase 1 - Advanced: collections Module (Counter, defaultdict, deque)
"""

from collections import Counter, defaultdict, deque

# Counter: Frequency tracking
words = ["python", "code", "python", "speedrun", "git", "code", "python"]
counter = Counter(words)
print("Word Frequencies:", counter)
print("Most Common 2:", counter.most_common(2))

# defaultdict: Handles missing keys automatically
grouped_words = defaultdict(list)
for w in words:
    grouped_words[len(w)].append(w)
print("Grouped by length:", dict(grouped_words))

# deque: O(1) double-ended queue
q = deque([10, 20, 30])
q.append(40)
q.appendleft(0)
print("Deque after appendleft & append:", q)

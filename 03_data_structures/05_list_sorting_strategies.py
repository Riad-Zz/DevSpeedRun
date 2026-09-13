"""
Phase 1 - Data Structures: Sorting Lists and Key Functions
"""

scores = [88, 42, 95, 71, 100, 63]

# Built-in sorted() creates new sorted copy
sorted_copy = sorted(scores)
print("Original:", scores)
print("New sorted copy:", sorted_copy)

# In-place .sort() modifies original
scores.sort(reverse=True)
print("In-place sorted descending:", scores)

# Sorting with custom key function
words = ["banana", "pie", "watermelon", "fig", "apple"]
words.sort(key=len)
print("Sorted by length:", words)

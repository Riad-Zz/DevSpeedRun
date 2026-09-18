"""
Phase 1 - Comprehensions: Dictionary and Set Comprehensions
"""

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

# Dict Comprehension: word -> character length
word_lengths = {word: len(word) for word in word_list}
print("Word Lengths Dict:", word_lengths)

# Inverting dictionary
inverted = {v: k for k, v in word_lengths.items()}
print("Inverted Dict (length -> word):", inverted)

# Set Comprehension: unique word lengths
unique_lengths = {len(word) for word in word_list}
print("Unique Lengths Set:", unique_lengths)
assert unique_lengths == {3, 4, 5, 6, 10}

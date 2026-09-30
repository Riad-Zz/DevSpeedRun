"""
Phase 1 - OOP: Magic (Dunder) Methods
"""

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

    def __len__(self) -> int:
        return self.pages

    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

b1 = Book("Clean Code", "Robert C. Martin", 464)
b2 = Book("Clean Code", "Robert C. Martin", 464)

print("str(b1):", str(b1))
print("repr(b1):", repr(b1))
print("len(b1):", len(b1))
print("b1 == b2:", b1 == b2)
assert b1 == b2

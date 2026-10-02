"""
Phase 1 - Mini-Project: Interactive CLI Todo List Manager
"""

class TodoManager:
    def __init__(self):
        self.todos = []

    def add_todo(self, title: str) -> dict:
        todo_item = {
            "id": len(self.todos) + 1,
            "title": title,
            "done": False
        }
        self.todos.append(todo_item)
        return todo_item

    def complete_todo(self, todo_id: int) -> bool:
        for t in self.todos:
            if t["id"] == todo_id:
                t["done"] = True
                return True
        return False

    def list_todos(self) -> list:
        return self.todos

# Testing CLI Manager
manager = TodoManager()
manager.add_todo("Complete Phase 1 Python SpeedRun")
manager.add_todo("Review Holy_Claude.py master script")
manager.complete_todo(1)

print("=== Todo List State ===")
for item in manager.list_todos():
    status = "[x]" if item["done"] else "[ ]"
    print(f"{status} #{item['id']}: {item['title']}")

"""
Phase 1 - Functions: Default Arguments and Avoiding Mutable Defaults
"""

# WRONG: def append_item(val, target_list=[]):  <- Mutable default danger!
# RIGHT: Use None as default and initialize inside function
def add_task(task_name: str, task_list: list = None) -> list:
    """Appends task to task_list safely."""
    if task_list is None:
        task_list = []
    task_list.append(task_name)
    return task_list

list_a = add_task("Review PR")
list_b = add_task("Deploy API")

print("List A:", list_a)
print("List B:", list_b)
assert list_a is not list_b, "Lists should be distinct instances"
print("[OK] Mutable default argument trap avoided.")

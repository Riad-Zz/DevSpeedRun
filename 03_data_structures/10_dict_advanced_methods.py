"""
Phase 1 - Data Structures: Advanced Dictionary Operations
"""

metrics = {"cpu": 45.2, "ram": 78.0}

# setdefault: gets value if key exists, inserts default if missing
disk_metric = metrics.setdefault("disk", 55.4)
print("After setdefault('disk'):", metrics)

# .update() to merge another dictionary
new_metrics = {"gpu": 62.1, "ram": 82.5}
metrics.update(new_metrics)
print("After update:", metrics)

# Modern Python 3.9+ Union Operator (|)
extra_data = {"uptime_hours": 320}
merged = metrics | extra_data
print("Merged with (|):", merged)

# .pop() with default fallback
removed_gpu = metrics.pop("gpu", None)
print(f"Popped GPU: {removed_gpu}, Remaining keys: {list(metrics.keys())}")

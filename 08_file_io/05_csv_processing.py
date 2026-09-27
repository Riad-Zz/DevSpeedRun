"""
Phase 1 - File I/O: CSV Processing with DictReader and DictWriter
"""

import csv
import io

# In-memory CSV buffer
csv_buffer = io.StringIO()
fieldnames = ["module_id", "title", "difficulty"]

writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({"module_id": "MOD-01", "title": "Basics & Types", "difficulty": "Easy"})
writer.writerow({"module_id": "MOD-02", "title": "OOP Architecture", "difficulty": "Medium"})
writer.writerow({"module_id": "MOD-03", "title": "Generators & Iterators", "difficulty": "Advanced"})

# Rewind and read
csv_buffer.seek(0)
reader = csv.DictReader(csv_buffer)
print("=== Parsed CSV Modules ===")
for row in reader:
    print(f"[{row['module_id']}] {row['title']} ({row['difficulty']})")

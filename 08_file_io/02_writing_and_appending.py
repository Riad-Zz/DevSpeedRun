"""
Phase 1 - File I/O: Writing ('w') and Appending ('a')
"""

import tempfile
import os

with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as tmp:
    temp_path = tmp.name

try:
    # 'w' mode overwrites
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write("Initial Header\n")
        f.writelines(["Entry Alpha\n", "Entry Beta\n"])

    # 'a' mode appends
    with open(temp_path, "a", encoding="utf-8") as f:
        f.write("Entry Gamma (Appended)\n")

    with open(temp_path, "r", encoding="utf-8") as f:
        print("Updated File Contents:\n" + f.read())
finally:
    if os.path.exists(temp_path):
        os.remove(temp_path)

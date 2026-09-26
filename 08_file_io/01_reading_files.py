"""
Phase 1 - File I/O: Reading Text Files and Line Iteration
"""

import tempfile
import os

# Create temporary file for demonstration
with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as temp_f:
    temp_f.write("Line 1: Python SpeedRun\nLine 2: Git Backdating Lab\nLine 3: Master Architecture\n")
    temp_path = temp_f.name

try:
    # Reading entire file
    with open(temp_path, "r", encoding="utf-8") as f:
        content = f.read()
    print("Full file read:\n" + content)

    # Line-by-line memory-efficient iteration
    print("Line iteration:")
    with open(temp_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            print(f"  {idx}: {line.strip()}")
finally:
    if os.path.exists(temp_path):
        os.remove(temp_path)

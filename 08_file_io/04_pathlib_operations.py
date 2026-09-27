"""
Phase 1 - File I/O: Pathlib Modern Filesystem Paths
"""

from pathlib import Path

# Constructing paths with / operator
current_dir = Path(".")
sub_dir = current_dir / "08_file_io"

print(f"Current Directory: {current_dir.resolve()}")
print(f"Path exists: {current_dir.exists()}")
print(f"Is Directory: {current_dir.is_dir()}")

# Finding python files in workspace
py_files = list(current_dir.glob("*.py"))
print(f"Root Python files found: {[p.name for p in py_files]}")

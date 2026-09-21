"""
Phase 1 - Functions: Variable Scope and the LEGB Hierarchy
Local -> Enclosing -> Global -> Built-in
"""

GLOBAL_SYSTEM_STATUS = "OPERATIONAL"

def audit_system():
    # Reading global variable without modification
    print(f"System audit check: {GLOBAL_SYSTEM_STATUS}")

def update_status(new_status: str):
    global GLOBAL_SYSTEM_STATUS
    GLOBAL_SYSTEM_STATUS = new_status
    print(f"Status updated globally to: {GLOBAL_SYSTEM_STATUS}")

audit_system()
update_status("MAINTENANCE_MODE")
assert GLOBAL_SYSTEM_STATUS == "MAINTENANCE_MODE"
print("[OK] Global variable manipulation understood.")

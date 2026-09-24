"""
Phase 1 - Exceptions: Complete Lifecycle (try, except, else, finally)
"""

def robust_transaction(amount: float, balance: float) -> float:
    try:
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        if amount > balance:
            raise ArithmeticError("Insufficient funds for withdrawal.")
        new_balance = balance - amount
    except (ValueError, ArithmeticError) as error:
        print(f"[ERROR] Transaction aborted: {error}")
        return balance
    else:
        print(f"[SUCCESS] Deducted ${amount:,.2f}. New balance: ${new_balance:,.2f}")
        return new_balance
    finally:
        print("[AUDIT] Transaction record processed and logged.")

curr_bal = 500.0
curr_bal = robust_transaction(150.0, curr_bal)
curr_bal = robust_transaction(600.0, curr_bal)

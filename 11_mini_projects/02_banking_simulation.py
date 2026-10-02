"""
Phase 1 - Mini-Project: Bank Account OOP Simulation
"""

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self._balance = initial_balance
        self.transactions = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self.transactions.append(f"Deposit: +${amount:.2f}")
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError(f"Cannot withdraw ${amount:.2f}. Balance: ${self._balance:.2f}")
        self._balance -= amount
        self.transactions.append(f"Withdrawal: -${amount:.2f}")
        return self._balance

account = BankAccount("Riad", 1000.0)
account.deposit(500.0)
account.withdraw(250.0)
print(f"Final Account Balance for {account.account_holder}: ${account.balance:.2f}")
print("Transactions History:", account.transactions)
assert account.balance == 1250.0

"""
Phase 1 - OOP: @classmethod and @staticmethod
"""

class UserAccount:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    @classmethod
    def from_csv_string(cls, csv_line: str):
        """Alternative constructor from CSV row."""
        username, email = csv_line.strip().split(",")
        return cls(username=username, email=email)

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Utility method without access to cls or self."""
        return "@" in email and "." in email

user = UserAccount.from_csv_string("riad_coder,riad@speedrun.dev")
print(f"Created user: {user.username} <{user.email}>")
print("Valid email check:", UserAccount.is_valid_email(user.email))

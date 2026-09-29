"""
Phase 1 - OOP: Encapsulation and Private Attributes
"""

class SecureVault:
    def __init__(self, owner: str, secret_code: str):
        self.owner = owner          # Public
        self._access_log = []       # Protected convention
        self.__secret_code = secret_code  # Private (name mangled)

    def verify_and_read(self, attempted_code: str) -> str:
        self._access_log.append(f"Attempt made by owner {self.owner}")
        if attempted_code == self.__secret_code:
            return "ACCESS GRANTED: Secret Payload"
        return "ACCESS DENIED"

vault = SecureVault("Riad", "SuperSecret99")
print(vault.verify_and_read("SuperSecret99"))
print(vault.verify_and_read("WrongCode"))

# Accessing name-mangled private attribute (_ClassName__attribute)
print("Private mangled attribute:", vault._SecureVault__secret_code)

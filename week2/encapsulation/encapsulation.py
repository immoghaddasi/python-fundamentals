"""

Refactor BankAccount to make balance private (name-mangled), and provide:
- get_balance() read-only accessor,
- validation inside deposit/withdraw,
- a property is_overdrawn returning True when balance < 0 (should never happen
if validations are correct; include a unit-style check).
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute (name-mangled)

    # Read-only accessor for balance
    def get_balance(self):
        return self.__balance
    
    # Deposit money (must be positive)
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount

    # Withdraw money (must be positive and not exceed balance)
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance -= amount

    # Property to check if the account is overdrawn
    @property
    def is_overdrawn(self):
        """Check if balance < 0 (should never be True with proper validations)"""
        return self.__balance < 0

    # String representation of the account
    def __str__(self):
        """Readable string representation"""
        return f"{self.owner}: {self.__balance}"


# Unit-style check
if __name__ == "__main__":
    account = BankAccount("Alice", 100)

    account.deposit(50)
    account.withdraw(20)
    account.withdraw(200)
    account.deposit(-10)

    print(account)
    print("Balance:", account.get_balance())  
    print("Is overdrawn?", account.is_overdrawn)
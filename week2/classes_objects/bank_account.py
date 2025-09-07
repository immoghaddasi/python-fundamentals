"""

Create a class BankAccount with attributes owner and balance (default 0). Implement
methods:
- deposit(amount) (adds to balance; reject negative amounts),
- withdraw(amount) (subtracts if sufficient funds; otherwise print an error),
- __str__ to display "owner: balance".

Write a short script that creates two accounts, performs a few operations, and prints
results.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        # Initialize account with owner name and optional balance (default = 0)
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        # Add money to the balance if amount is positive
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Subtract money from balance if sufficient funds exist
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def __str__(self):
        # Return a readable string showing owner and balance
        return f"{self.owner}: {self.balance}"


account1 = BankAccount("Alice", 100)
account2 = BankAccount("Bob")

account1.deposit(50)
account1.withdraw(30)
account1.withdraw(200)

account2.deposit(200)
account2.withdraw(50)

print(account1)
print(account2)
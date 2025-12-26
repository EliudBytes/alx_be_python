class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.1f}")

    def display_balance(self):
        print(f"Balance: ${self.balance:.1f}")

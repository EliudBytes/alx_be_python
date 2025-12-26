class BankAccount:
    """A simple bank account with basic operations."""

    def __init__(self, initial_balance: float = 0.0):
        self._account_balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        """Deposit a positive amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._account_balance += float(amount)

    def withdraw(self, amount: float) -> bool:
        """Withdraw if sufficient funds; return True if success, else False."""
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount <= self._account_balance:
            self._account_balance -= float(amount)
            return True
        return False

    def display_balance(self) -> None:
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")

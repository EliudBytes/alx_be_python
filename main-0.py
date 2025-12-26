<<<<<<< HEAD
=======
# main-0.py

>>>>>>> cd1f36565f391e0748cedd655849c2db814bae40
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
<<<<<<< HEAD
=======

>>>>>>> cd1f36565f391e0748cedd655849c2db814bae40
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
<<<<<<< HEAD
=======

>>>>>>> cd1f36565f391e0748cedd655849c2db814bae40
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
<<<<<<< HEAD
    elif command == "display":
        account.display_balance()
=======

    elif command == "display":
        account.display_balance()

>>>>>>> cd1f36565f391e0748cedd655849c2db814bae40
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

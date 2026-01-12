#!/usr/bin/env python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Prompts the user for a monetary amount and ensures valid numeric input.

    Parameters:
        prompt (str): The message shown to the user.

    Returns:
        float: A valid positive amount entered by the user.
    """
    try:
        amount = float(input(prompt))
        return amount
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return None


def main():
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            if amount is not None:
                cb.deposit(amount)

        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            if amount is not None:
                cb.withdraw(amount)

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

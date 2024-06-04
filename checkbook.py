# Class to manage a checkbook with deposit, withdraw, and balance inquiry functionalities

# Function descriptions:
# 1. deposit(amount): Deposit money into the checkbook.
# 2. withdraw(amount): Withdraw money from the checkbook.
# 3. get_balance(): Get the current balance of the checkbook.

# Parameters and returns:
# - deposit(amount): Parameters: amount (float). Returns: None.
# - withdraw(amount): Parameters: amount (float). Returns: None.
# - get_balance(): Parameters: None. Returns: None.

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit money into the checkbook."""
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw money from the checkbook."""
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Get the current balance of the checkbook."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """Main function to interact with the Checkbook class."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
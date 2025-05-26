# Real World Problems
# Bank Account:Saving Account and current account and it will inherit from bank account.
# deposit,withdraw,display balance, types of accounts
# Superclass
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Tolina sente bro!!!")

    def display_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


# Subclass for Saving Account
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        # Storing interest rate for the saving account
        self.interest_rate = interest_rate
        super().__init__(account_number, balance)

    # Add new method for interest rate
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interes of {interest} added. New balance is {self.balance}.")


# Subclass for Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        # Storing overdraft limit for the current account
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal exceeds overdraft limit!")


# Create objects
saving = SavingAccount("SA123", 100000, 5)
current = CurrentAccount("CA123", 50000, 10)
# Test to display
saving.display_balance()
saving.add_interest()
saving.withdraw(20000)
print("_______________________________")
current.display_balance()
current.withdraw(60000)  # Should succeed due to overdraft limit
current.withdraw(100000)  # Should fail due to overdraft limit

class BankAccount:

    def __init__(self, holder_name, initial_balance):
        self.holder_name = holder_name
        self.__balance = initial_balance

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount):
        self.__balance += amount

class SavingsAccount(BankAccount):

    def deposit(self):
        print(f"Savings Account Deposit ({self.holder_name})")
        amount = float(input("Enter the amount to deposit: $"))

        if amount > 0:
            self._update_balance(amount)
            print(f"Success! Deposited: ${amount}")
            print(f"Current balance: ${self.get_balance}")
        else:
            print("Error: Deposit amount must be greater than zero.")

class BusinessAccount(BankAccount):

    def deposit_business(self):
        print(f"Business Account Deposit ({self.holder_name})")
        amount = float(input("Enter the commercial deposit amount: $"))

        if amount > 0:
            self._update_balance(amount)
            print(f"Transaction processed. Amount: ${amount}")
            print(f"Total business balance: ${self.get_balance()}")
        else:
            print("Error: Invalid transaction. Amount must be positive.")

savings = SavingsAccount("John Doe", 1000.00)
business = BusinessAccount("Tech Solutions LLC", 5000.00)

savings.deposit()
business.deposit_business()
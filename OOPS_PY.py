# Encapsulation: BankAccount Class
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        # Private attributes (Encapsulation)
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    # Getter for account holder
    def get_account_holder(self):
        return self.__account_holder

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

# Inheritance: SavingsAccount Class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    # Method to calculate interest
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print(f"Interest earned: {interest}")
        return interest

# Polymorphism: Function that works with any account type
def account_summary(account):
    print("---- Account Summary ----")
    print(f"Account Holder: {account.get_account_holder()}")
    print(f"Balance: {account.get_balance()}")
    if isinstance(account, SavingsAccount):
        account.calculate_interest()

# Abstraction: Abstract Base Class for Loan
from abc import ABC, abstractmethod

class Loan(ABC):
    @abstractmethod
    def calculate_emi(self):
        pass

# Derived class implementing Loan abstraction
class PersonalLoan(Loan):
    def __init__(self, principal, interest_rate, tenure):
        self.principal = principal
        self.interest_rate = interest_rate
        self.tenure = tenure

    def calculate_emi(self):
        # EMI formula: E = P * r * (1 + r)^n / [(1 + r)^n - 1]
        monthly_rate = self.interest_rate / (12 * 100)
        emi = self.principal * monthly_rate * (1 + monthly_rate) ** self.tenure / \
              ((1 + monthly_rate) ** self.tenure - 1)
        print(f"EMI for loan: {emi:.2f}")
        return emi

# Main program
if __name__ == "__main__":
    # Create a BankAccount object (Encapsulation)
    account1 = BankAccount("123456", "John Doe", 5000)
    account1.deposit(1000)
    account1.withdraw(2000)

    # Create a SavingsAccount object (Inheritance)
    savings_account = SavingsAccount("789012", "Jane Smith", 10000, 5)
    savings_account.deposit(2000)
    account_summary(savings_account)

    # Create a PersonalLoan object (Abstraction)
    loan = PersonalLoan(500000, 7.5, 60)  # Principal: 5L, Interest: 7.5%, Tenure: 60 months
    loan.calculate_emi()

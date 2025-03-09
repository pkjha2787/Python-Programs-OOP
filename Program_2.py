# Create a class BankAccount with attributes account_holder and balance, and a method display_balance().

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def display_bal(self):
        return self.balance

# Create a subclass SavingsAccount that overrides display_balance() to include "This is a savings account"
class SavingsAccount(BankAccount):
    def display_bal(self):
        return f"{super().display_bal()}- this is a saving account"
        
acc1=SavingsAccount("John Doe", 1000)
print(acc1.display_bal())
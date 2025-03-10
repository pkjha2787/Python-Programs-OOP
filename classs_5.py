#Create a BankAccount class with attributes account_number and balance. Add methods deposit(amount) and withdraw(amount) to update the balance.
class BankAccount:
    def __init__(self,account_numb,balance,amount):
        self.account_num=account_numb
        self.balance=balance
        self.amount=amount
    def deposit(self):
        if self.amount>0:
            self.balance+=self.amount
            return f"{self.amount} added and Total balance is {self.balance}"
    def withraw(self):
        if self.amount>0 and self.amount< self.balance:
            self.balance-=self.amount
            return f"{self.amount} is withdrawn and Current balance is {self.balance}"
acc1=BankAccount(111,1000,100)
print(acc1.deposit())
print(acc1.withraw())


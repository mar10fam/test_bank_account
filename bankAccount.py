class BankAccount: 
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def checkBalance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "You have insufficient funds"
        else:
            self.balance -= amount
            return "Withdraw successful"
    
    def transfer(self, amount, toAccount):
        if amount > self.balance:
            return "You have insufficient funds"
        self.balance -= amount
        toAccount.deposit(amount)
        
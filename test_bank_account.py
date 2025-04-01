import pytest

from bankAccount import BankAccount

# Test deposit 
def test_deposit():
    account = BankAccount(0)
    account.deposit(100)
    assert account.checkBalance() == 100

# Test balance check
def test_check_balance():
    account = BankAccount(150)
    assert account.checkBalance() == 150

# Test withdrawal
def test_withdrawal():
    account = BankAccount(50)
    assert account.withdraw(100) == "You have insufficient funds"
    assert account.withdraw(25) == "Withdraw successful"
    assert account.checkBalance() == 25

# Test transfer to another BankAccount
def test_transfer():
    fromAccount = BankAccount(100)
    toAccount = BankAccount(50)
    assert fromAccount.transfer(150, toAccount) == "You have insufficient funds"
    fromAccount.transfer(100, toAccount)
    assert fromAccount.checkBalance() == 0
    assert toAccount.checkBalance() == 150
    
    



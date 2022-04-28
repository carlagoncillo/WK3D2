class BankAccount:
    
    bank_name = "LittleBank"

    def __init__(self, int_rate=0.5, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.sufficient_funds(self.balance,amount):
            self.balance -= amount
            return self
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Account Balance:${self.balance}, Intrest Rate:{self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            print(f"Interst Yielded: ${self.balance*self.int_rate}")
        return self

    @staticmethod
    def sufficient_funds(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

class User:
    
    def __init__(self, fname):
        self.account = BankAccount(int_rate=0.5, balance=0)
        self.fname = fname

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.fname}'s balance is ${self.account.balance}")
        return self

    def make_transfer(self, receiver, amount):
        receiver = receiver
        self.account.balance -= amount
        receiver.account.balance += amount
        print(f"{self.fname} just sent {receiver.fname} ${amount}")
        print(f"{self.fname}'s new balance is ${self.account.balance} and {receiver.fname}'s new balance is ${receiver.account.balance}")
        return self

alex = User("Alex")
anna = User("Anna")
alan = User("Alan")

alex.make_deposit(20).make_deposit(20).make_deposit(10).make_withdraw(5).display_user_balance()
anna.make_deposit(50).make_deposit(50).make_withdraw(20).make_withdraw(10).display_user_balance()
alan.make_deposit(500).make_withdraw(100).make_withdraw(20).make_withdraw(10).display_user_balance().make_transfer(anna, 20)
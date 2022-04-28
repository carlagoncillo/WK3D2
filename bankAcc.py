class BankAccount:
    
    bank_name = "LittleBank"

    def __init__(self, int_rate, balance): 
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

Alex = BankAccount(.05, 3000)
Anna = BankAccount(.05, 2000)
jin = BankAccount(.01, 1) # made this to show insufficient bank acc is not working

Alex.deposit(1000).deposit(2000).deposit(3000).withdraw(500).yield_interest().display_account_info()
Anna.deposit(1000).deposit(2000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()
jin.deposit(1).withdraw(10).display_account_info() # made this to show insufficient bank acc is not working
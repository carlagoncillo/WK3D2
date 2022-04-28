class User:
    
    def __init__(self, fname):
        self.account_balance = 0
        self.fname = fname

    def make_deposit(self, money):
        self.account_balance += money

    def make_withdraw(self, money):
        self.account_balance -= money

    def display_user_balance(self):
        print(self.account_balance)

    def display_account_info(self, receiver, amount):
        receiver = receiver
        self.account_balance -= amount
        receiver.account_balance += amount
        print(self.fname, self.account_balance)
        print(receiver.fname, receiver.account_balance)

alex = User("Alex")
anna = User("Anna")
alan = User("Alan")

alex.make_deposit(20)
alex.make_deposit(20)
alex.make_deposit(10)
alex.make_withdraw(5)

anna.make_deposit(50)
anna.make_deposit(50)
anna.make_withdraw(20)
anna.make_withdraw(10)

alan.make_deposit(500)
alan.make_withdraw(100)
alan.make_withdraw(20)
alan.make_withdraw(10)

print(alex.fname, alex.account_balance)
print(anna.fname, anna.account_balance)
print(alan.fname, alan.account_balance)
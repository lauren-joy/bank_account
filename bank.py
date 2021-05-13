class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("insufficient Funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

account1 =BankAccount(.02,100)
account2 =BankAccount(.05, 2000)

account1.deposit(10).deposit(20).deposit(30).withdraw(15).yield_interest().display_account_info()
account2.deposit(20).withdraw(100).withdraw(500).withdraw(1000).withdraw(500).yield_interest().display_account_info()
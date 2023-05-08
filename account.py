class Account:
    def __init__(self):
        self.name = "Izuchukwu Emmanuel" \
                    ""
        self.account_number = 2266345708
        self.account_balance = 200000

    def deposite(self, amount):
        self.account_balance = self.account_balance + amount
        print(self.account_balance)

    def withdraw(self, amount):
        self.account_balance = self.account_balance - amount
        print(self.account_balance)
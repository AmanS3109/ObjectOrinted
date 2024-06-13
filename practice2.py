class Account:
    def __init__(self, balance, account_no):
        self.account = account_no
        self.balance = balance

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited")
        print("Your balance is:", self.get_final())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited")
        print("Your balance is:", self.get_final())

    def get_final(self):
        return self.balance


acc1 = Account(10000, 45678912)
acc1.debit(1000)
acc1.credit(500)

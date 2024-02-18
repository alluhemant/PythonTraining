class Bank:
    def __init__(self, name, account_no, ifsc_code, balance=0):
        self.name = name
        self.account_no = account_no
        self.ifsc_code = ifsc_code
        self.balance = balance

    def add_amount(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            return f"Enter a valid amount"

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            return f"Withdraw {amount}, New balance: Rs.{self.balance}"
        else:
            return "No sufficient funds"

    def balance_enquiry(self):
        return f"Name:{self.name}\nAccount_no:{self.account_no}\nIFSC_CODE:{self.ifsc_code}\nBalance:{self.balance}"


bank = Bank("Hemant Kumar", "1234", "00000")
bank.add_amount(200)
bank.add_amount(100)
bank.withdraw(100)

print(bank.balance_enquiry())

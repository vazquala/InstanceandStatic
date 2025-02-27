class BankAccount:
    bank_name = "Fred's Bank"
    num_accounts = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.num_accounts += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    @classmethod
    def display_bank_info(cls):
        print(f"Bank Name: {cls.bank_name}, Number of Account: {cls.num_accounts}")


bank_account_1 = BankAccount("Fred", 100)
bank_account_2 = BankAccount("Susie", 200)
bank_account_3 = BankAccount("Billie", 300)
BankAccount.display_bank_info()


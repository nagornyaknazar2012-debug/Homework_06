class BankAccount:
    def __init__(self, owner, balance: int = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Рахунок {self.owner} поповнено на {amount}. Баланс: {self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, *args):
        for account in args:
            self.accounts.append(account)

    def print_accounts(self):
        if self.accounts != []:
            print(f"Bank account {self.name}:")
            for account in self.accounts:
                print(account.owner)
        else:
            print(f"There are no accounts in {self.name}")


acc1 = BankAccount("Назар", 1000)
acc2 = BankAccount("Андрій", 500)

my_bank = Bank("ПриватБанк")

my_bank.add_account(acc1)
my_bank.add_account(acc2)

my_bank.print_accounts()




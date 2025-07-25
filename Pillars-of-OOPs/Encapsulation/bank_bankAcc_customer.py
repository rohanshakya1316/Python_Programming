# A Customer can have multiple bank accounts, but not in the same bank
# A BankAccount is linked to a bank
# A Bank holds only basic information like name and IFSC code

class Bank:
    def __init__(self, name, ifsc_code):
        self.name = name
        self.ifsc_code = ifsc_code

    def __str__(self):
        return f"{self.name} ({self.ifsc_code})"


class BankAccount:
    def __init__(self, account_number, balance, bank: Bank):
        self.account_number = account_number
        self.__balance = balance  # encapsulated
        self.bank = bank

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Acc#: {self.account_number}, Bank: {self.bank.name}, Balance: {self.__balance}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account: BankAccount):
        # Ensure no two accounts are from the same bank
        for acc in self.accounts:
            if acc.bank.ifsc_code == account.bank.ifsc_code:
                print(f"Cannot add another account from bank: {account.bank.name}")
                return
        self.accounts.append(account)

    def show_accounts(self):
        print(f"\n{self.name}'s Accounts:")
        for acc in self.accounts:
            print(f"- {acc}")

    def total_balance(self):
        return sum(acc.get_balance() for acc in self.accounts)
    
# Create banks
bank1 = Bank("Nabil Bank", "NABIL0001")
bank2 = Bank("NIC Asia", "NICASIA0002")
bank3 = Bank("Nabil Bank", "NABIL0001")  # Duplicate for test

# Create accounts
acc1 = BankAccount("1001", 5000, bank1)
acc2 = BankAccount("1002", 3000, bank2)
acc3 = BankAccount("1003", 7000, bank1)  # Same bank as acc1

# Create customer
cust = Customer("Rohan")

cust.add_account(acc1)
cust.add_account(acc2)
cust.add_account(acc3)  # Should not be added

cust.show_accounts()

print("Total balance:", cust.total_balance())
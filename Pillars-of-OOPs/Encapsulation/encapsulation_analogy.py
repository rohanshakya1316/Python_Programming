class BankAccount: 
    def __init__(self, balance):
        self.__balance = balance    # private attribute

    def deposit(self, amount): 
        if amount > 0: 
            self.__balance += amount

    def withdraw(self, amount): 
        if 0 < amount <= self.__balance: 
            self.__balance -= amount
        else: 
            print("Insufficient balance")
    
    def get_balance(self):
        return self.__balance
    
acc = BankAccount(1000)
acc.deposit(5000)
acc.withdraw(2000)
print(acc.get_balance())
# print(acc.__balance)  # Not allowed        
#  Encapsulation
#  Encapsulation means restricting direct access to variables and methods. In Python, we use '_' or
#  '__' before variable names to indicate protected/private access

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = Account("John", 1000)
acc.deposit(500)
print(acc.get_balance())
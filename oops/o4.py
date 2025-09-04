# Encapsulation
# Encapsulation is the practice of bundling the data (attributes) and methods (functions) that operate on the data into a single unit, which is a class. This restricts direct access to some of the object's components to protect the integrity of the data.

# In simple Encapsulation mean protecting the function from accessing and giving the access to spefic function

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())  # Output: 100
account.withdraw(50)
print(account.get_balance())  # Output: 50
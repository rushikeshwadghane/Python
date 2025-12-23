class BankAccount:
    def __init__(self,bal):
        self.__bal = bal   #private variable

    def deposite(self,amount):
        if amount > 0:
            self.__bal += amount

    def get_balance(self):
        return self.__bal



# Using the class
account = BankAccount(1000)   # create account with balance = 1000
account.deposite(500)          # deposit 500
print(account.get_balance())  # get balance -> 1500
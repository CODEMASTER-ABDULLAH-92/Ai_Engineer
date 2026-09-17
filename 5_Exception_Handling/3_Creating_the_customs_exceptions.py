# . Create a custom exception

# You create it by inheriting from Exception:

# class AgeError(Exception):
#     def __init__(self, message):
#         self.message = message

#     def __str__(self):
#         return self.message


# age = int(input("Enter the age: "))

# try:
#     if age < 18:
#         raise AgeError("Age must be 18 or greater")

# except AgeError as err:
#     print(err)
    

class BankException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise BankException("-ve amount")

        if amount > self.balance:
            raise BankException("Low balance")
        
        self.balance -= amount
        print(self.balance)


obj = Bank(1000)

try:
    obj.withdraw(-200)
except BankException as err:
    print(err)
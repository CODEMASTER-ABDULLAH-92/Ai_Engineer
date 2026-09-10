def oop():
    class ATM:
        def __init__(self, pin, balance):
            self.pin = str(pin)  # ✅ Store as string for consistency
            self.balance = balance
        
        def menu(self):
            while True:  # ✅ Use loop instead of recursion
                user_input = input('''
    Hi, how can I help you?
    1. Press 1 to create pin.
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Press 5 to deposit 
    6. Anything else to exit   
    ''')
                
                if user_input == '1':
                    self.create_pin()
                elif user_input == '2':
                    self.change_pin()
                elif user_input == '3':
                    self.check_balance()
                elif user_input == '4':
                    self.withdraw()
                elif user_input == '5':
                    self.deposit()
                else:
                    print("Thank you! Goodbye.")
                    break  # ✅ Exit the loop
        
        def create_pin(self):
            user_pin = input("Enter the new pin: ")
            self.pin = user_pin
            print("Pin created Successfully")
        
        def change_pin(self):
            old_pin = input("Enter the old pin: ")
            if old_pin == self.pin:
                new_pin = input("Enter the new Pin: ")
                self.pin = new_pin
                print("Pin Updated Successfully.")
            else:
                print("Wrong Pin")
        
        def verify_user(self):
            user_pin = input("Enter the pin: ")
            return self.pin == user_pin  # ✅ Simpler return
        
        def check_balance(self):
            if self.verify_user():
                print(f'Current balance is: {self.balance}')
            else:
                print("Verification Error")
        
        def withdraw(self):
            if self.verify_user():
                try:
                    amount = int(input("Enter the amount: "))
                    if 0 < amount <= self.balance:
                        self.balance -= amount
                        print(f"Amount Withdrawn successfully. Your current balance is {self.balance}")
                    else:
                        print("Insufficient Amount or Invalid Amount")
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("Verification Error")
        
        def deposit(self):
            if self.verify_user():
                try:
                    amount = int(input("Enter the amount you want to deposit: "))
                    if amount > 0:
                        self.balance += amount
                        print(f"Amount added successfully. Your current balance is {self.balance}")
                    else:
                        print("Invalid Amount")
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("Verification Error")


    obj = ATM("123", 10000)
    obj.menu()

# oop()

#===============================================
# class diagram of this class 
#===============================================


# ┌──────────────────────────┐
# │           ATM            │
# ├──────────────────────────┤
# │ + pin: str               │
# │ + balance: int           │
# ├──────────────────────────┤
# │ + __init__(pin, balance) │
# │ + menu(): void           │
# │ + create_pin(): void     │
# │ + change_pin(): void     │
# │ + verify_user(): bool    │
# │ + check_balance(): void  │
# │ + withdraw(): void       │
# │ + deposit(): void        │
# └──────────────────────────┘

# Visibility Signs 

# +	Public	
# -	Private	
# #	Protected	
# ~	Package



class Fraction:
    
    # parameterized Constructor.
    def __init__(self, x, y):
        self.x = x
        self.y =y
    
    def __str__(self):
        return f'{self.x}/{self.y}'
    
    def __add__(self, other):
        new_numerator = self.x*other.y + other.x* self.y
        new_den = self.y * other.y
        
        return '{}/{}'.format(new_numerator,new_den)
    
    def __sub__(self, other):
        new_numerator = self.x*other.y - other.x* self.y
        new_den = self.y * other.y
        
        return '{}/{}'.format(new_numerator,new_den)
    
    def __mul__(self, other):
        new_numerator = self.x * other.x
        new_den = self.y * other.y
        
        return '{}/{}'.format(new_numerator,new_den)
        
    def __truediv__(self, other):
        new_numerator = self.x * other.y
        new_den = self.y * other.x
        
        return '{}/{}'.format(new_numerator,new_den)
        

fr1 = Fraction(3,4)
fr2 = Fraction(1,2)
print(fr1 + fr2)
        
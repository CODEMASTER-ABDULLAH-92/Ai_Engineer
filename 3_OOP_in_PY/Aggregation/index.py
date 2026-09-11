# Aggregation means one class uses/contains an object of another class, while that object has an independent lifetime
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)
    
    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)
        
class Address:
    def __init__(self, city, pin, state):
        # self.city = city if i make this private variable we can not access this in the upper class and we need the getter here
        self.__city = city
        self.pin = pin
        self.state = state
    
    def get_city(self):
        return self.__city
    
    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.state = new_state
        self.pin = new_pin
        
add1 = Address('KHU', 94040, 'Punjab')
cust1 = Customer('abdullah', 'male', add1)
cust1.print_address()
cust1.edit_profile('abdullah','ISL', 9999, 'Fed')
cust1.print_address()


#    ┌──────────────┐          ┌──────────────┐
#    │   Customer   │◇────────▶│   Address    │
#    ├──────────────┤  1    1  ├──────────────┤
#    │ - name       │          │ - __city     │
#    │ - gender     │          │ + pin        │
#    │ - address    │          │ + state      │
#    ├──────────────┤          ├──────────────┤
#    │ + print_addr │          │ + get_city   │
#    │ + edit_prof  │          │ + edit_addr  │
#    └──────────────┘          └──────────────┘


                    # ┌─────────────────────────────────────┐
                    # │             Customer                │
                    # ├─────────────────────────────────────┤
                    # │ - name     : str                    │
                    # │ - gender   : str                    │
                    # │ - address  : Address   ◇────────────┼───┐
                    # ├─────────────────────────────────────┤   │
                    # │ + __init__(name, gender, address)   │   │
                    # │ + print_address() : void            │   │
                    # │ + edit_profile(new_name, new_city,  │   │
                    # │                new_pin, new_state)  │   │
                    # └─────────────────────────────────────┘   │
                    #                                           │  Aggregation
                    #                                           │  (◇ hollow diamond)
                    #                                           │  Address has an
                    #                                           │  independent lifetime
                    #                                           ▼
                    # ┌─────────────────────────────────────┐
                    # │             Address                 │
                    # ├─────────────────────────────────────┤
                    # │ - __city : str      (private)       │
                    # │ + pin    : int                      │
                    # │ + state  : str                      │
                    # ├─────────────────────────────────────┤
                    # │ + __init__(city, pin, state)        │
                    # │ + get_city() : str                  │
                    # │ + edit_address(new_city, new_pin,   │
                    # │                new_state) : void    │
                    # └─────────────────────────────────────┘
                    
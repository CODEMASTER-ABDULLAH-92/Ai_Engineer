# ============================================================
# PASSING AN OBJECT TO A FUNCTION
# ============================================================
# Objects are mutable 
class Person:
    def __init__(self, name):
        self.name = name
    

def greet(person):
    print(f'Hey, my name is {person.name}')
    p1 = Person("rajab")
    return p1

p = Person("abdullah")
x = greet(p)
print(x.name)




# Serialization   → Python object → storable data
# Deserialization → storable data → Python object


# Serialization = Pack Python data into JSON.
# Deserialization = Unpack JSON back into Python data.


# A Python object exists in your program's memory. Other systems cannot directly use that Python object. Serialization converts it into a common form that can be stored or transported.

import json

student = {
    "name": "Abdullah",
    "age": 20,
    "skills": ["Python", "React"]
}

# This dictionary is an object in your program's memory (RAM).
# But now we have a problem.

# - Your program runs.
# - Then you close the program.
# - What happens to student?
# - It disappears from memory.

# So, at here we store it  and we could convert it into JSON:
# Python object
#      ↓
# Serialization
#      ↓
# JSON
#      ↓
# student.json
#      ↓
# Hard disk

# The program can close.
# The data remains in the file.

# ===================================
# This is serialization 
# ===================================


with open('demo.json', 'w') as f:
    json.dump(student,f, indent=4)
    

# ===================================
# This is Deserialization 
# ===================================
with open('demo.json', 'r') as f:
    print(json.load(f))
    


# Now working with the tuple 

tup = (1,2,3,4)

with open('demo.json', 'w') as f:
    json.dump(tup, f)

with open('demo.json', 'r') as f:
    print(json.load(f)) # [1,2,3,4,5]
# json.dump() can serialize a tuple, but JSON stores it as an array, and json.load() brings that array back as a Python list—not a tuple.





# Serialization and Deserialization with Custom Objects

import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Muhammad Abdullah", 23)


# Serialization
# Person object -> Dictionary -> JSON

def show_person(person):
    if isinstance(person, Person):
        return {
            "name": person.name,
            "age": person.age
        }

# default means:

# "If JSON doesn't know how to convert this object, use this function to convert it."


# JSON sees Person object
#         ↓
# JSON doesn't know what to do
#         ↓
# Call show_person(person)
#         ↓
# Get a dictionary
#         ↓
# Save dictionary as JSON


with open("demo.json", "w") as f:
    json.dump(person, f, default=show_person, indent=4)


# Deserialization
# JSON -> Dictionary -> Person object

with open("demo.json", "r") as f:
    data = json.load(f)

person = Person(data["name"], data["age"])


print(person.name)
print(person.age)
print(type(person))

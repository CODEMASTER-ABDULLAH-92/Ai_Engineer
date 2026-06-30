# A dictionary is a mutable, unordered (Python 3.6+ maintains insertion order) collection of key-value pairs. Each key maps to a value, allowing fast lookups.

# Examples of dictionaries
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
mixed = {1: "one", "two": 2, (1, 2): "tuple key"}  # Keys can be various types!
nested = {"user": {"name": "Bob", "age": 25}, "active": True}


# ==============================
# Key Characteristics:
# ==============================


# ✅ Key-Value Pairs - Each item has a key and associated value
# ✅ Mutable - Can be changed after creation (add, remove, modify)
# ✅ Dynamic - Can grow or shrink in size
# ✅ Ordered - Maintains insertion order (Python 3.7+)
# ✅ Fast Lookups - O(1) average time complexity for key access
# ✅ Unique Keys - Keys must be unique (values can duplicate)
# ✅ Hashable Keys - Keys must be immutable (strings, numbers, tuples)


# 2. Creating Dictionaries
# Different Ways to Create Dictionaries:

def creating_dict():
    dict1 = {
        "name":"Muhammad Abdullah",
        "age":30
    }
    dict2 = dict(name = "Muhammad Abdullah", age = 23)

    keys = ['name', 'age', 'city']
    values = ['Muhammad Abdullah', 23, 'NYC']
    dict3 = dict(zip(keys, values))

# creating_dict()

# =============================
# 3. Accessing Elements
# =============================

def getting_val():
    person = {"name": "Alice", "age": 30, "city": "New York"}

    # Method 1: Direct access (raises KeyError if key doesn't exist)
    print(person["name"])  # Alice
    # print(person["country"])  # KeyError: 'country'

    # Method 2: get() - Returns None if key doesn't exist (safe)
    print(person.get("name"))     # Alice
    print(person.get("country"))  # None
    print(person.get("country", "USA"))  # USA (default value)

    # Method 3: setdefault() - Returns value, if key missing adds it
    print(person.setdefault("age", 99))     # 30 (existing)
    print(person.setdefault("country", "USA"))  # USA (added)
    print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

    # Method 4: Using in operator (check if key exists)
    if "name" in person:
        print(person["name"])  # Alice

    # Method 5: Using keys(), values(), items()
    print(person.keys())    # dict_keys(['name', 'age', 'city', 'country'])
    print(person.values())  # dict_values(['Alice', 30, 'New York', 'USA'])
    print(person.items())   # dict_items([('name', 'Alice'), ('age', 30), ...])


# getting_val()

# Nested Dictionary Access
def nested_dictionary():
    # Nested dictionary
    users = {
        "alice": {
            "age": 30,
            "city": "New York",
            "hobbies": ["reading", "coding"]
        },
        "bob": {
            "age": 25,
            "city": "Los Angeles",
            "hobbies": ["gaming", "sports"]
        }
    }

    # Access nested values
    print(users["alice"]["city"])  # New York
    print(users["bob"]["hobbies"][0])  # gaming

    # Safe nested access using get()
    print(users.get("alice", {}).get("city", "Unknown"))  # New York
    print(users.get("charlie", {}).get("city", "Unknown"))  # Unknown

    # Using try/except for nested access
    try:
        city = users["charlie"]["city"]
    except KeyError:
        city = "Unknown"
# nested_dictionary()

#==============================
# Modifying Dictionaries
#==============================


# =============================
# Adding/Updating Elements
# =============================

def adding_updating():
    person = {"name": "Alice", "age": 30}

    person["city"] = "New York"
    print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
    # Update existing value
    person["age"] = 31
    print(person)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}
    # Update with multiple key-value pairs
    # Add new key-value pair
    person.update({"job": "Engineer", "salary": 80000})
    print(person)  # {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer', 'salary': 80000}
    # Update from another dictionary

    extra_info = {"department": "IT", "salary": 90000}
    person.update(extra_info)  # salary updated to 90000
    print(person)


    # Using | operator (Python 3.9+)
    person = person | {"country": "USA", "age": 32}

    print(person)

# adding_updating()



# =============================
# Removing Elements:
# =============================

def removing_element():
    person = {"name": "Alice", "age": 30, "city": "New York", "job": "Engineer"}

    age = person.pop("age")
    print(age)       # 30
    print(person)    # {'name': 'Alice', 'city': 'New York', 'job': 'Engineer'}
    # pop() - Remove key and return value
    # pop() with default (no error if key missing)
    country = person.pop("country", "Not Found")
    print(country)   # Not Found
    # popitem() - Remove and return last inserted key-value pair (Python 3.7+)

    last_item = person.popitem()
    print(last_item)  # ('job', 'Engineer')
    print(person)     # {'name': 'Alice', 'city': 'New York'}

    # del - Delete key
    del person["city"]
    print(person)    # {'name': 'Alice'}


    # clear() - Remove all items
    person.clear()
    print(person)    # {}

    # Delete entire dictionary
    # del person

# removing_element()


#. Dictionary Methods
# Complete Method Reference:

def complete_method():
    person = {"name": "Alice", "age": 30, "city": "New York"}

    # get() - Get value with default
    print(person.get("age", 0))        # 30
    print(person.get("country", "N/A")) # N/A

    # keys() - Get all keys
    print(person.keys())  # dict_keys(['name', 'age', 'city'])

    # values() - Get all values
    print(person.values())  # dict_values(['Alice', 30, 'New York'])

    # items() - Get all key-value pairs as tuples
    print(person.items())  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

    # update() - Merge another dictionary
    person.update({"country": "USA", "age": 31})
    print(person)

    # pop() - Remove and return value for key
    age = person.pop("age")
    print(age)  # 31

    # popitem() - Remove and return last item
    item = person.popitem()
    print(item)  # ('country', 'USA')

    # clear() - Remove all items
    person.clear()
    print(person)  # {}

    # copy() - Shallow copy
    original = {"a": 1, "b": 2}
    copy_dict = original.copy()
    print(copy_dict)  # {'a': 1, 'b': 2}

    # fromkeys() - Create dictionary with default values
    new_dict = dict.fromkeys(["x", "y", "z"], 0)
    print(new_dict)  # {'x': 0, 'y': 0, 'z': 0}

    # setdefault() - Get value, set if missing
    person = {"name": "Alice"}
    person.setdefault("age", 30)  # Adds age: 30
    print(person)  # {'name': 'Alice', 'age': 30}
# complete_method()



# Membership Testing

def Membership_testing():
    person = {"name": "Alice", "age": 30, "city": "New York"}

    # Check keys (fast, O(1))
    print("name" in person)       # True
    print("country" in person)    # False
    print("Alice" in person)      # False (checks keys, not values)

    # Check values (slow, O(n))
    print("Alice" in person.values())  # True
    print(30 in person.values())       # True

    # Check key-value pairs
    print(("name", "Alice") in person.items())  # True
    print(("age", 31) in person.items())        # False
# Membership_testing()



# =======================================
# Iteration Over an dictionary
# =======================================

def Iteration_over_dict():
    person = {"name": "Alice", "age": 30, "city": "New York"}

    # Iterate over keys
    for key in person:
        print(key, person[key])

    # Iterate over keys (explicit)
    for key in person.keys():
        print(key)

    # Iterate over values
    for value in person.values():
        print(value)

    # Iterate over key-value pairs
    for key, value in person.items():
        print(f"{key}: {value}")

# Iteration_over_dict()


def merging_dict():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}

    # Method 1: update()
    merged = dict1.copy()
    merged.update(dict2)
    print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Method 2: Using | operator (Python 3.9+)
    merged = dict1 | dict2
    print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Method 3: Using ** unpacking
    merged = {**dict1, **dict2}
    print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Method 4: Using collections.ChainMap
    from collections import ChainMap
    merged = ChainMap(dict1, dict2)
    print(merged)  # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})

# merging_dict()
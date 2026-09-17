# raise in Python

# - raise is a Python keyword used to manually trigger an exception.
# - raise tells Python: "This situation is an error, so raise an exception."

# raise   → CREATE / TRIGGER an exception
# except  → CATCH / HANDLE an exception

try:
    age = 15

    if age < 18:
        raise ValueError("Age must be 18 or above.")

except ValueError as err:
    print(err)
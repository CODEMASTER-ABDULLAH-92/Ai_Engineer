a = 2
def temp():
    global a
    # without the global variable you can't modify the global variable.
    a += 1
    print(a)
temp()

# functional parameters are the local scope 


# LEGB Rule — Summary

# Python stops searching as soon as it finds the name.

# Local → Enclosing → Global → Built-in
# Found in Local → ❌ No search in Enclosing, Global, or Built-in.
# Found in Enclosing → ❌ No search in Global or Built-in.
# Found in Global → ❌ No search in Built-in.
# Not found anywhere → ❌ NameError

# Key point:
# LEGB searches from left to right and stops at the first match.
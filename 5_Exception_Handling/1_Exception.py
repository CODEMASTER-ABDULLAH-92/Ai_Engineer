# Exception handling means handling errors that happen while your program is running, so the program can respond properly instead of suddenly crashing.

"""
try
--> Write the code here that may cause an exception,
    such as risky operations, reading a file, using another
    module/library, user input, database operations, etc.

except
--> Handles the exception that occurs in the try block.

else
--> Runs only when the try block executes successfully
    without any exception.

finally
--> Runs in every situation, whether an exception occurs
    or not. It is commonly used for cleanup operations.
"""



        #          ┌─────────┐
        #          │   TRY   │
        #          └────┬────┘
        #               ↓
        #          ◇─────────◇
        #         ╱           ╲
        #        ╱             ╲
        #       ↓               ↓
        # ┌───────────┐   ┌───────────┐
        # │ EXCEPTION │   │    ELSE   │
        # │ (if try fail)  (if Try PASS)
        # └─────┬─────┘   └─────┬─────┘
        #       │               │
        #       └───────┬───────┘
        #               ↓
        #          ┌─────────┐
        #          │ FINALLY │
        #          └────┬────┘
        #               ↓
        #          ┌─────────┐
        #          │ CLEANUP │
        #          └─────────┘
def exception():

    try:
        f = open('demo.txt','w')
        f.write('Hello, my name is abdullah.\nI am studying in Software Engineering.')
    except FileNotFoundError:
        print('file not error.')
    finally:
        f.close()

# exception()

def exception():
    try:
        connection = connect_to_db()
        data = connection.execute("select * from users")
    
    except Exception as e:
        print(e)
    finally:
        connection.close()

# exception()

def exception():
    try:
        bluetooth.connect(device)

    except ConnectionError:
        print("Bluetooth connection failed.")

    finally:
        bluetooth.disconnect()


# exception()


try:
    with open('demo1.txt', 'r') as f:
        s = f.read()
        print(s)    
except Exception as e:
    print(e)


# catching the specific errors 
try:
    # The with block automatically closes the file when you leave it.
    with open('demo.txt', 'r') as f:
        s = f.read()
except Exception as e:
    print(e.with_traceback)
else:
    print(s)
    


try:
    m = 5
    with open('demo.txt', 'r') as f:
        print(f.read())
        print(m)
        print(5/12)
        l = [1,2,3]
        l[100]
except FileNotFoundError:
    print("File Not found")
except NameError:
    print("Variable Not found")
except ZeroDivisionError:
    print('can not divide by zero')

# this is correct don't handle the generic exceptions  at the top 
except Exception as err:
    print(err)
    
    
    

Crea
#The Simple principle is that 

# Open a file 
# Read/write data 
# close the file 

def file():
    f = open('4_File-Handling/sample.txt', 'w')
    f.write("Hello,\nMy name is abdullah.")
    f.close()

    # You got an error because we closed the file and this is not possible 
    f.write("I'm software Engineer.")

# file()

# Write Multiple lines 
# So, the file is already exist this action override the existing data.

def file():
    f = open('4_File-Handling/sample.txt', 'w')
    f.write('My name is abdullah.')
    f.write('I am Software Engineer.')
    f.close()

# file()

# a mode ===> is the append mode, it does not overrides the data it adds the new data at the end of the existing data.

def file():
    f = open('4_File-Handling/sample.txt', 'a')
    f.write('\nI Studied in 7th Semester.')
    f.close()

# file()


# =================================================================

# If you wants to write many lines then do this 

# =================================================================

def file():
    l = ['Hello,','I ','am ','software ','Engineer.']
    f = open('4_File-Handling/sample.txt','w')
    f.writelines(l)
    f.close()
# file()


# =======================================================

# Now its time to read the file 

# =======================================================

# read() ->  This read the complete passage from the file 
#readline() -> This reads only the line by line data from the 

def file():
    f = open('4_File-Handling/sample.txt', 'r')
    s = f.read()
    print(s)
    f.close()
# file()

def file():
    f = open('4_File-Handling/sample.txt', 'r')
    s = f.read(10)
    print(s)
    f.close()
# file()


# =================
# ReadLines 
# =================


def file():
    f = open('4_File-Handling/sample.txt', 'r')
    s = f.readline()
    print(s)
    f.close()

# file()


# Load the entire file 

def file():
    f = open('4_File-Handling/sample.txt', 'r')
    
    while True:
        data = f.readline()
        if data == '':
            break
        else:
            print(data, end='')
    f.close()

# file()



# Why do we close it?
# 1. It releases system resources
    # --> When Python opens a file, the operating system keeps track of that open file.
# 2. It allows other programs to use the file. (Security)

# ===================================
# context manager
# ===================================

# A context manager in Python is a mechanism that automatically manages a resource for you — such as opening and closing a file.

# The most common way you use a context manager is with the with statement.

def file():
    
    with open('4_File-Handling/sample.txt', 'w') as f:
        f.write('My name is abdullah.\n and whats your name.')
        

    with open('4_File-Handling/sample.txt', 'r') as f:
        f.read()

# file()



# To Load a big file in memory 

def big_data():
    big_data = ['hello world\n' for i in range(1000)]

    with open('4_File-Handling/sample.txt', 'w') as f:
        # This doesn't work because write() expects one string, not a list. 
    #     write()     → expects ONE string
    #     writelines() → accepts MULTIPLE strings

        f.writelines(big_data)
        
        
    with open('4_File-Handling/sample.txt', 'r') as f:
        chunk_size = 100
        
        while True:
            
            chunk = f.read(chunk_size)
            
            if len(chunk) == 0:
                break
            
            print(chunk, end='---')

# big_data()

# tell() → current file position
# seek() → change file position

data = ['Hello world\n' for i in range(10)]
with open('4_File-Handling/sample.txt', 'w') as f:
    f.writelines(data)
    

# ========================================
# Tell and Seek function 
# ========================================


# Open the file in read mode
with open("4_File-Handling/sample.txt", "r") as f:

    # tell() → tells the current position of the file pointer
    # At the beginning, the position is 0
    print(f.tell())

    # read(10) → reads the next 10 characters
    # After reading, the file pointer moves forward by 10
    print(f.read(10))

    # tell() → shows the new current position
    # Normally it will be 10 after reading 10 characters
    print(f.tell())

    # seek(0) → moves the file pointer back to position 0
    # 0 means the beginning of the file
    f.seek(0)

    # read(10) → reads the same first 10 characters again
    print(f.read(10))

    # tell() → shows the current position again
    # Normally it will be 10
    print(f.tell())
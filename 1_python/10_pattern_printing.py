#  First Pattern 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

def pattern():

    for i in range(0,5):
        for j in range(0,5):
            print("*",end=" ")
        print()

# pattern()


# ===========================
# Pattern 2 
# ===========================

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

def pattern():

    for i in range(0,5):
        for j in range(i+1):
            print("*", end=" ")
        print()

# pattern()





# ===========================
# Pattern 3
# ===========================


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

def pattern():

    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

# pattern()




# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

def pattern():
    for i in range(1,6):
        for j in range(1,i + 1):
            print(i, end=" ")
        print()

# pattern()



# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

def pattern():
    for i in range(5,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()

# pattern();



# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 


def pattern():
    for i in range(6,1,-1): # row 
        for j in range(1, i): # col
            print(j, end=" ")
        print()

# pattern()
# The text mode is not working binary files like images 

# "r"  → read text
# "rb" → read binary


# "w"  → write text
# "wb" → write binary


with open('4_File-Handling/my_img.jpeg', 'rb') as f:
    
    data = f.read()
    
    print(data)
    print(len(data))
    print(type(data))


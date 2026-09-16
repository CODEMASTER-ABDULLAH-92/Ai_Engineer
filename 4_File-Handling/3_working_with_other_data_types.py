
with open('4_File-Handling/sample.txt', 'w') as f:
    # We got this error:
    # TypeError: write() argument must be str, not int
    # f.write(5)
    
    f.write('5')

with open('4_File-Handling/sample.txt','r') as f:
    data = f.read()
    print(data)
    print(type(data)) #<class 'str'>
    
with open('4_File-Handling/sample.txt', 'r') as f:
    # print(f.read() + 5) # TypeError: can only concatenate str (not "int") to str
    print(int(f.read()) + 5) # Correct ==> 10
    
d = {
    'name':'Abdullah',
    'age':23,
    'marks':[10,12,14,15]
}

with open('4_File-Handling/sample.txt','w') as f:
    f.write(str(d))
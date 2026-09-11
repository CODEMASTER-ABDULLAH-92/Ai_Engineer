class person:
    def __init__(self, name):
        self.name = name
    

p1 = person('abdullah')
p2 = person('rajab')
p3 = person('afaq')

# L = [p1,p2,p3]

# for i in L:
#     print(i.name)


d = {'p1':p1, 'p2':p2, 'p3':p3}

for i in d:
    print(d[i].name)
str = input("Enter a string: ")
l = str.split()
print(l)
print()
d = {}
for i in set(l):#duplicate elements r removed in set data type
    d[i] = len(i)
print(d)

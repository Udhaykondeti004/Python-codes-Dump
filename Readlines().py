sfile = input("Enter a file to open: ")
f1 = open(sfile,"r")
data = f1.readline()
print(data)
print(type(data))
print()
data = f1.readlines()
print(data)
print()
print(type(data))
sfile = input("Enter a file name: ")
f1 = open(sfile,"r")
data = f1.read().lower()
d = {}
for i in data:
    if i in d:
        d[i]= d[i]+1
    else:
        d[i] = 1
print(d)
f1.close


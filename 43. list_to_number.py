list = eval(input("Enter a list: "))
res = ""
ls = [str(i) for i in list]
for s in ls:
    res = res+s
print("Number created with list elements is",int(res))

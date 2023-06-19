def power(n,p):
    if p==0:
        return 1
    else:
        return n*power(n,p-1)

n = int(input("Enter number: "))
p = int(input("Enter Power: "))
result = power(n,p)
print("{} power of {} is {}".format(n,p,result))

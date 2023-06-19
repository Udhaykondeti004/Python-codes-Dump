def table(n,m):
    for i in range(n,n+1):
        for j in range(1,m+1):
            print("{} * {} = {}".format(n,j,n*j))

num = int(input("Enter any number: "))
mul = int(input("Enter any number: "))
table(num,mul)

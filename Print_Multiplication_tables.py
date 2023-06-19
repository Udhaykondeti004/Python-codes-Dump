def table(n,m):
    for i in range(1,n+1):
        print("Multiplication table of {} is".format(i))
        for j in range(1,m+1):
            print("{} * {} = {}".format(i,j,i*j))
        print()

num = int(input("Enter any number: "))
mul = int(input("Enter any number: "))
table(num,mul)

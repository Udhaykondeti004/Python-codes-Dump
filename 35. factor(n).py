def factor(n):
    count = 0
    for i in range(1,n+1):
        if (n%i)==0:
            print(i)
            count = count+1

    if count==2:
        print("It is a prime number")
    else:
        print("Not a prime number")

num = int(input("Enter a number: "))
(factor(num))

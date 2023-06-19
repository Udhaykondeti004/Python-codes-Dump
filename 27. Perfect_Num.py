def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum = sum+i
    print(sum)
    if(sum == n):
        print("It is a perfect number")
    else:
        print("It is not a perfect number")

n = int(input("Enter a number: "))
perfect(n)
            

def series(n):
    if n==1:
        return n
    else:
        return (n**5) + series(n-1)

n = int(input("Enter a number: "))
if n==1:
    print("The sum of the series is: ",series(n))
elif n>1:
    print("The sum of the series is: ",series(n))
else:
    print("Invalid Number")
    

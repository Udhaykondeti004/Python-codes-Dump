def number(n):
    if (n>0):
        n = n//10
        return 1+number(n)
    else:
        return 0

num = int(input("Enter a number: "))
result = number(num)
print("Sum of digits are",result)

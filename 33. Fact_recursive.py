
def fact(n):
    if n == 1:
       return n
    else:
       return n*fact(n-1)

num = int(input("ENter a number: "))

print("The factorial of", num, "is",fact(num))

def factorial(x):
    fact = 1
    for i in range (1,num+1):
        fact = fact*i
    return fact
num = int(input("Enter any number\n"))
z = factorial(num)
print("Factorial of {} is {}".format(num,z))
print("Factorial of",num,"is",z)


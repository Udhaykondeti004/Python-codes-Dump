first,second = 0,1
n =int(input("Enter a number: "))
print("Fibonacci series of",n," elements is")
print(first,second,end = " ")
for i in range(n-2):
    result = first+second
    print(result,end = " ")
    first = second
    second = result
    

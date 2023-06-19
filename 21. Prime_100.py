n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
for i in range(n+1,m):
    for j in range(2, i):
           if (i % j) == 0:
               break
    else:
        print(i)  

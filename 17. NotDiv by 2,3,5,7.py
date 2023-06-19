count = 0
for i in range(1,1001):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0:
        count = count+1
        print(i,end =" ")
print()
print("Total numbers are",count)

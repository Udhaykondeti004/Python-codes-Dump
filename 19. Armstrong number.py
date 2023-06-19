num = int(input("Enter a number"))
sum = 0
temp = num
while num>0:
    d = num%10
    sum = sum+d**3
    num = num//10
if sum==temp:
    print("The number is armstrong number")
else:
    print("Not a armstrong number")

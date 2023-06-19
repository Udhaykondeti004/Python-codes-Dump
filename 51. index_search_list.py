l = eval(input("Enter a list: "))
e = int(input("Enter element to search "))
print("Element present at indexes ")
count = 0
for i in range(len(l)):
    if l[i]==e:
        print(i)
        count+=1
print(f"Element repeated {count} times in a list")
    

n = list(range(1,11))
print("Before:",n)
for i in n:
    if i%2!=0:
        n.remove(i)
print("After deleting odd numbers",n)
print()

#Using List Comprehension
l = [i for i in range(1,11)]
print("Before:",l)
m = [i for i in l if i%2==0]
print("After deleting odd numbers:",m)

l = eval(input("Enter a list: "))
l.append("srmap")
print(l)
l.insert(1,888)
print(l)
data = list(range(1,10))
print(data)
l.extend(data)
print(l)
del l[2]
print(l)
l.remove(4)
print(l)
print(l.pop(1))
l.clear()
print(l)
a = [10,20,30]
b = [1,2,3]
print(a+b)
result = b*3
print(result)
c = [1,2,3,4]
d = c[:]
d[1]=15
print(c)
print(d)

l1 = []
n = int(input("Enter number of elements: "))
for i in range(n):
    l1.append(int(input("Enter the element: ")))
print("List: ",l1)


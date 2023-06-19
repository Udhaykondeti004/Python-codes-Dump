def swap(n):
    str1 = str(n)
    l = [i for i in str1]
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    str2 = "".join(l)
    return int(str2)
n = int(input("Enter the number: "))
result = swap(n)
print(result)

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

ul = eval(input("Enter unsorted list: "))
print("The unsorted list is:",ul)
sl = bubble_sort(ul)
print("The sorted list is:",sl)

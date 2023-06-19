def lsearch(list1,key):
    for i in range(len(list1)):
        if key==list1[i]:
            print("Key element is fount at index:",i)
            break
        else:
            print("Element is not found")

list1 = eval(input("Enter a list: "))
key = int(input("Enter element to search: "))
lsearch(list1,key)

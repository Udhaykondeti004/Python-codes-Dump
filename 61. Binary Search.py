def bsearch(list1,key):
    low = 0
    high = len(list1)-1
    found = False
    while low<=high and not found:
        mid = (low+high)//2
        if key==list1[mid]:
            found = True
        elif key>list1[mid]:
            low = mid+1
        else:
            high = mid-1
    if found == True:
        print("Key is found")
    else:
        print("Key is not found")
list1 = eval(input("Enter a list: "))
key = int(input("Enter element to search: "))
bsearch(list1,key)

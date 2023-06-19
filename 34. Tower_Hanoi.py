def tower_hanoi(n,s,d,m):
    if(n<1):
        print("Invalid")
    elif n==1:
        print("Move disk {} from {} to {}".format(n,s,d))
    else:
        tower_hanoi(n-1,s,m,d)
        print("Move disk {} from {} to {}".format(n,s,d))
        tower_hanoi(n-1,m,d,s)
        
n = int(input("Enter number of discs: "))
tower_hanoi(n,'a','c','b')

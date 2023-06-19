a = int(input("Enter x1: "))
b = int(input("Enter x2: "))
c = int(input("Enter y1: "))
d = int(input("Enter y2: "))

distance = (((b-a)**2)+((d-c)**2))**0.5
print("Distance between (%d,%d) and (%d,%d)is %.2f"%(a,b,c,d,distance))

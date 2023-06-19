a = int(input(" Enter coefficient of x² "))
b = int(input(" Enter coefficient of x "))
c = int(input(" Enter Constant"))
disc = (b**2) - (4*a*c)
root1 = (-b + (disc)**0.5)/2*a
root2 = (-b - (disc)**0.5)/2*a
if(disc>0):
    print("Roots are Real and Distinct")
elif(disc == 0):
    print("Roots are Real and equal")
elif(disc<0):
    print("Roots are imaginary")
else:
    print("Invalid")
print("Roots of the equation are {} and {}".format(root1,root2))


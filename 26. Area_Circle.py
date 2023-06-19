def circle(x):
    a = 3.14*(x**2)
    return a

r = eval(input("Enter the radius: "))
result = circle(r)
print("Area of the cirle is %.3f square units"%(result))

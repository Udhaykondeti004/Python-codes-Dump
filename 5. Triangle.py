print("Enter the three angles of triangle respectively")
a = float(input("A ="))
b = float(input("B ="))
c = float(input("C ="))
sum = a+b+c
if(sum ==180) and (a!=0 and b!=0 and c!=0)and (a<90 and b<90 and c<90):
    print("Sum of the angles in the triangle is",sum, "degrees")
    print("The triangle is valid and it is Acute angled triangle")
elif(sum == 180) and (a!=0 and b!=0 and c!=0)and (a==90 or b==90 or c==90):
    print("Sum of the angles in the triangle is",sum, "degrees")
    print("The triangle is valid and it is Right angled triangle")
elif(sum == 180) and (a!=0 and b!=0 and c!=0)and (a>90 or b>90 or c>90):
    print("Sum of the angles in the triangle is",sum, "degrees")
    print("The triangle is valid and it is Obtuse angled triangle")
else:
     print("Sum of the angles in the triangle is",sum, "degrees")
     print("Hence the triangle is INVALID")
    
    

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))

if (num1 >= num2) and (num1 >= num3):
   print("{} is the greatest".format(num1))
elif (num2 >= num1) and (num2 >= num3):
   print("{} is the greatest".format(num2))
else:
   print("{} is the greatest".format(num3))


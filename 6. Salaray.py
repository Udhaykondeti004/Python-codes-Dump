basic = float(input("Enter Basic salary: "))
if(basic<=10000):
    hra = basic*(20/100)
    da = basic*(80/100)
    gross = basic + hra + da
    print("Gross salary of employee is",gross)
elif(basic<=20000):
    hra = basic*(25/100)
    da = basic*(90/100)
    gross = basic + hra + da
    print("Gross salary of employee is",gross)
elif(basic>20000):
    hra = basic*(30/100)
    da = basic*(95/100)
    gross = basic + hra + da
    print("Gross salary of employee is",gross)
else:
    print("Invalid Salary Number")


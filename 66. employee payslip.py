class EMP:
    def __init__(self,ids,name,sal):
        self.ids = ids
        self.name = name
        self.sal = sal
    def payslip(self):
        print("---------EMPLOYEE PAY SLIP-----------")
        print("EMP ID:",self.ids)
        print("EMP NAME:",self.name)
        print("EMP BASIC:",self.sal)
        HRA = (self.sal*18)/100
        TAX = (self.sal*5)/100
        DA = (self.sal*10)/100
        print("EMP HRA:",HRA)
        print("EMP DA:",DA)
        print("EMP TAX:",TAX)
        gross = self.sal + HRA + DA
        print("EMP GROSS SAL:",gross)
        print("EMP NET SAL:",gross-((gross*10)/100))
e1 = EMP("AP21110011381","Udhay",1200)
e1.payslip()

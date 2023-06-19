class P:
    def __init__(self):
        self.name = "Rahul"
        self.roll = 501
    def m1(self):
        print("Name:",self.name)
        print("Roll No:",self.roll)
class C(P):
    def m2(self):
        print("This is child class method")

class C2(P):
    def m2(self):
        print("This is hierarchial inheritance")
class S(C):
    def m3(self):
        print("Multi Level Inheritance")
class M(C2,C):
    def m4(self):
        print("Multiple Inheritance")
        
s = S()
s.m1()
s.m2()
s.m3()

c = M()
c.m2()
c.m4()

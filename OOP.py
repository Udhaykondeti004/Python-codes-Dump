class Student:
    '''This is my fist class'''
    def __init__(self):#constructor
        print("Constructor Executed")
        self.name = "Rahul"
        self.roll = 501
        self.college="SRM AP"
    def info(self):       #method
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("College:",self.college)
print(Student.__doc__)
s = Student() #Object Creation
s.info()

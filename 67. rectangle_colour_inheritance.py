class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
class Colour_rect(Rectangle):
    def __init__(self,length,breadth,colour):
        super().__init__(length,breadth)
        self.colour = colour
    def area(self):
        a = self.length*self.breadth
        return a
    
n = int(input("Enter number of rectangles: "))
d = {}
for i in range(1,n+1):
    print("RECTANGLE:",i)
    l = int(input("Enter Length: "))
    b = int(input("Enter Breadth: "))
    c = input("Enter Colour: ")
    r = Colour_rect(l,b,c)
    d[r.area()]=c
print("Colour of rectangle having minimum area:",d[min(d.keys())])

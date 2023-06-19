class A:
    def calc(self,l,b,h):
        vol = float(l)*float(b)*float(h)
        return vol
l = input("Enter Length: ")
b = input("Enter Breadth: ")
h = input("Enter Height: ")

r = A()
vol = r.calc(l,b,h)
print(vol)

class Rectangle():
    def Area(self,l,b):
        print(l*b)
    def Perimeter(self,l,b):
        print(2*(l+b))
l=int(input("Enter Length= "))
b=int(input("Enter Breadth= "))
rec=Rectangle()
rec.Perimeter(l,b)
rec.Area(l,b)

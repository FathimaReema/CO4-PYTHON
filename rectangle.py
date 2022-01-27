class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def perimeter(self):
        return (2*(self.length+self.breadth))
r1=Rectangle(4,5)
r2=Rectangle(5,7)
a1=r1.area()
a2=r2.area()
p1=r1.perimeter()
p2=r2.perimeter()
print("The area of rectangle 1:",a1)
print("The perimeter of rectangle1:",p1)
print("The area of rectangle2:", a2)
print("The perimeter of rectangle2:", p2)
if(a1>a2):
    print("Rectangle 1 is bigger")
else:
    print("Rectangle 2 is bigger")

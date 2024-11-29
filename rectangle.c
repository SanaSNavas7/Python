class Rectangle:
    def __init__(self):
        self.length=int(input("Enter length of rectangle: "))
        self.breadth=int(input("Enter breadth of rectangle: "))
    def area(self):
        area=self.length*self.breadth
        print("area  is ",area)
        return area
    def perimeter(self):
        perimeter=2*(self.length+self.breadth)
        print("Perimeter is ",perimeter)
        return perimeter
c1=Rectangle()
c1.area()
c1.perimeter()  


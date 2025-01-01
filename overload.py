class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def area(self):
        return self.__length* self.__breadth
    def __lt__(self,rect2):
        return self.area() < rect2.area()
r1=Rectangle(40,5)
r1_area=r1.area()

r2=Rectangle(4,7)
r2_area=r2.area()

print("Area of first rectangle is :",r1_area)
print("Area of second rectangle is :",r2_area)

if(r1<r2):
    print("Area of rectangle 1 is less than rectangle 2")
else:
     print("Area of rectangle 2 is less than rectangle 1")





    
 









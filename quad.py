import cmath
import math
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=b**2-4*a*c
if(d<0):
    r1=(-b-cmath.sqrt(d))/2*a
    r2=(-b+cmath.sqrt(d))/2*a
    print(f"Roots are {r1} and {r2}")  
elif(d>0):
    r1=(-b-math.sqrt(d))/2*a
    r2=(-b+math.sqrt(d))/2*a
    print(f"Roots are {r1} and {r2}")   
else:
    r=-b/2*a
    print(f" Root of the quadratic equation is {r}")

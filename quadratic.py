import cmath
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=b**2-4*a*c
r1=(-b-cmath.sqrt(d))/2*a
r2=(-b+cmath.sqrt(d))/2*a
print("Roots of the quadratic equation are : ",r1,r2)

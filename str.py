def swap(a,b):
    return a[0]+b[1]+a[2:]+" "+b[0]+a[1]+b[2:]
a=input("enter string 1")
b=input("enter string 2")
s=swap(a,b)
print(s)

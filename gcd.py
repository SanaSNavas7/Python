def gcd(a,b):
    if(b==0):
        print("gcd is ",a)
    else:
        return gcd(b,a%b)
s1=int(input("enter a "))
s2=int(input("enter b "))
gcd(s1,s2)


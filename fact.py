
def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact
num=int(input("enter number"))
fact1=factorial(num)
print("factorial is ",fact1)
    

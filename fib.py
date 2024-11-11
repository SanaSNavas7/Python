def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end='')
        a,b=b,a+b
num=int(input("enter no of terms   : "))
fib(num)

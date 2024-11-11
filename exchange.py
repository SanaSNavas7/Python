def exchange(a):
    if(len(a)<2):
        return a
    else:
        return a[-1]+a[1:-1]+a[0]
string=input("enter the string: ")
result=exchange(string)
print("String after exchanging first and last characters :",result)

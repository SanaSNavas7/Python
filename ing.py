s=input("enter string : ")
if  s[-3:]=='ing':
    s+='ly'
else:
    s+='ing'
print("new string is" ,s)

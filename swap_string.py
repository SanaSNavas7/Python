def swap(a,b):
    if(len(a)<2) or (len(b)<2):
        printf("Give atleast two characters")
    else:
        return b[0]+a[1:]+" "+a[0]+b[1:]

s1=input("Enter a string 1: ")
s2=input("Enter a string 2: ")
result=swap(s1,s2)
print(f" Strings after swapping {s1} and {s2}  is ",result)

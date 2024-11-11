a=input("Enter a string 1: ")
b=input("Enter a string 2: ")
if(len(a)<2) or (len(b)<2):
    printf("Give atleast two characters")

else:
    result=b[0]+a[1:]+" "+a[0]+b[1:]
    print(f" Strings after swapping {a} and {b}  is ",result)
        


string=input("enter string")
letter=input("enter letter to search")
count=0
for i in string:
    
    if letter==i:
        count+=1
    
print("count is ",count)

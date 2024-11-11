def exchange(s):
    if(len(s)<2):
        print("Give atleast two characters")
    else:
          print(s[-1]+s[1:-1]+s[0])
        
  
s=input("enter string ")
a=exchange(s)


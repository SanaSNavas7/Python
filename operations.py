num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
op=input("Enter the operation to perform  \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n")
if(op=='1'):
    sum=num1+num2
    print("Sum is ",sum)
elif(op=='2'):
    diff=num1-num2
    print("Difference is ",diff)
elif(op=='3'):
    mul=num1*num2
    print("Product is ",mul)
elif(op=='4'):
    if(num2==0):
        print("Cannot divide by zero")
    else:
        div=num1/num2
        print("Quotient is ",div)
else:
    print("Invalid option")
    



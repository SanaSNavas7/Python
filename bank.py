class Bank:
    def __init__(self,account_no,name,type_of,balance):
        self.account_no=account_no
        self.name=name
        self.type_of=type_of
        self.balance=balance
    def deposit(self):
        amount=int(input("enter the amount"))
        self.balance+=amount
        print("New balance is ",self.balance)
        return self.balance
        
    def withdraw(self):
        s=int(input("enter the amount to withdraw"))
        self.balance-=s
        print("New balance is ",self.balance)
        return self.balance
        
c=Bank("John","12345","Savings",500)
a=c.deposit(200)
b=c.withdraw(100) 
print("balance after depositing",a)
print("balance after withdrawing",b)


    
        
    
                   
        


    
                   
        


    

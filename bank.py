class Bank:
<<<<<<< HEAD
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


    
        
    
                   
        


    
                   
        


    
=======
    def __init__(self, accno, name, typ, balance):
        self.accno = accno
        self.name = name
        self.typ = typ
        self.balance = balance

    def deposit(self):
        amnt = int(input("Enter the amount to deposit: "))
        self.balance += amnt
        print("Deposit Successful!")
        print("Your current status is:")
        print(f"Account No: {self.accno}")
        print(f"Name:       {self.name}")
        print(f"Account Type: {self.typ}")
        print(f"New Balance: Rs.{self.balance}")

    def withdraw(self):
        amnt = int(input("Enter the amount to withdraw: "))
        if amnt > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amnt
            print("Withdrawal Successful!")
        print("Your current status is:")
        print(f"Account No: {self.accno}")
        print(f"Name:       {self.name}")
        print(f"Account Type: {self.typ}")
        print(f"New Balance: Rs.{self.balance}")


accno = int(input("Enter the account number: "))
name = input("Enter the name: ")
typ = input("What is your account type? (Savings/Current): ")
balance = int(input("Enter your current account balance: "))
acc = Bank(accno, name, typ, balance)

while True:
    print("\nWhat would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        acc.deposit()
    elif choice == 2:
        acc.withdraw()
    elif choice == 3:
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid entry. Please try again.")
>>>>>>> f366a45b1a9d1f1b005f1d0ef79b046175a598e8

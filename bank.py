class Bank:
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

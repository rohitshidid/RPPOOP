from curses import pair_number
from optparse import AmbiguousOptionError
from unittest import case


class Bank_account:
    def __init__ (self,name,acc_no,type,bal):
        self.name = name
        self.acc_no = acc_no
        self.type = type
        self.bal = bal
    
    def deposit(self, amount):
        self.bal = self.bal+amount

    def check_bal(self):
        print("Balance is "+self.bal)

    def withdraw(self, amount):
        if self.bal < amount:
            print("You Do not have enough funds")
        else:
            self.bal= self.bal-amount
            print("Withdrawal Sucessfully Completed")

    
p1 = Bank_account("rohit",142103012,"Saving",100000)
while True:
    print("1) Deposit \n2) Withdraw \n3)Check Bal \n4)Exit")
    choice= int (input("Enter your choice: "))
       
    if choice ==1:
        amt =int(input("Enter your amount"))
        p1.deposit(amt)
    elif choice == 2:
        amt = int(input("\nEnter the amount"))
        p1.withdraw(amt)
    elif choice == 3:
        print("\nBalance is : ")
        print(p1.bal)
    elif choice == 4:
        exit(0)
    else:
        print("Wrong input choice")

        

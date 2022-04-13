from curses import pair_number
from dataclasses import dataclass
from optparse import AmbiguousOptionError
from turtle import goto
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


initial_amount=10000
user_found = 0
bank_data={}
while(1):
    print("Welcome to Python Bank")


    print("\n1 Create account")
    print("\n2 Login")
    print("\n3 Exit")

    fchoice=int(input("Enter your Choice"))

    if(fchoice == 1):
        fname = input("Enter your name: ")
        fid = int(input("Enter your ID: "))
        bank_data[fname] = fid
    elif(fchoice == 2):
        name = input("Enter your name ")
        id = int(input("Enter your Bank ID "))
        for x in bank_data:
            if(name == x and id == bank_data[x]):
                user_found=1

        if(user_found):
            p1 = Bank_account(name,id,"Saving",initial_amount)
            user_found = 1
            print("\nLogin Sucessfull\n\n")
            print("Login Details: \nName:{0} \nAccount id: {1} \n".format(name,id))
        else:
            print("User not found") 

        while (user_found):
            print("1) Deposit \n2) Withdraw \n3)Check Bal \n4)Exit")
            choice= int (input("Enter your choice: "))
            
            if choice ==1:
                amt =int(input("Enter your amount "))
                p1.deposit(amt)
            elif choice == 2:
                amt = int(input("\nEnter the amount "))
                p1.withdraw(amt)
            elif choice == 3:
                print("\nBalance is : ")
                print(p1.bal)
            elif choice == 4:
                break
            else:
                print("Wrong input choice")
    elif(fchoice == 3):
        break
print("Thank you for using Python Bank \nSee you again!!!\n")
            

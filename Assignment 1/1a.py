class animal:
    print("hello")


while(1):
    print("Welcome to animal detector: \n1) Enter the detector\n2) Exit \n")
    choice = int(input("Enter your choice "))
    if(choice == 1):
        print("choice 1")
    if(choice == 2):
        break
    else: 
        print("Invalid Input")

print("Thanks for using Animal detector")
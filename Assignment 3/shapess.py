from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self):
        print("============== Welcome to Area Finder ============== ") 
        self.S1 = None
        self.S2 = None
    def get_details(self):
        self.S1 = int(input("Enter first dimension: "))
        self.S2 =int(input("Enter second dimension:  "))
        
    def area_rect(self):
        if(self.S1 and self.S2):
            self.val = self.S1*self.S2
            print("Area of rectangle is : {0}".format(self.val))
        else:
            print("Enter Values first.....")

    def area_tri(self):
        if(self.S1 and self.S2):
            self.val = (self.S1*self.S2)/2
            print("Area of triangle is: {0}".format(self.val))
        else:
            print("Enter Values first.....")
    def show_val(self):
        print("\nThe Values are {0} and {1} ".format(self.S1 , self.S2))

begin = input("Press any key to initiate...... \n")
p1 = Polygon()

while(1):
    cho=int(input("\n\n============== Main Menu ============== \n1) Enter Details \n2) Calculate Area\n3) Show current values\n4) Exit \nYour Choice: "))
    if(cho == 1):
        p1.get_details()
    elif(cho== 2 ):
        
        while(1):
            cho1 = int(input("\n\n============== Select the Polygon ============== \n1) Rectangle \n2) Triangle \n3) Back \nYour Choice: "))
            if(cho1 == 1):
                p1.area_rect()
            elif(cho1 ==2):
                p1.area_tri()
            elif(cho1==3):
                break
            else:
                print("Enter a valid choice ")
    elif(cho == 3):
        p1.show_val()
    elif(cho == 4):
        exit(0)
    else:
        print("Enter a valid choice ")

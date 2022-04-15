

import imp
from secrets import choice

animals_data={"Dog":"Bark","Cat":"Mew","Horse":"Neigh"}
class animal:
 def __init__ (self):
        self.catego = "catego"
        self.sound = "temp"
        self.mammals ="YES"
       
        self.tail = "YES"
        self.teeth = "YES"
        self.legs = 4
        self.eyes = 2
        self.__nose = 1
        not_found = 0
        

        

        def accept_data():
            legs_count =input("\n\nEnter the number of the legs : ")
            self.legs= legs_count
            eyes_count = input("Enter the number of eyes : ")
            self.eyes =eyes_count
            nose_count = input("Enter the number of nose : ")
            self.__nose = nose_count
            tail = input("Does it have tail : ")
            self.tail = tail
            teeth=input("Does it have Teeth : ")
            self.teeth = teeth
            mammal=input("Is it a mammal: ")
            self.mammals = mammal
            sound = input("What sound Does it make: ")
            sound = sound.capitalize()
            self.sound=sound
            

        accept_data() 

        if(1>0):
            for x in animals_data:
                if(animals_data[x]==self.sound):
                    self.catego = x
            if(self.catego == "catego"):
                not_found = 1
                print("\nAnimal Not Found!!\n\n")
        if(not_found==0):
            print("\n--------------------------For "+self.catego+"--------------------------")
            print("I am "+self.catego)
            print("Number of legs: {0} ".format(self.legs)) 
            print("Number of eyes: {0} ".format(self.eyes)) #eyes is private hence we cannot acces it
            print("Number of Nose: {0} ".format(self.__nose))
            print("Is tail Present: "+self.tail+" ")
            print("Is teeth Present: "+self.teeth+" ")
            print("Is a mammal: "+self.mammals+" ")
            print("Hence I "+self.sound+" ")
            print("----------------------------------------------------\n\n\n")
        


while(1):
    print("\n-----------Welcome to Animal Detector-----------\n\n1) Check Animal\n2) Add animal\n3) Display animal list\n4) Exit")
    cho = int(input("Enter your choice: "))
    if(cho == 1):
        some_animal = animal()
    elif(cho == 2):
        ani = input("Enter the name of animal: ")
        ani=ani.capitalize()
        sound = input("Enter the sound it makes: ")
        sound = sound.capitalize()
        animals_data[ani] = sound
        print("Animal Added Sucessfully \n")
    elif(cho == 3):
        print("Animals in Data base are: \n")
        for x in animals_data:
            print("{0} : {1} \t".format(x,animals_data[x]))
    elif(cho==4):
        break
    else:
        print("\nSelect from the given choices....\n")

print("\n\n Thank for using our Animal Detector")








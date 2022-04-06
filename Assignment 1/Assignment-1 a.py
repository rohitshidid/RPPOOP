

class animal:
 def __init__ (self,catego,sound):
        self.catego = catego
        self.sound = sound
        self.mammals ="YES"
       
        self.tail = "YES"
        self.teeth = "YES"
        self.legs = 4
        self.eyes = 2
        self.__nose = 1

        

        

        def accept_data():
            print("For "+self.catego)
            legs_count =input("Enter the number of the legs : ")
            self.legs= legs_count
            eyes_count = input("Enter the number of eyes : ")
            self.eyes =eyes_count
            nose_count = input("Enter the number of nose : ")
            self.__nose = nose_count
            tail = ""
            tail = input("Does it have tail : ")
            self.tail = tail
            teeth=input("Does it have Teeth : ")
            self.teeth = teeth
            mammal=input("Is it a mammal: ")
            self.mammals = mammal
            

        accept_data() 

        print("\n--------------------------For "+self.catego+"--------------------------")
        print("I am "+self.catego)
        print("Number of legs: {0} ".format(self.legs)) 
        print("Number of eyes: {0} ".format(self.eyes)) #eyes is private hence we cannot acces it
        print("Number of Nose: {0} ".format(self.__nose))
        print("Is tail Present: "+self.tail+" ")
        print("Is teeth Present: "+self.teeth+" ")
        print("Is a mammal: "+self.mammals+" ")
        print("Hence I "+self.sound+" ")
        print("----------------------------------------------------")
        

dog = animal("Dog","Bark")
cat = animal("Cat","Mew")
horse = animal("Horse","Neigh")
rabbit = animal("Rabbit","Grunt")
cow = animal("Cow","Moo")
tiger = animal("Tiger","Growl")
lion = animal("Lion","Roar")
wolf = animal("Wolf","Howl")
deer = animal("Deer","Grunt")
elephant = animal("Elephant","Trumpet")






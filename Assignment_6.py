from tkinter import E
import numpy as np
x = np.array([[0, 0], [0, 0]])
y = np.array([[0, 0], [0, 0]])

print("Enter the elements for first matrix")
x[0,0] = int(input("For 00: "))
x[0,1] = int(input("For 01: "))
x[1,0] = int(input("For 10: "))
x[1,1] = int(input("For 11: "))
print("Enter the elements for Second matrix")
y[0,0] = int(input("For 00: "))
y[0,1] = int(input("For 01: "))
y[1,0] = int(input("For 10: "))
y[1,1] = int(input("For 11: "))

while True: 
    print("\n\n\n+++++++++++++ Menu ++++++++++++\n")
    print ("1) Addition")
    print("2) Subtraction")
    print("3) Division")
    print("4) Multiplication ")
    print("5) Transpose")
    print("6) Exit")
    print("9) View")
    cho = int(input("Enter your Choice: "))
    if(cho == 1):
        print ("Addition of two matrices: ")
        print (np.add(x,y))
    elif(cho == 2):
        print ("Subtraction of two matrices : ")
        print (np.subtract(x,y))
    elif(cho == 3):
        print ("Matrix Division : ")
        print (np.divide(x,y))
    elif(cho == 4):
        print ("Multiplication of two matrices: ")
        print (np.multiply(x,y))
    elif(cho == 5):
        print ("Matrix transposition : ")
        print (x.T)
        print(y.T)
    elif(cho == 9):
        print(x)
        print(y)
    elif(cho == 6):
        break;
    else:
        print("Invalid Choice! ")


    
    
    
    
   
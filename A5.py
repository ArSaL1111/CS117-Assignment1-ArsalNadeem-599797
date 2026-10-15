#This program will take three values of resistors as input and tells us the greates and smallest value of resistor
R1=int(input("Enter Resistor1: "))
R2=int(input("Enter Resistor2: "))
R3=int(input("Enter Resistor3: "))
if R1 >= R2 and R1 >= R3:
    largest = R1
elif R2 >= R1 and R2 >= R3:
    largest = R2
else:
    largest = R3
print("Largest = ", largest, "ohms")
if R1 <= R2 and R1 <= R3:
    smallest = R1
elif R2 <= R1 and R2 <= R3:
    smallest = R2
else:
    smallest = R3
print("Smallest = ", smallest, "ohms")

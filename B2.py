#This program finds the equavilent resistance of resistors in series
series=int(input("How many resistors in series?: "))
count=1
Total_R=0
while count<=series:
    Resistor=int(input(f"Enter R{count}:"))
    count+=1
    Total_R+=Resistor
print("Total Resistance: ", Total_R,"ohms")
    

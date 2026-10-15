#This program calculates current through a fixed resistor value from 1V to 10V voltages
for V in range(1,11):
    I=V/10
    print("V = ", V,"V",", I = ", I,"A")

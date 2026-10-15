#Resistor Color Code Values: this program will take color of resistor band show its value to user
Color=str(input("Enter Color: "))
lower_case=Color.lower()
if lower_case=="black":
    print("Digit = 0")
elif lower_case=="brown":
    print("Digit = 1")
elif lower_case=="red":
    print("Digit = 2")
elif lower_case=="orange":
    print("Digit = 3")
elif lower_case=="yellow":
    print("Digit = 4")
elif lower_case=="green":
    print("Digit = 5")
elif lower_case=="blue":
    print("Digit = 6")
elif lower_case=="violet":
    print("Digit = 7")
elif lower_case=="grey":
    print("Digit = 8")
elif lower_case=="white":
    print("Digit = 9")
else:
    print("Invalid Color")


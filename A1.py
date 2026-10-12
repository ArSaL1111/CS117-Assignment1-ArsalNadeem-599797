#Finding Current and Fuse Check
V=int(input("Enter Voltage(V):"))
R=int(input("Enter Resistance(ohms):"))
if R<=0:
    print("Invalid Resistance")
else:
    I=V/R
    if I>2:
        print("Fuse will blow")
    else:
        print("Current(A):", I)

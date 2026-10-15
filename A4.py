#Logic Gates: In this program we will take input from user in 1 or 0 and evaluate logic gates
A=int(input("Enter A: "))
B=int(input("Enter B: "))
if (A==1 or A==0) and (B==1 or B==0):
    if A==1 and B==1:
        print("AND = 1")
    else:
        print("AND = 0")
    if A==1 or B==1:
        print("OR = 1")
    else:
        print("OR = 0")
    if A==1 and B==0 or A==0 and B==1:
        print("XOR = 1")
    else:
        print("XOR = 0")
else:
    print("Bits must be 0 or 1")

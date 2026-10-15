#This program checks tolerance of resistance and divides them into 1% and 5% and invalid category. Program ends when 0 is entered.
count_1=0
count_5=0
count_invalid=0
while True:
    R=float(input("Enter Resistance: "))
    if R==0:
        break
    if 99.0<=R<=101.0:
        count_1+=1
    elif 95.0<=R<=105.0:
        count_5+=1
    else:
        count_invalid+=1
print("Total R with 1% tolerance: ", count_1)
print("Total R with 5% tolerance: ", count_5)
print("Total rejected: ", count_invalid)
        

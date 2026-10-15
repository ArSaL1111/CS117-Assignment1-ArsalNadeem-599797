#this program converts decimal positive numbers into binary string
def decimal_to_binary(n):
    binary=""
    quotient=n
    if quotient==0:
        return 0
    elif quotient<0:
        return "Negative value"
    while quotient>0:
        remainder=int(quotient)%2
        binary=str(remainder)+binary
        quotient=quotient//2
    return binary
print(decimal_to_binary(25))
        

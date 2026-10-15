#this program takes three resistance values from star network and convert them into delta network
def star_to_delta(ra, rb, rc):
    R_numerator=ra*rb+rb*rc+rc*ra
    R_ab=R_numerator/rc
    R_bc=R_numerator/ra
    R_ca=R_numerator/rb
    return round(R_ab, 2), round(R_bc, 2), round(R_ca, 2)
print(star_to_delta(10, 20, 30))
    
    
    

#This program calculates theoretical voltage drop, and actual voltage drop when load is attached with the source.
def loaded_divider(vs, r1, r2, rl):
    unload_voltage=(r1/(r1+r2))*vs
    R_eq=(r2*rl)/(r2+rl)
    load_voltage=(R_eq/(r1+R_eq))*vs
    return 'Theoretical:',unload_voltage, 'Actual:',load_voltage
print(loaded_divider(12, 1000, 1000, 500))
    
    

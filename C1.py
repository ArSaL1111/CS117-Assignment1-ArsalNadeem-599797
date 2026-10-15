#There are two functions in this program. One calculates the current and other calculates power.
def ohms_current(v, r):
    current=v/r
    return current
i=ohms_current(12, 6)
print("Current = ", i, "A")
def power_dissipated(i, r):
    p=(i*i)*r
    return p
print("Power = ", power_dissipated(i, 6), "W")

#In this program a function evaluates equivalent resistance in parallel.
def parallel_resistance(resistors):
    R_equivalent=0
    for R in resistors:
        R_equivalent += 1/R
    return 1/R_equivalent
print("R_equivalent in parallel: ", parallel_resistance([10, 10]))
print("R_equivalent in parallel: ", parallel_resistance([100, 200, 300]))

#This program finds the longest interval of voltage drop along with time taken for the voltage drop.
voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
count = 1
max_count = 1

start = voltages[0]
best_start = voltages[0]
best_end = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        count += 1
        if count > max_count:
            max_count = count
            best_start = start
            best_end = voltages[i]
    else:
        count = 1
        start = voltages[i]
print(f"Longest continuous drop: {max_count} minutes Started at: {best_start} V Ended at: {best_end} V")
        
    

#This program is divided into four parts

#Part(a) to find total readings above 3.2
readings=[3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2]
count=0
for i in range(0, len(readings)):
    if readings[i]>3.2:
        count+=1
print("Readings above 3.2 V: ", count)

#Part(b) This part finds the maximum reading. Logic of program is:
#"Take first reading and check it with rest of readings in the array by iterating"
Max=readings[0]
for i in range(0, len(readings)):
        if readings[i]>Max:
            Max=readings[i]
print("Highest: ", Max,"V")

#Part(c) has same logic as of part(b) and it finds the minimum reading
Min=readings[0]
for i in range(0, len(readings)):
        if readings[i]<Min:
            Min=readings[i]
print("Lowest: ", Min,"V")

#Part(d) finds the average readings
Total=0
for i in range(0, len(readings)):
    Total+=readings[i]
Average=Total/len(readings)
print("Average: ", Average,"V")


        

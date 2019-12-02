import math;
totalMass = 0;

with open('input1.txt', 'r') as f:
    for line in f:
        num = int(line.strip());
        totalMass += (math.floor(num/3) - 2);

print("Total mass: " + str(totalMass));

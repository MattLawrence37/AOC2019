import math;
totalMass = 0;

def calcFuel(mass):
    tempMass = (math.floor(mass/3) - 2);
    if(tempMass < 0):
        return 0;
    else:
        return tempMass;

with open('input1.txt', 'r') as f:
    for line in f:
        tempMass = int(line.strip());
        while(tempMass > 0):
            tempMass = calcFuel(tempMass);
            totalMass += tempMass;

print("Total mass: " + str(totalMass));

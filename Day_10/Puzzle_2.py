import math;
import copy;

file = open('input.txt', 'r')
asteroidData = [];
for line in file.readlines():
    lineData = list(line.rstrip());
    asteroidData.append(lineData);

startX = 26;
startY = 36;

asteroidTemp = copy.deepcopy(asteroidData);
currentAngle = math.pi / 2;
prevAngle = 0;

def recalculateAngles():
    currentAsteroid = asteroidData[startY][startX];
    for y in range(len(asteroidTemp)):
        for x in range(len(asteroidTemp[y])):
            if(asteroidTemp[y][x] == '.' or (startX == x and startY == y)):
                continue;
            asteroidAngle = math.atan2(y - startY, x - startX) + currentAngle;
            if(asteroidAngle < 0):
                asteroidAngle += (2*math.pi);
            asteroidTemp[y][x] = (math.degrees(asteroidAngle));

def getLowestAngleCoords():
    minY = 0;
    minX = 0;
    minValue = 360;
    for y in range(len(asteroidTemp)):
        for x in range(len(asteroidTemp[y])):
            if(asteroidTemp[y][x] == '.' or asteroidTemp[y][x] == '#'):
                continue;
            if(asteroidTemp[y][x] < minValue):
                minY = y;
                minX = x;
                minValue = asteroidTemp[y][x];
    return (minX, minY);

def getLowestAngleCoordsNotZero():
    global prevAngle;
    minY = 0;
    minX = 0;
    minValue = 360;
    for y in range(len(asteroidTemp)):
        for x in range(len(asteroidTemp[y])):
            if(asteroidTemp[y][x] == '.' or asteroidTemp[y][x] == '#'):
                continue;
            if(asteroidTemp[y][x] < minValue and asteroidTemp[y][x] > prevAngle):
                minY = y;
                minX = x;
                minValue = asteroidTemp[y][x];
    return (minX, minY);
            

def destroyLowestAngle(currentCount, targetX, targetY):
    global prevAngle;
    distanceX = targetX - startX;
    distanceY = targetY - startY;

    stepX = int(distanceX / math.gcd(abs(distanceX), abs(distanceY)));
    stepY = int(distanceY / math.gcd(abs(distanceX), abs(distanceY)));

    lookingX = startX + stepX;
    lookingY = startY + stepY;

    iterations = 0;
    if(stepX == 0):
        iterations = int(distanceY/stepY);
    elif(stepY == 0):
        iterations = int(distanceX/stepX);
    else:
        iterations = int(max(distanceX/stepX, distanceY/stepY));
    
    for i in range(iterations):
        if(asteroidTemp[lookingY][lookingX] != '.'):
            #DESTROY
            #print("Destroyed asteroid " + str(currentCount) + " at " + str(lookingX) + ", " + str(lookingY));
            prevAngle = asteroidTemp[lookingY][lookingX];
            asteroidTemp[lookingY][lookingX] = '.';
            break;
        else:
            lookingX += stepX;
            lookingY += stepY;

def resetCurrentAngle(targetX, targetY):
    currentAngle = math.atan2(targetY - startY, targetX - startX) + (math.pi / 2);

recalculateAngles();
lowestAngle = getLowestAngleCoords();
for i in range(1, 200):
    destroyLowestAngle(i, lowestAngle[0], lowestAngle[1]);
    resetCurrentAngle(lowestAngle[0], lowestAngle[1]);
    
    recalculateAngles();
    lowestAngle = getLowestAngleCoordsNotZero();

print(str((lowestAngle[0] * 100) + lowestAngle[1]));



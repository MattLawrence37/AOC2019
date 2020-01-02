import math;
import copy;

file = open('input.txt', 'r')
asteroidData = [];
for line in file.readlines():
    lineData = list(line.rstrip());
    asteroidData.append(lineData);

asteroidX = -1;
asteroidY = -1;
mostSeen = 0;
for y1 in range(len(asteroidData)):
    for x1 in range(len(asteroidData[y1])):
        currentAsteroid = asteroidData[y1][x1];
        if(currentAsteroid != '#'):
            continue;
        else:
            asteroidTemp = copy.deepcopy(asteroidData);
            asteroidTemp[y1][x1] = "O";
            for y2 in range(len(asteroidTemp)):
                for x2 in range(len(asteroidTemp[y2])):
                    lookingAsteroid = asteroidTemp[y2][x2];
                    if(lookingAsteroid != '#'):
                        continue;
                    if(y1 == y2 and x1 == x2):
                        continue;
                    else:
                        distanceX = x2 - x1;
                        distanceY = y2 - y1;

                        stepX = int(distanceX / math.gcd(abs(distanceX), abs(distanceY)));
                        stepY = int(distanceY / math.gcd(abs(distanceX), abs(distanceY)));

                        lookingX = x1 + stepX;
                        lookingY = y1 + stepY;

                        iterations = 0;
                        if(stepX == 0):
                            iterations = int(distanceY/stepY);
                        elif(stepY == 0):
                            iterations = int(distanceX/stepX);
                        else:
                            iterations = int(max(distanceX/stepX, distanceY/stepY));
                        
                        for i in range(iterations):
                            if(asteroidTemp[lookingY][lookingX] == '#' or asteroidTemp[lookingY][lookingX] == '@'):
                                asteroidTemp[lookingY][lookingX] = "@";
                                break;
                            else:
                                lookingX += stepX;
                                lookingY += stepY;
            cometCount = sum(x.count('@') for x in asteroidTemp);
            if(cometCount > mostSeen):
                mostSeen = cometCount;
                asteroidX = x1;
                asteroidY = y1;
print(str(asteroidX) + ", " + str(asteroidY));
print("Detected asteroids: " + str(mostSeen));

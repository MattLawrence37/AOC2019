import re;
import copy;
counter = 0;
class Moon:
    def __init__(self, posX, posY, posZ):
        self.posX = posX;
        self.posY = posY;
        self.posZ = posZ;
        self.velX = 0;
        self.velY = 0;
        self.velZ = 0;

    def calculateEnergy(self):
        return (abs(self.posX) + abs(self.posY) + abs(self.posZ)) * (abs(self.velX) + abs(self.velY) + abs(self.velZ))

file = open('input.txt', 'r')
moonList = [];
for line in file.readlines():
    line = re.sub(r'([a-z]+)(=)', '', line);
    line = line.replace(">", "");
    line = line.replace("<", "");
    line = line.replace(" ", "");

    listData = line.rstrip().split(",");
    moonList.append(Moon(int(listData[0]), int(listData[1]), int(listData[2])));

startingMoons = copy.deepcopy(moonList);
foundX = False;
foundY = False;
foundZ = False;

def doPosMatch(moon1, moon2):
    return moon1.posX == moon2.posX and moon1.posY == moon2.posY and moon1.posZ == moon2.posZ;

def doVelMatch(moon1, moon2):
    return moon1.velX == moon2.velX and moon1.velY == moon2.velY and moon1.velZ == moon2.velZ;

def doMatch(moon1, moon2):
    return doPosMatch(moon1, moon2) and doVelMatch(moon1, moon2);

hashArray = [];
i = 0;
while(True):
    for x1 in range(len(moonList)):
        for x2 in range(x1 + 1, len(moonList)):
            moon1 = moonList[x1];
            moon2 = moonList[x2];
            if(moon1.posX > moon2.posX):
                moon1.velX -= 1;
                moon2.velX += 1;
            elif(moon1.posX < moon2.posX):
                moon1.velX += 1;
                moon2.velX -= 1;

            if(moon1.posY > moon2.posY):
                moon1.velY -= 1;
                moon2.velY += 1;
            elif(moon1.posY < moon2.posY):
                moon1.velY += 1;
                moon2.velY -= 1;

            if(moon1.posZ > moon2.posZ):
                moon1.velZ -= 1;
                moon2.velZ += 1;
            elif(moon1.posZ < moon2.posZ):
                moon1.velZ += 1;
                moon2.velZ -= 1;
   
    for moon in moonList:
        moon.posX += moon.velX;
        moon.posY += moon.velY;
        moon.posZ += moon.velZ;

    i += 1;
    if(foundX == False):
        if((moonList[0].posX == startingMoons[0].posX) and (moonList[1].posX == startingMoons[1].posX) and (moonList[2].posX == startingMoons[2].posX) and (moonList[3].posX == startingMoons[3].posX)):
            if((moonList[0].velX == startingMoons[0].velX) and (moonList[1].velX == startingMoons[1].velX) and (moonList[2].velX == startingMoons[2].velX) and (moonList[3].velX == startingMoons[3].velX)):
                print("X repeats at :" + str(i));
                foundX = True;
    if(foundY == False):
        if((moonList[0].posY == startingMoons[0].posY) and (moonList[1].posY == startingMoons[1].posY) and (moonList[2].posY == startingMoons[2].posY) and (moonList[3].posY == startingMoons[3].posY)):
            if((moonList[0].velY == startingMoons[0].velY) and (moonList[1].velY == startingMoons[1].velY) and (moonList[2].velY == startingMoons[2].velY) and (moonList[3].velY == startingMoons[3].velY)):
                print("Y repeats at :" + str(i));
                foundY = True;
    if(foundZ == False):
        if((moonList[0].posZ == startingMoons[0].posZ) and (moonList[1].posZ == startingMoons[1].posZ) and (moonList[2].posZ == startingMoons[2].posZ) and (moonList[3].posZ == startingMoons[3].posZ)):
            if((moonList[0].velZ == startingMoons[0].velZ) and (moonList[1].velZ == startingMoons[1].velZ) and (moonList[2].velZ == startingMoons[2].velZ) and (moonList[3].velZ == startingMoons[3].velZ)):
                print("X repeats at :" + str(i));
                foundZ = True;
    if(foundX and foundY and foundZ):
        break;


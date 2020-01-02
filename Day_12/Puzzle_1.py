import re;
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

for i in range(3):
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

    #print("After " + str(i) + " steps:");            
    for moon in moonList:
        moon.posX += moon.velX;
        moon.posY += moon.velY;
        moon.posZ += moon.velZ;
        print(hash(moon));
        #print("X: " + str(moon.posX) + " Y: " + str(moon.posY) + " Z: " + str(moon.posZ) + " vX: " + str(moon.velX) + " vY: " + str(moon.velY) + " vZ: " + str(moon.velZ));

energy = 0;
for moon in moonList:
    energy += moon.calculateEnergy();
print(energy);
        


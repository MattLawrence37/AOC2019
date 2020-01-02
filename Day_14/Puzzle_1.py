import copy;
import math;

class Resource:
    def __init__(self, name):
        self.name = name;
        self.quantity = 1;
        self.ingredients = [];

    def setRecipe(self, quantity, ingredients):
        self.quantity = quantity;
        self.ingredients = ingredients;

resourceList = {};
recipeList = {};

file = open('input.txt', 'r')
for line in file.readlines():
    listData = line.rstrip().replace(" =>", ",");
    listData = listData.split(", ");
    resourceData = [];
    for x in listData:
        data = x.split(" ");
        data[0] = int(data[0]);
        resourceData.append(data);

    for i in range(len(resourceData)):
        x = resourceData[i];
        
        if(i == len(resourceData) - 1):
            if(x[1] not in resourceList):
                resourceList[x[1]] = Resource(x[1]);
            resourceList[x[1]].setRecipe(x[0], resourceData[:-1]);
        elif(x[1] not in resourceList):
             resourceList[x[1]] = Resource(x[1]);

currentMaterial = [[1, resourceList['FUEL']]];
tempMaterial = [];
while(len(currentMaterial) > 0):
    for x in currentMaterial:
        ingredients = x[1].ingredients;
        print(str(x[0]) + " " + x[1].name);
        for y in ingredients:
            doesExist = False;
            for z in tempMaterial:
                if(z[1] == resourceList[y[1]]):
                    doesExist = True;
                    z[0] += (x[0] * y[0]) / x[1].quantity;
                    break;
            if(not doesExist):
                tempMaterial.append([(x[0] * y[0]) / x[1].quantity , resourceList[y[1]]]);
##        if(len(ingredients) == 0):
##            doesExist = False;
##            for z in tempMaterial:
##                if(z[1] == x[1]):
##                    doesExist = True;
##                    z[0] += x[0];
##                    break;
##            if(not doesExist):
##                tempMaterial.append(x);
    for z in tempMaterial:
        z[0] = math.ceil(z[0]/z[1].quantity)*z[1].quantity;
    currentMaterial = copy.deepcopy(tempMaterial);
    tempMaterial.clear();
    print("");


        


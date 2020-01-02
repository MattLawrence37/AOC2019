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

#return true if resource ccan still get made, otherwise return false
def findParents(resourceName):
    resource = resourceList[resourceName];
    onesToSearch = [];
    for i in resourceList:
        if(i.name != resourceName):
            for x in i.ingredients:
                if(x[1] == resourceName):
                    onesToSearch.append(x[1]);
    

prevArray = [];
while(True):
    if(len(currentMaterial) == 1):
        if(currentMaterial[0][1].name == "ORE"):
            print(str(currentMaterial[0][0]) + " ORE");
            break;
    
    doMatch = True;
    if(len(prevArray) == len(currentMaterial)):
        for i in range(len(currentMaterial)):
            if(prevArray[i][0] != currentMaterial[i][0] or prevArray[i][1].name != currentMaterial[i][1].name):
                doMatch = False;
                break;
    else:
        doMatch = False;
    
    for x in currentMaterial:
        ingredients = x[1].ingredients;
        resourceCount = x[0];
        print(str(x[0]) + " " + x[1].name);
        if(len(ingredients) == 0):
            doesExist = False;
            for z in tempMaterial:
                if(z[1].name == x[1].name):
                    doesExist = True;
                    z[0] += resourceCount;
                    break;
            if(not doesExist):
                tempMaterial.append(x);
        else:
            if(resourceCount >= x[1].quantity):
                for y in ingredients:
                    newCountAmount = (resourceCount // x[1].quantity) * y[0];
                    doesExist = False;
                    for z in tempMaterial:
                        if(z[1].name == y[1]):
                            doesExist = True;
                            z[0] += newCountAmount;
                            break;
                    if(not doesExist):
                        tempMaterial.append([newCountAmount, resourceList[y[1]]]);
                        
                    remainderAmount = resourceCount % x[1].quantity;
                    if(remainderAmount != 0):
                        doesExist = False;
                        for z in tempMaterial:
                            if(z[1].name == x[1].name):
                                doesExist = True;
                                z[0] += remainderAmount;
                                break;
                        if(not doesExist):
                            tempMaterial.append([remainderAmount, x[1]]);
            else:
                
                if(not doMatch or findParents(x[1].name)):
                    tempMaterial.append(x);
                else:
                    for y in ingredients:
                        tempMaterial.append([y[0], resourceList[y[1]]]);

    prevArray = copy.deepcopy(currentMaterial);
    currentMaterial = copy.deepcopy(tempMaterial);
    tempMaterial.clear();


        


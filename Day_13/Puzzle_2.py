file = open('input.txt', 'r')
listData = [];
for line in file.readlines():
    listData = line.rstrip().split(',');
	
listData = list(map(int, listData));

tileArray = [[0 for i in range(10)] for j in range(10)]

MODE_POSITION = 0;
MODE_IMMEDIATE = 1;
MODE_RELATIVE = 2;

class OpcodeComputer:
    def __init__(self, data):
        self.currentPos = 0;
        self.relativeBase = 0;
        self.tempData = data.copy();

    def extendArray(self, pos):
        for x in range(len(self.tempData), pos + 1):
            self.tempData.append(0);

    def testIndex(self, index):
        if(index >= len(self.tempData)):
           self.extendArray(index);  

    def getParameter(self, mode, offset):
        self.testIndex(self.currentPos + offset);
        if(mode == MODE_IMMEDIATE):
            return self.tempData[self.currentPos + offset];
        elif(mode == MODE_RELATIVE):
            self.testIndex(self.relativeBase + self.tempData[self.currentPos + offset]);
            return self.tempData[self.relativeBase + self.tempData[self.currentPos + offset]];
        else:
            self.testIndex(self.tempData[self.currentPos + offset]);
            return self.tempData[self.tempData[self.currentPos + offset]];

    def getIndex(self, mode, offset):
        self.testIndex(self.currentPos + offset);
        if(mode == MODE_IMMEDIATE):
            return self.currentPos + offset;
        elif(mode == MODE_RELATIVE):
            self.testIndex(self.relativeBase + self.tempData[self.currentPos + offset]);
            return self.relativeBase + self.tempData[self.currentPos + offset];
        else:
            self.testIndex(self.tempData[self.currentPos + offset]);
            return self.tempData[self.currentPos + offset];    

    def performCommand(self):
        outputInstructions = [];       
        while(self.currentPos < len(self.tempData)):
            opCode = self.tempData[self.currentPos];
            
            paramMode1 = MODE_POSITION;
            paramMode2 = MODE_POSITION;
            paramMode3 = MODE_POSITION;

            if(opCode > 99):
                paramMode1 = ((opCode // 100) % 10);
                paramMode2 = ((opCode // 1000) % 10);
                paramMode3 = ((opCode // 10000) % 10);
                opCode = opCode % 100;
                
            if(opCode == 1):
                # Adds
                param1 = self.getParameter(paramMode1, 1);
                param2 = self.getParameter(paramMode2, 2);
                self.tempData[self.getIndex(paramMode3, 3)] = param1 + param2;
                self.currentPos += 4;
            elif(opCode == 2):
                # Multiplies
                param1 = self.getParameter(paramMode1, 1);
                param2 = self.getParameter(paramMode2, 2);
                self.tempData[self.getIndex(paramMode3, 3)] = param1 * param2;
                self.currentPos += 4;
            elif(opCode == 3):
                # Sets value
                printArray();
                inputVal = int(input("Request input:"));
                self.tempData[self.getIndex(paramMode1, 1)] = inputVal;
                self.currentPos += 2;
            elif(opCode == 4):
                # Prints value
                param1 = self.getParameter(paramMode1, 1);
                outputInstructions.append(param1);
                if(len(outputInstructions) == 3):
                    if(outputInstructions[0] == -1 and outputInstructions[1] == 0):
                        print(outputInstructions[2]);
                    else:
                        setTile(outputInstructions[0],outputInstructions[1],outputInstructions[2]);
                    outputInstructions.clear();
                    
                self.currentPos += 2;
            elif(opCode == 5):
                # Jump if true
                param1 = self.getParameter(paramMode1, 1);
                if(param1 != 0):
                    param2 = self.getParameter(paramMode2, 2);
                    self.currentPos = param2;
                else:
                    self.currentPos += 3;
            elif(opCode == 6):
                # Jump if false
                param1 = self.getParameter(paramMode1, 1);
                if(param1 == 0):
                    param2 = self.getParameter(paramMode2, 2);
                    self.currentPos = param2;
                else:
                    self.currentPos += 3;
            elif(opCode == 7):
                # Less than
                param1 = self.getParameter(paramMode1, 1);
                param2 = self.getParameter(paramMode2, 2);
                if(param1 < param2):
                    self.tempData[self.getIndex(paramMode3, 3)] = 1;
                else:
                    self.tempData[self.getIndex(paramMode3, 3)] = 0;
                self.currentPos += 4;
            elif(opCode == 8):
                # Equal to
                param1 = self.getParameter(paramMode1, 1);
                param2 = self.getParameter(paramMode2, 2);
                if(param1 == param2):
                    self.tempData[self.getIndex(paramMode3, 3)] = 1;
                else:
                    self.tempData[self.getIndex(paramMode3, 3)] = 0;
                self.currentPos += 4;
            elif(opCode == 9):
                param1 = self.getParameter(paramMode1, 1);
                self.relativeBase += param1;
                self.currentPos += 2;
            elif(opCode == 99):
                # Finishes
                print("Program End");
                break;
            else:
                print("Something went wrong");
        return -1;
        print("END");

def setTile(posX, posY, tile):
    if(posX >= len(tileArray[0])):
        for array in tileArray:
            array.append(0);
            
    if(posY >= len(tileArray)):
        tileArray.append([0 for i in range(len(tileArray[0]))]);
    tileArray[posY][posX] = tile;

def printArray():
    for line in tileArray:
        for tile in line:
            if(tile == 0):
                print(" ", end = '');
            elif(tile == 1):
                print("█", end = '');
            elif(tile == 2):
                print("■", end = '');
            elif(tile == 3):
                print("●", end = '');
            elif(tile == 4):
                print("═", end = '');
        print("");
    print("\n");

computer = OpcodeComputer(listData);
computer.tempData[0] = 2;
computer.performCommand();

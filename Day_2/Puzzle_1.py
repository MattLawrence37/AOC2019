file = open('input.txt', 'r')
listData = [];
for line in file.readlines():
    listData = line.rstrip().split(',');
	
listData = list(map(int, listData));

listData[1] = 12;
listData[2] = 2;

currentPos = 0;
while(currentPos < len(listData)):
    opCode = listData[currentPos];
    if(opCode == 1):
        # Adds
        listData[listData[currentPos + 3]] = listData[listData[currentPos + 1]] + listData[listData[currentPos + 2]];
    elif(opCode == 2):
        # Multiplies
        listData[listData[currentPos + 3]] = listData[listData[currentPos + 1]] * listData[listData[currentPos + 2]];
    elif(opCode == 99):
        # Finishes
        print("Program End");
        break;
    else:
        print("Something went wrong");

    currentPos += 4;

print(listData[0]);

    

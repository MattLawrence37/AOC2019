file = open('input.txt', 'r')
inputString = 0;
for line in file.readlines():
    inputString = line.rstrip();
	
width = 25;
height = 6;

imageData = [];
currentLayer = [];
currentRow = [];
for digit in inputString:
    if(len(currentRow) < width):
        currentRow.append(digit);
    elif(len(currentLayer) < height):
        currentLayer.append(currentRow.copy());
        currentRow.clear();
        currentRow.append(digit);
    else:
        imageData.append(currentLayer.copy());
        currentLayer.clear();
        currentLayer.append(currentRow.copy());
        currentRow.clear();
        currentRow.append(digit);
currentLayer.append(currentRow.copy());
imageData.append(currentLayer.copy());



fewestZeroes = -1;
zeroLayer = [];
for layer in imageData:
    zeroCount = 0;
    for row in layer:
        zeroCount += row.count('0');
    if(fewestZeroes == -1 or zeroCount < fewestZeroes):
        fewestZeroes = zeroCount;
        zeroLayer = layer;

oneCount = 0;
twoCount = 0;
for row in zeroLayer:
    oneCount += row.count('1');
    twoCount += row.count('2');
print(oneCount);
print(twoCount);
print(oneCount * twoCount);
    
    

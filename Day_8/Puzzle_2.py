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

outputData = [[' ' for i in range(width)] for j in range(height)];
for w in range(width):
    for h in range(height):
        for layer in imageData:
            if(layer[h][w] == '0'):
                outputData[h][w] = "█";
                break;
            if(layer[h][w] == '1'):
                outputData[h][w] = " ";
                break;

for row in outputData:
    s1 = "";
    print(s1.join(row));
    
    

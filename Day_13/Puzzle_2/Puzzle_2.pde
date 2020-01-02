IntList listData = new IntList();
ArrayList<IntList> tileArray;
OpcodeComputer computer;
  
enum paramMode { POSITION, IMMEDIATE, RELATIVE};

paramMode intToParam(int input)
{
  switch(input)
  {
    case 0: return paramMode.POSITION;
    case 1: return paramMode.IMMEDIATE;
    case 2: return paramMode.RELATIVE;
    default: return paramMode.POSITION;
  }
}

void setTile(int posX, int posY, int tile)
{
  if(posX >= tileArray.get(0).size())
  {
    for(IntList intList : tileArray)
    {
      intList.append(0);
    }
  }
  
  if(posY >= tileArray.size())
  {
    IntList intList = new IntList();
    for(int i = 0; i < tileArray.get(0).size(); i++)
    {
      intList.append(0);
    }
    tileArray.add(intList);
  }
  tileArray.get(posY).set(posX, tile);
}

void setup()
{
  frameRate(10);
  size(900, 500);
  Table table = loadTable("input.csv");
  for (TableRow row : table.rows())
  {
    for(int i = 0; i < row.getColumnCount(); i++)
    {
      int num = row.getInt(i);
      listData.append(num);
    }
  }
  
  IntList tempList = new IntList();
  tempList.append(0);
  tileArray = new ArrayList<IntList>();
  tileArray.add(tempList);  
  
  computer = new OpcodeComputer(listData);
  computer.tempData.set(0, 2);
  computer.performCommand();
}

void draw()
{
  if(computer.isPaused)
    {
      int val = 0;
      if(keyPressed && key == CODED)
      {
        if(keyCode == LEFT)
        {
          val = -1;
        }
        else if(keyCode == RIGHT)
        {
          val = 1;
        }
      }
      computer.resumeExecution(val);
    }
}

void drawScreen()
{
  background(50);
  for(int y = 0; y < tileArray.size(); y++)
  {
    for(int x = 0; x < tileArray.get(y).size(); x++)
    {
      switch(tileArray.get(y).get(x))
      {
      case 0: 
        break;
      case 1:
        rect(x * 20, y * 20, 20, 20);
        break;
      case 2:
        rect((x * 20) + 2, (y * 20) + 2, 16, 16);
        break;
      case 3:
        rect(x * 20, (y * 20) + 10, 20, 10);
        break;
      case 4:
        ellipse(x * 20, y * 20, 10, 10);
        break;
      
      }
    }
  }
}

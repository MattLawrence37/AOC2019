class OpcodeComputer
{
  IntList tempData;
  int currentPos = 0;
  int relativeBase = 0;
  boolean isPaused = false;
  paramMode pausedParam = paramMode.POSITION;
  
  boolean startGame = false;
  
  OpcodeComputer(IntList data)
  {
    tempData = data.copy();
  }
  
  void extendArray(int pos)
  {
    if(pos > this.tempData.size())
    {
      for(int i = this.tempData.size() - 1; i < pos; i++)
      {
        this.tempData.append(0);
      }
    }
  }
  
  void testIndex(int pos)
  {
    if(pos >= this.tempData.size())
    {
      this.extendArray(pos);
    }
  }
  
  int getParameter(paramMode mode, int offset)
  {
    this.testIndex(this.currentPos + offset);
    if(mode == paramMode.IMMEDIATE)
    {
      return this.tempData.get(this.currentPos + offset);
    }
    else if(mode == paramMode.RELATIVE)
    {
      this.testIndex(this.relativeBase + this.tempData.get(this.currentPos + offset));
      return this.tempData.get(this.relativeBase + this.tempData.get(this.currentPos + offset));
    }
    else
    {
      this.testIndex(this.tempData.get(this.currentPos + offset));
      return this.tempData.get(this.tempData.get(this.currentPos + offset));
    }
  }
  
  int getIndex(paramMode mode, int offset)
  {
    this.testIndex(this.currentPos + offset);
    if(mode == paramMode.IMMEDIATE)
    {
      return this.currentPos + offset;
    }
    else if(mode == paramMode.RELATIVE)
    {
      this.testIndex(this.relativeBase + this.tempData.get(this.currentPos + offset));
      return this.relativeBase + this.tempData.get(this.currentPos + offset);
    }
    else
    {
      this.testIndex(this.tempData.get(this.currentPos + offset));
      return this.tempData.get(this.currentPos + offset);
    }
  }
  
  void resumeExecution(int keyInt)
  {
      this.tempData.set(this.getIndex(this.pausedParam, 1), keyInt);
      this.currentPos += 2;
      this.isPaused = false;
      this.performCommand();
  }
  
  void performCommand()
  {
    IntList outputInstructions = new IntList();
    while(this.currentPos < this.tempData.size())
    {
      int opCode = this.tempData.get(this.currentPos);
      paramMode paramMode1 = paramMode.POSITION;
      paramMode paramMode2 = paramMode.POSITION;
      paramMode paramMode3 = paramMode.POSITION;
      
      int param1 = 0;
      int param2 = 0;
      int param3 = 0;
      
      if(opCode > 99)
      {
        paramMode1 = intToParam((opCode / 100) % 10);
        paramMode2 = intToParam((opCode / 1000) % 10);
        paramMode3 = intToParam((opCode / 10000) % 10);
        opCode = opCode % 100;
      }
      
      if(opCode == 1) //Adds
      {
        param1 = this.getParameter(paramMode1, 1);
        param2 = this.getParameter(paramMode2, 2);
        this.tempData.set(this.getIndex(paramMode3, 3), param1 + param2);
        this.currentPos += 4;
      }
      else if(opCode == 2) //Multiplies
      {
        param1 = this.getParameter(paramMode1, 1);
        param2 = this.getParameter(paramMode2, 2);
        this.tempData.set(this.getIndex(paramMode3, 3), param1 * param2);
        this.currentPos += 4;
      }
      else if(opCode == 3) //Sets value
      {
        drawScreen();
        this.pausedParam = paramMode1;
        this.isPaused = true;
        break;
      }
      else if(opCode == 4) //Prints output
      {
        param1 = this.getParameter(paramMode1, 1);
        outputInstructions.append(param1);
        if(outputInstructions.size() == 3)
        {
          if(outputInstructions.get(0) == -1 && outputInstructions.get(1) == 0)
          {
            println("SCORE: " + outputInstructions.get(2));
          }
          else
          {
            setTile(outputInstructions.get(0),outputInstructions.get(1),outputInstructions.get(2));
          }
          outputInstructions.clear();
        }
        this.currentPos += 2;
      }
      else if(opCode == 5) //Jump if true
      {
        param1 = this.getParameter(paramMode1, 1);
        if(param1 != 0)
        {
          param2 = this.getParameter(paramMode2, 2);
          this.currentPos = param2;
        }
        else
        {
          this.currentPos += 3;
        }
      }
      else if(opCode == 6) //Jump if false
      {
        param1 = this.getParameter(paramMode1, 1);
        if(param1 == 0)
        {
          param2 = this.getParameter(paramMode2, 2);
          this.currentPos = param2;
        }
        else
        {
          this.currentPos += 3;
        }
      }
      else if(opCode == 7) //Less than
      {
        param1 = this.getParameter(paramMode1, 1);
        param2 = this.getParameter(paramMode2, 2);
        if(param1 < param2)
        {
          this.tempData.set(this.getIndex(paramMode3, 3), 1);
        }
        else
        {
          this.tempData.set(this.getIndex(paramMode3, 3), 0);  
        }
        this.currentPos += 4;
      }
      else if(opCode == 8) //Equal to
      {
        param1 = this.getParameter(paramMode1, 1);
        param2 = this.getParameter(paramMode2, 2);
        if(param1 == param2)
        {
          this.tempData.set(this.getIndex(paramMode3, 3), 1);
        }
        else
        {
          this.tempData.set(this.getIndex(paramMode3, 3), 0);
        }
        this.currentPos += 4;
      }
      else if(opCode == 9)
      {
        param1 = this.getParameter(paramMode1, 1);
        this.relativeBase += param1;
        this.currentPos += 2;
      }
      else if(opCode == 99)
      {
        println("Program End");
        break;
      }
      else
      {
        println("Something went wrong");
      }
    }
    return;    
  }
    
}

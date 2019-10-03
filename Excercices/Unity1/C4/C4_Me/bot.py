from random import randrange
def myName():
    return "JAUME"
def column(grid:list, disc:str) -> int:
    positionRow = 0
    discEneCol = 0
    myDisc = 0
    value=0
    for row in range(len(grid)):
        myDisc=0
        dickEneCol=0
        for col in range(len(grid[row])):
            if grid[row][col] == disc :
                if(myDisc>2 and col<8 and isEmptyToTry(col+1,grid)):#Esto detecta mi ficha
                    value=col+1
                elif (myDisc>=2 and col==8 and isEmptyToTry(0,grid)):
                    value=0
                myDisc += 1
            else:
                myDisc=0  
             
            if grid[row][col] != disc :
                discEneCol += 1
                if(discEneCol==3 and col<8 and isEmptyToTry(col+1,grid)):
                    value = col+1
                if discEneCol >=2 and col == 8 and isEmptyToTry(col -2, grid) and  grid[6][6] == "_" :
                    value = col + 1
            else:
                dickEneCol=0
    for col in range(len(grid[6])):
        v = 0;
        if grid[6][col] == 5:
            v += 1
        if col == 8 and v == 8:
            while not isEmptyToTry(value, grid):
                return randrange(0, 9, 1)

    return value

def isEmptyToTry (value:int, grid: list) -> bool:
    if grid[6][value]==-1:
        return False
    return True

       
    


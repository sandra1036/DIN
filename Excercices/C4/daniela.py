import sys, copy, random
  
def column(grid:list, disc:str) -> int:
    return scoreGrid(grid, disc, 4)[1]

def scoreGrid(grid:list, disc:str, level:int) -> list:
    # Check leaf conditions:
    score = scoreFinalGrid(grid)
    if abs(score) == 4:
        return [score, 0]
    col = 0
    leaf = True
    while leaf and col <= 8:
        leaf = grid[6][col] == -1
        col += 1
    if leaf or level == 0:
        return [score,0]

    if disc == "@":
        score = -4
    else:
        score = +4
    #values = []
    column = -1
    for col in range(0, 9):
        if grid[6][col] >= 0:
            auxCol = col
            gridCopy = copy.deepcopy(grid)
            if disc == "@":
                gridCopy[gridCopy[6][col]][col] = "@"
                gridCopy[6][col] -= 1
                temp = scoreGrid(gridCopy, "#", level - 1)
                #values.append(temp[0])
                if temp[0] > score:
                    score = temp[0]
                    column = col
            else:
                gridCopy[gridCopy[6][col]][col] = "#"
                gridCopy[6][col] -= 1
                temp = scoreGrid(gridCopy, "@", level - 1)
                #values.append(temp[0])
                if temp[0] < score:
                    score = temp[0]
                    column = col
    #print("-"*(5-level)*2,"LEVEL:",level,"MODO:",disc)
    #print("-"*(5-level)*2,values,"-->",score,column)
    if column == -1:
        column = auxCol
    return [score,column]

def scoreFinalGrid(grid:[]) -> int:
    # Horizontal segments
    # Find highest row
    upperRow = 6
    for col in range(0, 8 + 1):
        if grid[6][col] + 1 < upperRow:
            upperRow = grid[6][col] + 1
    maxAbsScore = 0
    score = 0
    if upperRow < 6:
        allRows = list(range(upperRow, 5 + 1))
        random.shuffle(allRows)
        for row in allRows:
            allCols = list(range(0, 8 - 3 + 1))
            random.shuffle(allCols)
            for col in allCols:  
                leftLimit = col
                rightLimit = col + 3
                upperLimit = row
                lowerLimit = row
                temp = scoreSegment(grid, leftLimit, upperLimit, rightLimit, lowerLimit)
                absScore = abs(temp)
                if absScore == 4:
                    return temp
                if absScore > maxAbsScore:
                    score = temp
                    maxAbsScore = absScore
    allCols = list(range(0, 8 - 3 + 1))
    random.shuffle(allCols)
    for col in allCols:
        allRows = list(range (0, 5 - 3 + 1))
        random.shuffle(allRows)
        for row in allRows:
            leftLimit = col
            rightLimit = col + 3
            upperLimit = row
            lowerLimit = row + 3
            temp = scoreSegment(grid, leftLimit, upperLimit, rightLimit, lowerLimit)
            absScore = abs(temp)
            if absScore == 4:
                return temp
            if absScore > maxAbsScore:
                score = temp
                maxAbsScore = absScore
    allCols = list(range(0, 8 - 3 + 1))
    random.shuffle(allCols)
    for col in allCols:
        allRows = list(range (0 + 3, 5 + 1))
        random.shuffle(allRows)
        for row in allRows:
            leftLimit = col
            rightLimit = col + 3
            upperLimit = row - 3
            lowerLimit = row
            temp = scoreSegment(grid, leftLimit, lowerLimit, rightLimit, lowerLimit)
            absScore = abs(temp)
            if absScore == 4:
                return temp
            if absScore > maxAbsScore:
                score = temp
                maxAbsScore = absScore
    return score


def scoreSegment(grid:list, col0:int, row0:int, col1:int, row1:int)->int:
    """ four cells segments are analised here
        a blocking disc is a disc of the oponent
        the segment is analised from coordinates (col0,row0) to (col1, row1)
    """
    patterns = {"@___":0.25,"_@__":0.25,"__@_":0.25,"___@":0.25,\
                "@@__":1.5,"@_@_":1.5,"@__@":1.5,"_@_@":1.5,"__@@":1.5,\
                "@@@_":3,"@@_@":3,"@_@@":3,"_@@@":3,\
                "@@@@":4,\
                "#___":-0.25,"_#__":-0.25,"__#_":-0.25,"___#":-0.25,\
                "##__":-1.5,"#_#_":-1.5,"#__#":-1.5,"_#_#":-1.5,"__##":-1.5,\
                "###_":-3,"##_#":-3,"#_##":-3,"_###":-3,\
                "####":-4}          
    col = col0
    row = row0
    colInc=0
    rowInc=0
    if col0 < col1:
        colInc = 1
    elif col0 > col1:
        colInc = -1
    else:
        colInc = 0
    if row0 < row1:
        rowInc = 1
    elif row0 > row1:
        rowInc = -1
    else:
        rowInc = 0
    segment = ""
    nCells = 1
    #print(col0, row0, col1, row1)
    while nCells <= 4:
        #print(segment)
        segment += grid[row][col]
        if col != col1:
            col += colInc
        if row != row1:
            row += rowInc
        nCells += 1
    return patterns.get(segment,0)

def printGrid(grid, level):
    tc = range(9)
    tr = range(6)
    for r in tr:
        sys.stdout.write(" "*level)
        for c in tc:
            sys.stdout.write("|"+grid[r][c])
        sys.stdout.write("|"+str(r))
        print()
    print (" "*level+" 0 1 2 3 4 5 6 7 8 ")

if __name__ == "__main__":
    print("soy main")
    gridTest01 =    [['_', '_', '_', '_', '_', '_', '_', '_', '_'], #0
                     ['_', '_', '_', '_', '_', '_', '_', '_', '_'], #1
                     ['_', '_', '_', '_', '_', '_', '_', '_', '_'], #2
                     ['_', '_', '_', '_', '_', '_', '_', '_', '_'], #3
                     ['_', '_', '_', '_', '_', '_', '_', '_', '_'], #4
                     ['_', '_', '_', '_', '#', '_', '_', '_', '_'], #5
                     [ 5,   5,   5,   5,   4,   5,   5,   5,   5]]  #6
                     # 0    1    2    3    4    5    6    7    8
    gridTest02 =    [['_', '_', '_', '_', '_', '_', '_', '@', '@'], #0
                     ['_', '_', '_', '_', '_', '_', '@', '@', '@'], #1
                     ['_', '_', '_', '_', '_', '_', '@', '@', '@'], #2
                     ['_', '_', '_', '_', '_', '_', '#', '#', '#'], #3
                     ['_', '_', '_', '_', '_', '#', '@', '@', '@'], #4
                     ['@', '@', '_', '_', '_', '@', '#', '#', '#'], #5
                     [ 4,   4,   5,   5,   5,   3,   0,  -1,  -1]]  #6
                     # 0    1    2    3    4    5    6    7    8
    gridTest03 =    [['_', '_', '_', '_', '_', '_', '@', '@', '@'], #0
                     ['_', '_', '_', '_', '_', '_', '#', '#', '#'], #1
                     ['_', '_', '_', '_', '_', '_', '@', '@', '@'], #2
                     ['_', '_', '_', '_', '_', '_', '#', '#', '#'], #3
                     ['_', '_', '_', '_', '_', '_', '@', '@', '@'], #4
                     ['@', '@', '_', '_', '_', '_', '#', '#', '#'], #5
                     [ 4,   4,   5,   5,   5,   5,   -1,  -1,  -1]] #6
                     # 0    1    2    3    4    5    6    7    8
    gridTest04 =    [['_', '_', '_', '_', '_', '_', '_', '@', '@'], #0
                     ['_', '_', '_', '_', '_', '_', '#', '#', '#'], #1
                     ['_', '_', '_', '_', '_', '_', '@', '@', '@'], #2
                     ['_', '_', '_', '_', '_', '_', '#', '#', '#'], #3
                     ['_', '_', '_', '_', '_', '_', '@', '@', '@'], #4
                     ['@', '@', '_', '_', '_', '_', '#', '#', '#'], #5
                     [ 4,   4,   5,   5,   5,   5,   0,  -1,  -1]]  #6
                     # 0    1    2    3    4    5    6    7    8

    gridTest04 =    [["_","_","_","_","_","_","_","_","_"], #0
                     ["_","_","_","_","_","_","_","_","_"], #1
                     ["_","_","#","#","_","_","_","_","_"], #2
                     ["_","_","@","#","#","_","_","_","_"], #3
                     ["@","@","#","@","#","#","_","_","_"], #4
                     ["@","#","@","#","@","@","_","_","_"], #5
                     [ 3,  3,  1,  1,  2,  3,  5,  5,  5]]  #6
                     # 0   1   2   3   4   5   6   7   8


    print(scoreFinalGrid(gridTest04))
    
                

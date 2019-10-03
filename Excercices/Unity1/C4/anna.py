from random import randrange
import sys

PLAYER1=0
PLAYER2=1

def scoreFinalGrid(grid:[]) -> int:
    score=0
    for column in range(0,9):
        score += scoreColumn(grid, column)
    return score

def scoreColumn(grid:[], column:int) -> int:
    value = 0
    # 4 disc radio circle
    # 0 degrees
    leftLimit = column
    rightLimit = column + 3
    upperLimit = grid[6][column] + 1
    lowerLimit = grid[6][column] + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("4 disc radio, 0 degrees")
        value += scoreSegment(grid, leftLimit, lowerLimit, rightLimit, upperLimit)
    # 45 degrees
    leftLimit = column
    rightLimit = column + 3
    upperLimit = grid[6][column] + 1 - 3
    lowerLimit = grid[6][column] + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("4 disc radio, 45 degrees")
        value += scoreSegment(grid, leftLimit, lowerLimit, rightLimit, upperLimit)
    # 90 degrees
    leftLimit = column
    rightLimit = column
    upperLimit = grid[6][column] + 1 - 3
    lowerLimit = grid[6][column] + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("4 disc radio, 90 degrees")
        value += scoreSegment(grid, leftLimit, lowerLimit, rightLimit, upperLimit)
    # 135 degrees
    leftLimit = column - 3
    rightLimit = column
    upperLimit = grid[6][column] + 1 - 3
    lowerLimit = grid[6][column] + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("4 disc radio, 135 degrees")
        value += scoreSegment(grid, rightLimit, lowerLimit, leftLimit, upperLimit)
    # 180 degrees
    leftLimit = column - 3
    rightLimit = column
    upperLimit = grid[6][column] + 1
    lowerLimit = grid[6][column] + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("4 disc radio, 180 degrees")
        value += scoreSegment(grid, rightLimit, lowerLimit, leftLimit, upperLimit)
    # 225 degrees
    leftLimit = column - 3
    rightLimit = column
    upperLimit = grid[6][column] + 1
    lowerLimit = grid[6][column] + 1 + 3
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("4 disc radio, 255 degrees")
        value += scoreSegment(grid, rightLimit, upperLimit, leftLimit, lowerLimit)
    # 270 degrees
    leftLimit = column
    rightLimit = column
    upperLimit = grid[6][column] + 1
    lowerLimit = grid[6][column] + 1 + 3
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("4 disc radio, 270 degrees")
        value += scoreSegment(grid, rightLimit, upperLimit, leftLimit, lowerLimit)
    # 315 degrees
    leftLimit = column
    rightLimit = column + 3
    upperLimit = grid[6][column] + 1
    lowerLimit = grid[6][column] + 1 + 3
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("4 disc radio, 270 degrees")
        value += scoreSegment(grid, leftLimit, upperLimit, rightLimit, lowerLimit)
    # 3 disc radio circle
    # 0 degrees
    leftLimit = column -1
    rightLimit = column + 3 -1
    upperLimit = grid[6][column] + 1
    lowerLimit = grid[6][column] + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("3 disc radio, 0 degrees")
        value += scoreSegment(grid, leftLimit, lowerLimit, rightLimit, upperLimit)
    # 45 degrees
    leftLimit = column - 1
    rightLimit = column + 3 - 1
    upperLimit = grid[6][column] + 1 - 3 + 1
    lowerLimit = grid[6][column] + 1 + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("3 disc radio, 45 degrees")
        value += scoreSegment(grid, leftLimit, lowerLimit, rightLimit, upperLimit)
    # 90 degrees
    leftLimit = column
    rightLimit = column
    upperLimit = grid[6][column] + 1 - 3 + 1
    lowerLimit = grid[6][column] + 1 + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("3 disc radio, 90 degrees")
        value += scoreSegment(grid, leftLimit, lowerLimit, rightLimit, upperLimit)
    # 135 degrees
    leftLimit = column - 3 + 1
    rightLimit = column + 1
    upperLimit = grid[6][column] + 1 - 3 + 1
    lowerLimit = grid[6][column] + 1 + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("3 disc radio, 135 degrees")
        value += scoreSegment(grid, rightLimit, lowerLimit, leftLimit, upperLimit)
    # 180 degrees
    leftLimit = column - 3 + 1
    rightLimit = column + 1
    upperLimit = grid[6][column] + 1
    lowerLimit = grid[6][column] + 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("3 disc radio, 180 degrees")
        value += scoreSegment(grid, rightLimit, lowerLimit, leftLimit, upperLimit)
    # 225 degrees
    leftLimit = column - 3 + 1
    rightLimit = column + 1
    upperLimit = grid[6][column] + 1 - 1
    lowerLimit = grid[6][column] + 1 + 3 - 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("3 disc radio, 225 degrees")
        value += scoreSegment(grid, rightLimit, upperLimit, leftLimit, lowerLimit)
    # 270 degrees
    leftLimit = column
    rightLimit = column
    upperLimit = grid[6][column] + 1 - 1
    lowerLimit = grid[6][column] + 1 + 3 - 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("3 disc radio, 270 degrees")
        value += scoreSegment(grid, rightLimit, upperLimit, leftLimit, lowerLimit)
    # 315 degrees
    leftLimit = column - 1
    rightLimit = column + 3 - 1
    upperLimit = grid[6][column] + 1 - 1
    lowerLimit = grid[6][column] + 1 + 3 - 1
    if leftLimit >= 0 and rightLimit <= 8 and upperLimit >= 0 and lowerLimit <= 5:
        print("3 disc radio, 315 degrees")
        value += scoreSegment(grid, leftLimit, upperLimit, rightLimit, lowerLimit)
    return value

def scoreSegment(grid:[], col0:int, row0:int, col1:int, row1:int)->int:
    player1Counter = 0
    player2Counter = 0
    col = col0
    row = row0
    colInc=0
    rowInc=0
    if col0<col1:
        colInc=1
    else:
        colInc=-1
    if row0<row1:
        rowInc=1
    else:
        rowInc=-1
    nCells = 0
    while nCells < 4:
        print("   row:{0} col:{1}".format(row,col))
        if grid[row][col] == "@":
            player1Counter +=2
        elif grid[row][col] == "#":
            player2Counter -= 2
        if col != col1:
            col += colInc
        if row != row1:
            row += rowInc
        nCells += 1
    if player1Counter == 8:
        player1Counter *=10
    if player2Counter == 8:
        player2Counter *=10
    print("     ",player1Counter + player2Counter)
    return player1Counter + player2Counter
    
def scoreGrid(grid:[], player:int, level:int) -> int:
    score = 0
    if level == 0:
        printGrid(grid)
        score = scoreFinalGrid(grid)
    else:
        if player == PLAYER1:
            score = -1000
        else:
            score = +1000
        for col in range(0,9):
            if grid[6][col] >= 0:
                gridCopy = grid[:]
                if player == PLAYER1:
                    gridCopy[gridCopy[6][col]][col] = "@"
                    gridCopy[6][col] -= 1
                    score = max(score, scoreGrid(gridCopy, PLAYER2, level-1))
                else:
                    gridCopy[gridCopy[6][col]][col] = "#"
                    gridCopy[6][col] -= 1
                    score = min(score, scoreGrid(gridCopy, PLAYER1, level-1))
    return score
   
def column(grid:list, disc:str) -> int:
    if disc = "@":
        player == PLAYER1
        score = -1000
    else:
        player == PLAYER2
        score = +1000
    for col in range(0, 9):
        if grid[6][col] >= 0:
            gridCopy = grid[:]
            if player == PLAYER1:
                gridCopy[gridCopy[6][col]][col] = "@"
                gridCopy[6][col] -= 1
                temp = scoreGrid(gridCopy, PLAYER2, level - 1)
                if temp > score:
                    score = temp
                    column = col
            else:
                gridCopy[gridCopy[6][col]][col] = "#"
                gridCopy[6][col] -= 1
                temp = scoreGrid(gridCopy, PLAYER1, level - 1)
                if temp < score:
                    score = temp
                    column = col

def printGrid(grid):
	tc = range(9)
	tr = range(6)
	for r in tr:
		for c in tc:
			sys.stdout.write("|"+grid[r][c])
		sys.stdout.write("|"+str(r))
		print()
	print (" 0 1 2 3 4 5 6 7 8 ")
	
if __name__ == "__main__":
    print("soy main")
    gridTest = [['_', '_', '_', '_', '_', '_', '_', '_', '_'], #0
                ['_', '_', '_', '_', '@', '_', '_', '_', '_'], #1
                ['_', '_', '_', '_', '@', '_', '_', '_', '_'], #2
                ['_', '_', '_', '_', '@', '_', '_', '_', '_'], #3
                ['_', '_', '_', '_', '@', '_', '_', '_', '_'], #4
                ['_', '_', '_', '_', '#', '_', '_', '_', '_'], #5
                [ 5,   5,   5,   5,   0,   5,   5,   5,   5]]  #6
                # 0    1    2    3    4    5    6    7    8
    
    print(scoreGrid(gridTest,1,1))
                

from random import randrange

def myName():
    return "Player"


def column(grid:list, disc:str) -> int:
   # for row in range(len(grid)):
   #     print(grid[row])

    x = randrange(0, 9, 2)
    if (grid[6][x] >= 0):
        return x
    else:
        if (x == 0):
            return x + 1

        elif (x == 8):

            return x - 1

        return winner(grid,disc, x)





def winner(grid:list,disc:str, x:int)-> int:

    for row in range(len(grid)):
      if  row != disc and disc != "_":

          return randrange(0,9,1)

    for col in range(len(grid)):
        for row in randrange(len(grid[col])):

            if col !=disc and disc !="_":

                return randrange(0,9,1)

            elif row !=disc and disc !="_":

                return randrange(0,9,1)



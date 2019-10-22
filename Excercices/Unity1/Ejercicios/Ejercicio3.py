"""
Python’s set objects have a method called pop that removes and returns an
arbitrary element from the set. If the set gerbils contains five cuddly little ani-
mals, for example, calling gerbils.pop() five times will return those animals one
by one, leaving the set empty at the end. Use this to write a function called
mating_pairs that takes two equal-sized sets called males and females as input and
returns a set of pairs; each pair must be a tuple containing one male and one
female. (The elements of males and females may be strings containing gerbil
names or gerbil ID numbers—your function must work with both.)
"""
males={"Eustaquio","Pablo","Jack","Rengo"}
famales={"Eduarda","Blanca","Estella","Esmeralda"}
resul=set()
def mating_pairs (males:set,famales:set)-> set:

     for i in range(len(males)):

        resul.add((males.pop(),famales.pop()))

     return resul
if __name__=="__main__":
    print(mating_pairs(males,famales))
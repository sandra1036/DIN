""" Implement a set data structure using a list of lists. The set will storage names using a hash function to correspond a name to an integer number in the range [0,9].

The two functions to implement are:
put(S:your set, element:str)
is(S:your set, element:str) -> bool """

S=[[],[],[],[],[],[],[],[],[],[]]

def put(S:list, name:str):
    bucket=0;
    for bucket in range(len(name)):
        bucket +=ord(name[bucket])
    bucket =bucket % 10
    S[bucket].append(name)
    return 0

def isin(S:list,name:str):
    bucket=0;
    #name letter for letter
    for bucket in range(len(name)):
        bucket +=ord(name[bucket])
        print(bucket)
    bucket= bucket % 10
    index=len(S[bucket]) -1
    while index >=0:
        if S[bucket][index]==name:
            return True
        index -=1
    return False
def remov(S:list,name:str) :



if __name__=="__main__":
     put(S,"juan")
     print(S)
     print(isin(S,"juan"))
     put(S,"Hannah")
     print(S)
     print(isin(S,"Pedro"))
     put(S,"El Monagillo")
     print(S)
     print(isin(S,"El Monagillo"))


















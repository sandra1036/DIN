""" Write a function called find_dups that takes a list of integers as its input argument and returns a set of those
    integers occurring two or more times in the list
"""

list_int=[1,2,4,9,8,4,3,7,9,11]
def find_dups (list_int:list)-> set:

    listR=[]
    for i in range(len(list_int)) :
            if list_int.count(list_int[i])>=2:
                if list_int[i] not in listR:
                    listR.append(list_int[i])
    return listR

if __name__=="__main__":
   print(find_dups(list_int))
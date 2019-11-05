#miran si el numero esta en la misma lista
dict1={'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}}
dict2={'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 1: 'd'}}
def db_consistent(dict_of_dict):
 """ (dict of dict) -> set
 Return whether all inner dictionaries in dict_of_dict contain the same
keys.
 >>> db_consistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
 False
 >>> db_consistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 1: 'd'}})
 True
 """
 inner_keys_list = []
 # Build a list of list of keys
 for key in dict_of_dict:
    inner_keys = list(dict_of_dict[key].keys())
    inner_keys.sort()
    inner_keys_list.append(inner_keys)
 for i in range(1, len(inner_keys_list)):
    # If the number of keys is different.
    if len(inner_keys_list[0]) != len(inner_keys_list[i]):
     return False
    # If the keys don't match.
    for j in range(len(inner_keys_list[0])):
        if inner_keys_list[0][j] != inner_keys_list[i][j]:
            return False
    return True

if __name__ == "__main__":

     print("Resultado1: ", db_consistent(dict1))
     print("Resultado2: ", db_consistent(dict2))
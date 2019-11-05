dict1={'a': 1, 'b': 2, 'c': 3}
dict2= {'a': 1, 'd': 2, 'b': 2}
#Te saca lo que esta común en los dos diccionarios

def dict_interest(dict1, dict2):
 """ (dict, dict) -> dict
 Return a new dictionary that contains only the key/value pairs that occur
 in both dict1 and dict2.
 >>> dict_interest({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'd': 2, 'b': 2})
 {'a': 1, 'b': 2}
 """
 intersection = {}
 for (key, value) in dict1.items():
    if key in dict2 and value == dict2[key]:
         intersection[key] = value
 return intersection

if __name__=="__main__":
    print(dict_interest(dict1,dict2))
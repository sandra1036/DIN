dict_of_dict={'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}}
def db_headings(dict_of_dict)->set:
 inner_keys = set()
 for key in dict_of_dict:
        print("key",key)
        for inner_key in dict_of_dict[key]:
            print("     inner_key",inner_key,"\n")
            inner_keys.add(inner_key)
 return inner_keys

if __name__=="__main__":
    print("Resultado: ",db_headings(dict_of_dict))
#cuenta los duplicados del diccionario
dictionary={'R': 1, 'G': 2, 'B': 2, 'Y': 1, 'P': 3}
def count_duplicates(dictionary):
 """ (dic) -> int
 Return the number of duplicate values in dictionary.
 >>> count_duplicates({'R': 1, 'G': 2, 'B': 2, 'Y': 1, 'P': 3})
 2
 """
 duplicates = 0
 values = list(dictionary.values())
 for item in values:
 # if an item appears at least 2 times, it is a duplicate
    if values.count(item) >= 2:
        duplicates = duplicates + 1
        # remove that item from the list
        num_occurrences = values.count(item)
        for i in range(num_occurrences):
            values.remove(item)
 return duplicates

if __name__=="__main__":
    print(count_duplicates(dictionary))
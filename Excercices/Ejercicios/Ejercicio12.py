dict1={1: 3, 3: 4}
dict2={2: 4, 3: 5, 5: 6}
#a.
def sparse_add(vector1, vector2):
 """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})
 Return the sum of sparse vectors vector1 and vector2.
 >>> sparse_add({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
 {1: 3, 2: 4, 3: 9, 5: 6}
 """
 sum_vector = vector1.copy()
 for key in vector2:
    if key in sum_vector:
        sum_vector[key] = sum_vector[key] + vector2[key]
    else:
         sum_vector[key] = vector2[key]
 return sum_vector
#b.
def sparse_dot(vector1, vector2):
 """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})
 Return the dot product of sparse vectors vector1 and vector2.
 >>> sparse_dot({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
 20
 """
 dot = 0
 for key1 in vector1:
    if key1 in vector2:
        dot = dot + vector1[key1] * vector2[key1]
 return dot

#c.
#Since only non-zero entries are stored, will the last entry always be nonzero? If not, how will the last entry be represented in the dictionary?
if __name__ == "__main__":

     print("Resultado A: ", sparse_add(dict1,dict2))
    # print("Resultado B: ", sparse_dot(dict2))

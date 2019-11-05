""" Calculate the numbers of cuadratic
>>> calculate(1,20,3)
19.697715603592208

>>> calculate(1,25,4)
24.677925358506133


"""


def calculate(n1:float,n2:float,n3:float) -> float:
    import math
    return math.sqrt(math.pow(n2,2)-4*n1*n3)

#print(calculate(1,20,3))

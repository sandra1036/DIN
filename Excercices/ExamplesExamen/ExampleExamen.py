""" Calculate electrical resistivity 
    Precondicion: l not number 0,the three numbers have to be positive and greater than 0

>>> cal(12,32,54)
7.111111111111111
   
>>> cal(1,2,3)     
0.6666666666666666

"""
def cal(r:float,a:float,l:float)-> float :


    result=(r*a)/l
    return result

##print(cal(12,32,54))
#help(cal)

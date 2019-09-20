

""" Calculate the volume of cone
	
	h= height the cone 
	R= the Radius of the cone the bass down 
	r= the Radius of the cone the bass up

       Preconditions: lenght must be number 0,the three numbers have to be positive and greater 	than 0

	>>> calV(10,20)
	6283.185307179587

        >>> calV(5,2)
	366.51914291880917


	>>> calV(8,10)
	2555.1620249196985

"""
def calV(r: float , h: float , R: float=10) -> float :
	import math
	volume= h*math.pi/3*(R**2+r**2+R*r)

	return volume

#print(calV(-9,10))








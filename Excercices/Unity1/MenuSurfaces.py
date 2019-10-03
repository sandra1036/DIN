import math

def square() -> float:
   l=float(input("number side: "))
   result=l*l
   return result
   print(result)

def triangle() -> float:
   h=float(input("Number height:"))
   b=float(input("Number base:"))
   result=(h*b)/2
   return result
   print(result)

def circle()-> float:

   r=float(input("Number radius:"))
   result=math.pi*r**2
   return result
   print(result)


if _name_=="_main_" :
    print("1-Square\n 2-triangle\n3-circle")
    op=int(input("number option: "))
   while(op<=0 or op>3):
	












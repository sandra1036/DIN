from math import pi
def surfaceSquare(l:float)->float:
    return l**2
def surfaceCircle(r:float)->float:
    return pi*(r**2)
def surfaceTriangle(b:float,h:float)->float:
    return (b*h)/2

if __name__=="__main__":
    print("1-Surface Square \n2-Surface Circle \n3-Surface Triangle \n")
    option=0
    while(option <=0 or option>3):
        option=int(input("Input an option: "))
        if(option==1):
            value=float(input("Introduce data: "))
            print(surfaceSquare(value))
        elif(option==2):
            value=float(input("Introduce radius: "))
            print(surfaceCircle(value))
        elif(option==3):
            value=float(input("Introduce base: "))
            value2=float(input("Introduce alture: "))
            print(surfaceTriangle(value,value2))
        else:
            print("Invalid Option")

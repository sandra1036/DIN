import math
def cal(r: float, f: float, g: float=90) -> float:

    """ Calculate the force the thorque

    r: magnitud of the torque
    f: the force
    g: degrees

    parameters: 
    
    the angle is in degrees

    >>> cal(10,4)
    2.4492935982947065e-15

    >>> cal(5,3)
    9.18485099360515e-16


    >>> cal(0,1)
    0.0
 

    """
    t=r*f*math.cos(math.radians(g))
    return t

print(cal(0,1))




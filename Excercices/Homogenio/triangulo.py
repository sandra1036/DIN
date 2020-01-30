from tkinter import *
import numpy as n

def homogenio(coord:list):
    for i in range(len(coord)):
        coord[i].append(1)
    return coord

def deshomogenio(coord:list):
    for i in range(len(coord)):
        coord[i][0]=coord[i][0]/coord[i][2]
        coord[i][1]=coord[i][1]/coord[i][2]
        del coord[i][2]

def traslacion(tx:float,ty:float):
        return ([1,0,0],[0,1,0],[tx,ty,1])

def rotation(gra:float):
    rad=n.radians(gra)
    return [[n.cos(rad),n.sin(rad),0],[-n.sin(rad),n.cos(rad),0],[0,0,1]]


window=Tk()
canvas=Canvas(window)
canvas.grid(column=0,row=0,sticky=NSEW)
canvas.configure(background="green")
triangle=[[25,50],[30,75],[50,25]]
canvas.create_polygon(triangle,fill="black")
homogenio(triangle)
print(triangle)
print(traslacion(50,50))
print(rotation(30))
triangle2=list()
trans=traslacion(0,0)
topos=traslacion(100,50)
rotation=rotation(25)
transform=n.dot(trans,rotation)
transform=n.dot(transform,topos)
for i in range(len(triangle)):
    triangle2.append(n.dot(triangle[i],transform).tolist())
deshomogenio(triangle2)
canvas.create_polygon(triangle2,fill="black")





window.update()
window.minsize(350,250)
window.mainloop()



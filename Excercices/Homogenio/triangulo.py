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
        return n.array([1,0,0],[0,1,0],[tx,ty,1])

def rotation(gra:float):
    rad=n.radians(gra)
    return [[n.cos(rad),n.sin(rad),0],[-n.sin(rad),n.cos(rad),0],[0,0,1]]

window=Tk()
canvas=Canvas(window)
canvas.grid(column=0,row=0,sticky=NSEW)
canvas.configure(background="green")
points=[[25,50],[30,75],[50,25]]
triangle=canvas.create_polygon(points,fill="black")

print(points)
homogenio(points)
print(points)
print(rotation(30))
print(traslacion(50,50))

window.update()
window.minsize(350,250)
window.mainloop()



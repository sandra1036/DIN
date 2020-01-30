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
canvas.pack()
traingle=([25,50],[60,75],[60,25])
canvas.create_polygon(traingle)
homogenio(traingle)
traingle2=list()
trasladar = traslacion(-25,-50)
rotar = rotation(180)
trasladar2 = traslacion(100,50)
transformado = n.dot(trasladar,rotar)#Lo lleva al origen lo rota
transformado2=n.dot(transformado,trasladar2) #lo lleva al sitio que quieras

#Pasa por todos los puntos del triangulo
for i  in range(len(traingle)):
    traingle2.append(n.dot(traingle[i],transformado2).tolist())

deshomogenio(traingle2)
canvas.create_polygon(traingle2)






window.mainloop()



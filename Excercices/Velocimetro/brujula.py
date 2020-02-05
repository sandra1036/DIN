from tkinter import *
import numpy as np


def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)


def homogenize(coords: list):
    for i in range(len(coords)):
        coords[i].append(1)


def dehomogenize(coords: list):
    for i in range(len(coords)):
        coords[i][0] = coords[i][0] / coords[i][2]
        coords[i][1] = coords[i][1] / coords[i][2]
        del coords[i][2]

def gettranslation(tx:float, ty:float)->list:
    return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

def getrotation(deg:float)->list:
    rad = np.radians(deg)
    return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]





window=Tk()
canvas=Canvas(window,width=500,height=500)
canvas.pack()

canvas.create_oval(150-140,150-140,350+140,350+140,fill="white")
canvas.create_oval(150-120,150-120,350+120,350+120, fill="black")

point=[[-200, 0],[-160, 0]]


homogenize(point)
torig=gettranslation(250,250)
#El primer num es donde empieda la linea y la inclinacion y el 2 hasta donde quieres que llegen
for rot in range(0,360,90):
    rotation = getrotation(rot)
    transform = np.dot(rotation, torig)
    temp = list()
    for i in range(len(point)):
        temp.append(np.dot(point[i], transform).tolist())
    dehomogenize(temp)
    canvas.create_line(temp,fill="white",width=4)

point=[[-190, 0],[-160, 0]]
to=gettranslation(260,230)
homogenize(point)
coordenadas='WNES'
z=0
for rot in range(0,360,90):
    rotation = getrotation(rot)
    transform = np.dot(rotation, to)
    temp = list()
    temp.append(np.dot(point[0],transform).tolist())
    dehomogenize(temp)
    canvas.create_text(temp, text=str(coordenadas[z]),fill="white")
    print(coordenadas)
    z = z + 1






canvas.bind("<Button-1>", lambda e:print(e.x,e.y))

window.update()
window.minsize(500,500)
window.mainloop()
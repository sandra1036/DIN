from tkinter import *
from tkinter import ttk
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

#Lo usa en una clase a parte donde lo llama desde ahi
def getscaled(self, xscl:float, yscl:float) -> list:
    return [[xscl, 0, 0], [0, yscl, 0], [0, 0, 1]]



window=Tk()
canvas=Canvas(window)
canvas.pack()

# Crea un Texto
# canvas.create_text(100,10,fill="darkblue",font="Times 20 italic bold",
#                         text="Label")

canvas.create_oval(173-2,214-2,194+2,232+2,fill="black")
canvas.create_oval(173,214,194,232,fill="red")
canvas.create_polygon(12,233,198,218,199,230,12,233,fill="red",outline="black",outlineoffset=1)

#la segunda parte agranda las lineas en x(cuanto menos negativo mas grandes son) y las rota en las y
pointl=[[-190, 0],[-170, 0]]
homogenize(pointl)
to = gettranslation(190,200)

#El - es el angulo en negativo fuera del canvas el 2 se mueve hacia la izquierda, y el ultimo parametro es la distancia entre las lineas
#Crea lineas del angulo -10 al 180 si pones mas que esto se crearan mas lineas
for rot in range(-10,194,14):
    rotation = getrotation(rot)
    trasladar = np.dot(rotation,to)
    #Poner la lista dentro si lo pones fuera no funciona
    linelist=list()
    for i in range(len(pointl)):
        linelist.append(np.dot(pointl[i],trasladar).tolist())
    dehomogenize(linelist)
    canvas.create_line(linelist)

#Crea los strings

#Strings
pos = [[-150, 0]]
homogenize(pos)
to = gettranslation(190,200)
vel = 0
for rot in range(-10,194,14):
    rotation = getrotation(rot)
    transform = np.dot(rotation, to)
    temp = list()
    temp.append(np.dot(pos[0],transform).tolist())
    dehomogenize(temp)
    canvas.create_text(temp, text=str(vel))
    vel = vel + 20

short = [[-180, 0],[-170, 0]]
homogenize(short)
toorig = gettranslation(190,200)
#Lineas intermedias
for rot in range(-10,190,7):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = list()
    for i in range(len(short)):
        temp.append(np.dot(short[i],transform).tolist())
    dehomogenize(temp)
    canvas.create_line(temp)



canvas.bind("<Button-1>", lambda e:print(e.x,e.y))

window.update()
window.minsize(500,350)
window.mainloop()
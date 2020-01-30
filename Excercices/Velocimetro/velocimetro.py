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
canvas=Canvas(window)
canvas.pack()
point=[10, 60, 350, 400]
canvas.create_arc(point,start=0,extent=180)
pointl=[[35,217],[60,217]]
canvas.create_line(pointl)
canvas.create_oval(173-2,214-2,194+2,232+2,fill="black")
canvas.create_oval(173,214,194,232,fill="red")
canvas.create_polygon(45,214,199,219,195,229,44,215,fill="red",outline="black",outlineoffset=1)

homogenize(pointl)
linelist=list()
to=gettranslation(-48,50)
rotation=getrotation(20)
trasladar=np.dot(to,rotation)
trasladar2=np.dot(trasladar,to)
for i in range(len(pointl)):
    linelist.append(np.dot(point[i],trasladar).tolist())

dehomogenize(linelist)
canvas.create_line(point)


canvas.bind("<Button-1>", lambda e:print(e.x,e.y))
window.mainloop()
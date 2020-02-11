from tkinter import *
from tkinter import ttk
import numpy as np

#Todo lo que que estaba escrito en el canvas pones un self
class Brujula(Canvas):

    def xy(self,event):
        global lastx, lasty
        lastx, lasty = self.canvasx(event.x), self.canvasy(event.y)

    def homogenize(self,coords: list):
        for i in range(len(coords)):
            coords[i].append(1)

    def dehomogenize(self,coords: list):
        for i in range(len(coords)):
            coords[i][0] = coords[i][0] / coords[i][2]
            coords[i][1] = coords[i][1] / coords[i][2]
            del coords[i][2]

    def gettranslation(self,tx: float, ty: float) -> list:
        return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

    def getrotation(self,deg: float) -> list:
        rad = np.radians(deg)
        return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]

    def __init__(self,master=NONE,**options):
        super().__init__(master, options)
        self.w0=400
        self.h0=400

        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))

        self.create_oval(150-140,150-140,350+140,350+140,fill="white")
        self.create_oval(150-120,150-120,350+120,350+120, fill="black")

        point=[[-200, 0],[-160, 0]]


        self.homogenize(point)
        torig=self.gettranslation(250,250)
        #El primer num es donde empieda la linea y la inclinacion y el 2 hasta donde quieres que llegen
        for rot in range(0,360,90):
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, torig)
            temp = list()
            for i in range(len(point)):
                temp.append(np.dot(point[i], transform).tolist())
            self.dehomogenize(temp)
            self.create_line(temp,fill="white",width=4)

        point=[[-190, 0],[-160, 0]]
        to=self.gettranslation(260,230)
        self.homogenize(point)
        coordenadas=['W','N','E','S']
        z=0
        for rot in range(0,360,90):
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, to)
            temp = list()
            temp.append(np.dot(point[0],transform).tolist())
            self.dehomogenize(temp)
            self.create_text(temp, text=str(coordenadas[z]),fill="white")
            print(coordenadas[z])
            z = z + 1


        self.create_polygon(250,90,280,230,250,250,220,230,250,90,fill="white",outline="red",width=2)



        self.bind("<Button-1>", lambda e:print(e.x,e.y))

from tkinter import *
from tkinter import ttk


window=Tk()

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
canvasD=Canvas(window,relief=RAISED,scrollregion=(0, 0, 1000, 1000))
canvasD.grid(column=0,row=0,sticky=(N,W,S,E))
canvasD.configure(background="blue")

canvasC=Canvas(window,relief=RAISED)
canvasC.grid(column=0,row=2,sticky=(W, E))
canvasC.configure(background="red")
points = [0, 25, 50,25, 25, 0]
uparrow=canvasC.create_polygon(points,fill="black")

points2=[0, 25, 25,25, 25, 50]
leftarrow=canvasC.create_polygon(points2,fill="black")
canvasC.bind("<Button-1>", lambda e:print(e.x,e.y))
window.update()
window.maxsize(600,500)
window.minsize(400,500)
window.mainloop()
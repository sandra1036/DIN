from tkinter import *
from tkinter import ttk

window=Tk()

frame=ttk.Frame(window)
frame.grid(column=0,row=0)

frameGrid=ttk.Frame(frame)
frameGrid.grid(column=0,row=1)

buttonSet=ttk.Button(frame,text="Set")
buttonSet.grid(column=0,row=2)

for i in range(4):
    checkbuttonwidth=ttk.Checkbutton(frame)
    checkbuttonwidth.grid()





window=mainloop()








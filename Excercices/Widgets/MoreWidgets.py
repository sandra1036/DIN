from tkinter import *
from tkinter import ttk

window=Tk()
frame=ttk.Frame(window)
frame.grid(column=0,row=0)
t=Text(frame,width=50,height=10)
t.grid(column=1,row=1)
b=ttk.Button(frame,text="Button")
b.grid(column=1,row=2)
spvar=StringVar()
sp=Spinbox(frame,textvariable=spvar)
sp["values"]=("lunes","Martes","Miercoles")
sp.grid(column=2,row=2)




window=mainloop()
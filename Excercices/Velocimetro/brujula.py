from tkinter import *
import numpy as np
from Brujula import Brujula
from tkinter import ttk
window=Tk()
frame=ttk.Frame(window)
frame.pack()
br=Brujula(frame,width=500,height=500)
br.grid(column=0,row=0)

window.update()
window.minsize(500,500)
window.mainloop()
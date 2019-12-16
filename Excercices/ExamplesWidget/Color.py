from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox
def colorla(label:ttk.Label):
    color=colorchooser.askcolor(initialcolor='#ff0000')
    print(color)
    if messagebox.askyesno(message='¿Estas seguro?'):
        label["background"] = color[1]




window=Tk()
frame=ttk.Frame(window)
frame.grid(column=0,row=0)
color=StringVar()
label=ttk.Label(frame,relief=SUNKEN,padding=(50,50,60,50))
label.grid(column=0,row=0)
button=ttk.Button(frame,text="Color",command=lambda :colorla(label))
button.grid(column=0,row=1)
window.mainloop()

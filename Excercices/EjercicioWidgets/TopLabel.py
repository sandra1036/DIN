from tkinter import *
from tkinter import ttk

def newWindow():
    new=Toplevel(root)


root=Tk()
ttk.Button(root,text="New window",command=newWindow).pack()
ttk.Button(root,text="Minimize",command=lambda :root.iconify()).pack()
root.geometry("300x200-5+40")
root.minsize(200,100)
root.maxsize(500,500)




root.mainloop()
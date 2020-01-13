from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def newWindow():
    new=Toplevel(root)
    var=StringVar()
    R1=ttk.Radiobutton(new,text="Opcion 1",variable=var,value=1)
    R1.pack()
    R2 = ttk.Radiobutton(new, text="Opcion 2",variable=var,value=2)
    R2.pack()
    R3 = ttk.Radiobutton(new, text="Opcion 3",variable=var,value=3)
    R3.pack()
    var.set(2)#Pone el radiobutton por defecto
    button=ttk.Button(new,text="Destroy",command=lambda :des(new))
    button.pack()
    
def des(new):
    if messagebox.askyesno(message="¿Estás seguro de querer salir?",icon='question',title='Salir'):
        new.destroy()

root=Tk()
ttk.Button(root,text="New window",command=newWindow).pack()
ttk.Button(root,text="Minimize",command=lambda :root.iconify()).pack()
root.geometry("300x200-5+40")
root.minsize(200,100)
root.maxsize(500,500)




root.mainloop()
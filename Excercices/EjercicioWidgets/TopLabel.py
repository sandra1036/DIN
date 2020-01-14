from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def newWindow():
    new=Toplevel(root)
    var=StringVar()
    var.set(style.theme_use())#Pone el radiobutton por defecto

    for t in style.theme_names():
        ttk.Radiobutton(new,text=t,variable=var,value=t,command=lambda : style.theme_use(var.get())).pack(anchor='w')#Coge para cada radiobutton un style diferente
        #command=lambda x=t : s.theme_use(x) se puede poner asi tambien


    button=ttk.Button(new,text="Destroy",command=lambda :close())
    button.pack()

    def close():
        if messagebox.askyesno(message="¿Estás seguro de querer salir?", icon='question', title='Salir'):
            new.destroy()
#def des(new):
 #   if messagebox.askyesno(message="¿Estás seguro de querer salir?",icon='question',title='Salir'):
  #      new.destroy()

root=Tk()
ttk.Button(root,text="New window").pack()
ttk.Button(root,text="Minimize",command=lambda :root.iconify()).pack()
root.geometry("300x200-5+40")
root.minsize(200,100)
root.maxsize(500,500)
style=ttk.Style()

menubar = Menu(root)
menu_nuevo = Menu(menubar)
root['menu'] = menubar #Sin esto no sale
menubar.add_command(label='New',command=lambda :newWindow())



root.mainloop()
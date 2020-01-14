from tkinter import *
from tkinter import ttk
from childw import newWindow


#def des(new):
 #   if messagebox.askyesno(message="¿Estás seguro de querer salir?",icon='question',title='Salir'):
  #      new.destroy()

root=Tk()
ttk.Button(root,text="New window").pack()
ttk.Button(root,text="Minimize",command=lambda :root.iconify()).pack()
root.geometry("300x200-5+40")
root.minsize(200,100)
root.maxsize(500,500)
root.update()

menubar = Menu(root)
menu_nuevo = Menu(menubar)
root['menu'] = menubar #Sin esto no sale
menubar.add_command(label='New',command=lambda :newWindow(root))

root.mainloop()
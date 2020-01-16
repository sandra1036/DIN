from tkinter import *
from tkinter import ttk
from  F2romero_orozco import pref
window=Tk()
window.title("Course is almost done ")
window.geometry("600x400-30+30")

window.option_add('*tearOff', FALSE)

def funcmenuX(checkX,checkY):
    if checkX.get():
        window.update()
        window.maxsize(window.winfo_rootx(),700)

    if checkY.get():
        window.update()
        window.maxsize(700, window.winfo_rooty())

    if checkX.get() and checkY.get():
        window.update()
        window.maxsize(window.winfo_rootx(), 700)
        window.maxsize(window.winfo_rooty(), 1000)

button=ttk.Button(window,text="Minimize Window",command=lambda :window.iconify())
button.pack()

menubar=Menu(window)
menu_window=Menu(menubar)
menubar.add_cascade(menu=menu_window,label="Window")

checkX=StringVar()
checkY=StringVar()

menu_window.add_checkbutton(label="X resizable",variable=checkX,command=lambda : funcmenuX(checkX,checkY))
menu_window.add_checkbutton(label="Y resizable",variable=checkY,command=lambda : funcmenuX(checkX,checkY))
menu_window.add_separator()
menu_window.add_command(label="Close",command=lambda : window.destroy())
window["menu"]=menubar



buttonpre=ttk.Button(text="Prefecences",command=lambda : pref(window)).pack()
window.update()
window.minsize(500,300)
window.maxsize(700,500)
window.mainloop()


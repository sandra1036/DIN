from tkinter import ttk
from tkinter import *

def snbutton(label,button):
    s.theme_use(ChVar.get())
    label["text"]=button["style"]
    button["text"]=button.winfo_class()

window = Tk()
frame=ttk.Frame(window)
frame.pack()
s=ttk.Style()
#Modifica el tema en el que estas para eso necesitas usarlo
s.theme_use('clam')
s.configure('MyButton.TButton', font='helvetica 24',background="white")
s.configure('MyLabel.TLabel',background="red",foreground="blue")
s.configure('TRadiobutton',background="orange",foreground="green",indicatorbackground="yellow")
s.configure('TCheckbutton',background="black",foreground="white")
s.configure('TCombobox',background="purple",foreground="white",fieldbackground ="black")
#s.configure(".",background="yellow")#se aplica a todos los widgets

s.map('MyButton.TButton',
    background=[('disabled','#d9d9d9'), ('active','#ececec')],
    foreground=[('disabled','#a3a3a3'), ('active','#0000cc')],
    relief=[('active', '!disabled', 'sunken')])

#Para cambiar de tema usarlo
s.theme_use('default')
s.configure('MyButton.TButton',font="Arial 57")

#Tiene que ser un map para cada tema que quiero crear

s.map('MyButton.TButton',
    background=[('disabled','#C48B00'), ('active','#C40000')],
    foreground=[('disabled','#a3a3a3'), ('active','#0000cc')],
    relief=[('active', '!disabled', 'sunken')])
s.configure('TFrame',background="orange")
label=ttk.Label(frame,text="Label", style='MyLabel.TLabel')
label.pack()
button=ttk.Button(frame,text="Button",style="MyButton.TButton")
button.pack()
radio=ttk.Radiobutton(frame,text="Radio")
radio.pack()
check=ttk.Checkbutton(frame,text="Check")
check.pack()
ChVar=StringVar()
sel=ttk.Combobox(frame,textvariable=ChVar)
sel.pack()
sel["values"]=s.theme_names()
sel.bind("<<ComboboxSelected>>",lambda e: snbutton(label,button))
window=mainloop()




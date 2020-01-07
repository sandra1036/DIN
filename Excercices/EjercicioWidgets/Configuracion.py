from tkinter import ttk
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
def color(label:ttk.Label):
    col=colorchooser.askcolor(initialcolor='#ff0000')
    if messagebox.askyesno(message='¿Estas seguro?'):
        label["background"] = col[1]

def labels(label:ttk.Label):
    if Nvar.get():
        label.configure(font=("Times New Roman", 12, "bold"))


window=Tk()
window.title("Configuración")
#Frames de fuera
frameC=ttk.Frame(window)
frameC.pack()

#NoteBook
n=ttk.Notebook(frameC)
n.pack()
#Frames del NoteBook
#Frame1
fr1=ttk.Frame(n)
n.add(fr1,text="Ver")
#Checkbox
Nvar=StringVar()
Svar=StringVar()
Ivar=StringVar()
labelV=ttk.Label(fr1,text="Cambiame")
labelV.pack()
checkboxN=ttk.Checkbutton(fr1,text="Negrita",variable=Nvar)
checkboxN.pack()
checkboxS=ttk.Checkbutton(fr1,text="Subrayar",variable=Svar)
checkboxS.pack()
checkboxI=ttk.Checkbutton(fr1,text="Cursiva",variable=IntVar)
checkboxI.pack()
#Frame2
spinboxvar=IntVar()
fr2=ttk.Frame(n)
n.add(fr2,text="Editor")
labelE=ttk.Label(fr2,text="Cambio de tamaño")
labelE.pack()
spinbox=Spinbox(fr2,from_=20.0, to=100.0,textvar=spinboxvar)
spinbox.pack()

#Frame3
col=StringVar()
fr3=ttk.Frame(n)
n.add(fr3,text="Color")
labelC=ttk.Label(fr3,text="Cambio de color")
labelC.pack()

#Button
buttonColor=ttk.Button(fr3,text="Cambiame de color",command=lambda : color(labelC))
buttonColor.pack()

#Frame de Style
frameS=ttk.Frame(window)
frameS.pack()
styles=ttk.Style()
varcom=StringVar()
combobox=ttk.Combobox(frameS,textvariable=varcom)
combobox.pack()
combobox["values"]=styles.theme_names()
combobox.bind("<<ComboboxSelected>>",lambda e: styles.theme_use(varcom.get()))
combobox.set(combobox["values"][0])



window.mainloop()
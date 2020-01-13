from tkinter import ttk
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter.font import Font

window=Tk()
def color(label:ttk.Label):
    col=colorchooser.askcolor(initialcolor='#ff0000')
    if messagebox.askyesno(message='¿Estas seguro?'):
        label["background"] = col[1]

def labels(label):
    styles.theme_use(varcom.get())

    if Nvar.get():
        label.configure(font=('helvetica 11 bold'))
    else:
        label.configure(font=('helvetica 11'))

    if Nvar.get() and Ivar.get():
        label.configure(font=('helvetica 11 bold italic'))

    if Nvar.get() and Svar.get():
        label.configure(font=('helvetica 11 bold underline'))

    if Svar.get():
        label.configure(font=('helvetica 11 underline'))

    if Svar.get() and Ivar.get():
        label.configure(font=('helvetica 11 underline italic'))

    if Ivar.get():
        label.configure(font=('helvetica 11 italic'))

    if Nvar.get() and Ivar.get() and Svar.get():
        label.configure(font=(('helvetica 11 underline bold italic')))




def snbutton():
    styles.theme_use(varcom.get())

def preferences(window):
    windowC=Toplevel(window)
    frameA = ttk.Frame(windowC)
    frameA.pack()

    # Frames de fuera
    frameC = ttk.Frame(windowC)
    frameC.pack()

    # NoteBook
    n = ttk.Notebook(frameC)
    n.pack()
    # Frames del NoteBook
    # Frame1
    fr1 = ttk.Frame(n)
    n.add(fr1, text="Ver")
    # Checkbox

    labelV = ttk.Label(fr1, text="Cambiame", style="")
    labelV.pack()
    checkboxN = ttk.Checkbutton(fr1, text="Negrita", variable=Nvar)
    checkboxN.pack()
    checkboxS = ttk.Checkbutton(fr1, text="Subrayar", variable=Svar)
    checkboxS.pack()
    checkboxI = ttk.Checkbutton(fr1, text="Cursiva", variable=Ivar)
    checkboxI.pack()
    button = ttk.Button(text="Dale", command=lambda: labels(labelV))
    button.pack()
    # Frame2
    spinboxvar = IntVar()
    fr2 = ttk.Frame(n)
    n.add(fr2, text="Editor")
    labelE = ttk.Label(fr2, text="Cambio de tamaño")
    labelE.pack()
    spinbox = Spinbox(fr2, from_=20.0, to=100.0, textvar=spinboxvar)
    spinbox.pack()

    # Frame3
    col = StringVar()
    fr3 = ttk.Frame(n)
    n.add(fr3, text="Color")
    labelC = ttk.Label(fr3, text="Cambio de color")
    labelC.pack()

    # Button
    buttonColor = ttk.Button(fr3, text="Cambiame de color", command=lambda: color(labelC))
    buttonColor.pack()

    # Frame de Style
    frameS = ttk.Frame(windowC)
    frameS.pack()


    # ComboBox

    combobox = ttk.Combobox(frameS, textvariable=varcom)
    combobox.pack()
    combobox["values"] = styles.theme_names()
    combobox.bind("<<ComboboxSelected>>", lambda e: snbutton())
    combobox.set(combobox["values"][0])

    # Styles
    styles.theme_use('clam')
    windowC.mainloop()




window.title("Configuración")
styles = ttk.Style()
Nvar = IntVar()
Svar = IntVar()
Ivar = IntVar()
varcom = StringVar()
#Text
text=Text(window)
text.pack()


#Menu

menubar = Menu(window)
menu_nuevo = Menu(menubar)
menu_conf = Menu(menubar)
window['menu'] = menubar #Sin esto no sale

menubar.add_command(label='Nuevo')
menubar.add_command(label='Configuración', command=lambda :preferences(window))


window.mainloop()
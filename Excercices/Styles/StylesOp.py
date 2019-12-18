from tkinter import ttk
from tkinter import *

window = Tk()
frame=ttk.Frame(window)
frame.pack()
s=ttk.Style()
s.configure('TButton', font='helvetica 24',background="white")
s.configure('TLabel',background="red",foreground="blue")
s.configure('TRadiobutton',background="orange",foreground="green")
s.configure('TCheckbutton',background="black",foreground="white")
s.configure('TCombobox',background="purple",foreground="white")
label=ttk.Label(frame,text="Label")
label.pack()
button=ttk.Button(frame,text="Button")
button.pack()
radio=ttk.Radiobutton(frame,text="Radio")
radio.pack()
check=ttk.Checkbutton(frame,text="Check")
check.pack()
ChVar=StringVar()
sel=ttk.Combobox(frame,textvariable=ChVar)
sel.pack()
sel["values"]=s.theme_names()
sel.bind("<<ComboboxSelected>>",lambda e: s.theme_use(ChVar.get()))
window=mainloop()




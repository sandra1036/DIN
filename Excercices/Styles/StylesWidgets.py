from tkinter import ttk
from tkinter import *

window = Tk()
frame=ttk.Frame(window)
frame.pack()
label=ttk.Label(frame,text="Label")
label.pack()
button=ttk.Button(frame,text="Button")
button.pack()
radio=ttk.Radiobutton(frame,text="Radio")
radio.pack()
check=ttk.Checkbutton(frame,text="Check")
check.pack()
s=ttk.Style()
ChVar=StringVar()
sel=ttk.Combobox(frame,textvariable=ChVar)
sel.pack()
sel["values"]=s.theme_names()
sel.set(sel["values"][0])
sel.bind("<<ComboboxSelected>>",lambda e: s.theme_use(ChVar.get()))
window=mainloop()




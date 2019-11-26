from tkinter import *
from tkinter import ttk

window = Tk()

statebuttons=StringVar()

frame = ttk.Frame(window)
frame.grid(column=0,row=0)
label = ttk.Label(frame, textvar=statebuttons)
label.grid(column=0,row=0)
button=ttk.Button(frame, text="Click")
button.grid(column=1,row=0)

window.bind('<Return>',lambda e:statebuttons.set(button.state()))

window.mainloop()


































from tkinter import *
from tkinter import ttk

window = Tk()

statebuttons=StringVar()
statecheckbutton=StringVar()
measureSystem=StringVar()


def refresh():
    statebuttons.set(button.state())
    statecheckbutton.set(check.state())

frame = ttk.Frame(window)
frame.grid(column=0,row=0)
label = ttk.Label(frame, textvar=statebuttons)
label.grid(column=0,row=0)
button=ttk.Button(frame, text="Click")
button.grid(column=1,row=0)

check=ttk.Checkbutton(frame,variable=measureSystem,onvalue="ON",offvalue="OFF")
check.grid(column=0,row=1)

labelcheck=ttk.Label(frame, text="Status CheckButton",textvar=statecheckbutton)
labelcheck.grid(column=1,row=1)



window.bind('<Return>',lambda e:refresh())

window.mainloop()



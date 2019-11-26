from tkinter import *
from tkinter import ttk

def refreshStates():
    button_state.set(button.state())
    check_state.set(check.state())
    rd1_state.set(rd1.state())
    rd2_state.set(rd2.state())
    rd3_state.set(rd3.state())
    cmb_state.set(cmb.state())

window = Tk()

frame = ttk.Frame(window)
frame.pack()

button_state = StringVar()

btlabel = ttk.Label(frame, textvariable=button_state)
btlabel.grid(row=0, column=1)

button = ttk.Button(frame, text="Set state")
button.grid(row=0, column=0)

check_state = StringVar()

chlabel = ttk.Label(frame, textvariable=check_state)
chlabel.grid(row=1, column=1)

measureSystem = StringVar()
check = ttk.Checkbutton(frame, text='A Check', variable=measureSystem, onvalue='ImOn', offvalue='ImOff')
check.grid(row=1, column=0)

rd1_state = StringVar()
rd2_state = StringVar()
rd3_state = StringVar()

rd1l = ttk.Label(frame, textvariable=rd1_state)
rd1l.grid(row=2, column=1)
rd1l = ttk.Label(frame, textvariable=rd2_state)
rd1l.grid(row=3, column=1)
rd1l = ttk.Label(frame, textvariable=rd3_state)
rd1l.grid(row=4, column=1)

rStrv = StringVar()
rd1 = ttk.Radiobutton(frame, text='Home', variable=rStrv, value='one')
rd2 = ttk.Radiobutton(frame, text='Office', variable=rStrv, value='two')
rd3 = ttk.Radiobutton(frame, text='Mobile', variable=rStrv, value='three')
rd1.grid(row=2, column=0)
rd2.grid(row=3, column=0)
rd3.grid(row=4, column=0)

rStrv1 = StringVar()
rd4 = ttk.Radiobutton(frame, text='Home1', variable=rStrv1, value='one1')
rd5 = ttk.Radiobutton(frame, text='Office1', variable=rStrv1, value='two1')
rd6 = ttk.Radiobutton(frame, text='Mobile1', variable=rStrv1, value='three1')
rd4.grid(row=2, column=2)
rd5.grid(row=3, column=2)
rd6.grid(row=4, column=2)


cmb_state = StringVar()

cmbl = ttk.Label(frame, textvariable=cmb_state)
cmbl.grid(row=5, column=1)

cmbStr = StringVar()
cmb = ttk.Combobox(frame, textvariable=cmbStr)
cmb.grid(row=5, column=0)
cmb['values'] = ('USA', 'Canada', 'Australia')
#cmb.state(['readonly'])


window.bind("<Return>", lambda e:refreshStates())

window.mainloop()
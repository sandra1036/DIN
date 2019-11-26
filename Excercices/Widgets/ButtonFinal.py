from tkinter import *
from tkinter import ttk

window = Tk()
#Button
statebuttons=StringVar()
#CheckButton
statecheckbutton=StringVar()
measureSystem=StringVar()
#RadioButton
phone = StringVar()
rd1=StringVar()
rd2=StringVar()
rd3=StringVar()

#ComboBox
contryvar=StringVar()
labelvar=StringVar()


def refresh():
    statebuttons.set(button.state())
    statecheckbutton.set(check.state())
    rd1.set(home.state())
    rd2.set(office.state())
    rd3.set(cell.state())
    labelvar.set(combobox.state())
    click()

def click():
    phone.set("home")
    measureSystem.set("ON")
    contryvar.set("USA")


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


home = ttk.Radiobutton(frame, text='Home', variable=phone, value='home')
home.grid(column=0,row=2)
labelhome=ttk.Label(frame,text="Home",textvariable=rd1)
labelhome.grid(column=1,row=2)

office = ttk.Radiobutton(frame, text='Office', variable=phone, value='office')
office.grid(column=0,row=3)
labeloffice=ttk.Label(frame,text="Office",textvariable=rd2)
labeloffice.grid(column=1,row=3)

cell = ttk.Radiobutton(frame, text='Mobile', variable=phone, value='cell')
cell.grid(column=0,row=4)
labelcell=ttk.Label(frame,text="cell",textvariable=rd3)
labelcell.grid(column=1,row=4)

combobox=ttk.Combobox(frame,textvariable=contryvar)
combobox.grid(column=0,row=5)
combobox["values"]= ('USA', 'Canada', 'Australia')
#combobox.state(["readonly"])# no te deja escribir en el combobox
labelCombobox=ttk.Label(frame,textvariable=labelvar)
labelCombobox.grid(column=1,row=5)
buttonsstates=ttk.Button(frame,text="State",command=lambda : click())
buttonsstates.grid(column=1,row=6)

window.bind('<Return>',lambda e:refresh())
window.mainloop()

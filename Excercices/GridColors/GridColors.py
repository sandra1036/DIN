from tkinter import *
from tkinter import ttk

window=Tk()

frame=ttk.Frame(window)
frame.grid(column=0,row=0)


buttonClear=ttk.Button(frame,text="Clear")
buttonClear.grid(column=0,row=0, sticky = W)

buttonSet=ttk.Button(frame,text="Set")
buttonSet.grid(column=0,row=5, sticky = W)

combo=ttk.Combobox(frame)
combo.grid(column=1,columnspan=4,row=5)
combo["values"]=("Red","Green","Yellow","Purple")
combo.set(combo["values"][0])

#ListLabel
listlabel=list()
#List CheckButton
listchbh=list()
listchbv=list()


#CheckButton
for i in range(4):
    listchbv.append(StringVar())
    listchbh.append(StringVar())
    check=ttk.Checkbutton(frame,variable=listchbh[i])
    check.grid(row=0,column=i+1)
    check=ttk.Checkbutton(frame,variable=listchbv[i])
    check.grid(row=i+1,column=0)


#Labels

for r in range(4):
    listlabel.append([])
    for c in range(4):
        listlabel[r].append(ttk.Label(frame,relief="ridge",padding=(30,30,40,30)))
        listlabel[r][c].grid(row=r+1,column=c+1)

window=mainloop()








from tkinter import *
from tkinter import ttk

window=Tk()
frame=ttk.Frame(window)
frame.grid(column=0,row=0)




#Labels Alfabet
listLabelh=list()
listLabelhVar=StringVar()

for c in range(3):
    listLabelh.append(ttk.Label(frame,textvariable=listLabelhVar,relief="ridge",padding=(10,10,10,10)))
    listLabelh[c].grid(column=c+1,row=0,sticky=NSEW)



#LabelsNum
listLabelv=list()
listLabelvVar=StringVar()

for r in range(6):
    listLabelv.append(ttk.Label(frame,text=r,textvariable=listLabelvVar,relief="ridge",padding=(10,10,10,10)))
    listLabelv[r].grid(column=0,row=r+1,sticky=NSEW)



listEntrys=list()
#Entrys
for r in range(6):
    listEntrys.append([])
    for c in range(3):
        listEntrys[r].append(ttk.Entry(frame))
        listEntrys[r][c].grid(column=c+1,row=r+1,sticky=NSEW)








window.mainloop()
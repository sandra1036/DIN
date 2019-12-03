from tkinter import *
from tkinter import ttk

window=Tk()
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=5)



#variable combo
colorL=StringVar()

#ListLabel
listlabel=list()
#List CheckButton
listchbh=list()
listchbv=list()


def colors(listV:list,listH:list,listlabels:list,colorL:StringVar):

    for r in range(len(listlabels)):
        for c in range(len(listlabels[r])):
            if listV[r].get() and listH[c].get():
                print("dentro")
                listlabels[r][c].config(background=colorL.get())

def clear(listlabels:list):
    for r in range(len(listlabels)):
        for c in range(len(listlabels[r])):
            listlabels[r][c]["background"]= ""



#otra manera

    #Coordenadas
def get_coordinates(h:list,v:list)-> list:
    coords=[]
    for r in range(4):
        if v[r].get()=="1":
            for c in range(4):
                if h[c].get()=="1":
                    coords.append((r,c))
    return coords

    #Colores

def set_labels_color(h:list,v:list,s,lg:list):
    coord=get_coordinates(h,v)
    color=s.get()
    for t in coord:
        (r,c)=t
        lg[r][c]["background"]=color




frame=ttk.Frame(window)

frame.grid(column=0,row=0,sticky=NSEW)


buttonClear=ttk.Button(frame,text="Clear",command=lambda : clear(listlabel))
buttonClear.grid(column=0,row=0, sticky = W)

buttonSet=ttk.Button(frame,text="Set",command=lambda: colors(listchbv,listchbh,listlabel,colorL))
buttonSet.grid(column=0,row=5, sticky = W)

combo=ttk.Combobox(frame,textvar=colorL)
combo.grid(column=1,columnspan=4,row=5,sticky="we")
combo["values"]=("Red","Green","Yellow","Purple","Blue","Orange")
combo.set(combo["values"][0])
combo.bind("<<ComboSelected>>"),lambda e: colors(listchbh,listchbh,listlabel,colorL)



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
        listlabel[r][c].grid(row=r+1,column=c+1,sticky=NSEW)
        frame.rowconfigure(r+1, weight=1)
        frame.columnconfigure(c+1, weight=1)

window.update()
window.minsize(window.winfo_width(),window.winfo_height())
window=mainloop()








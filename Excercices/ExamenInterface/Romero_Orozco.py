from tkinter import *

window=Tk()

# model
counterR=IntVar()
counterR.set(255)

counterG=IntVar()
counterG.set(255)

counterB=IntVar()
counterB.set(255)
colors={"R":255,"G":255,"B":255}

#controler
def clickmin(counter):

    counter.set(counter.get() -5)

def clickmax(counter):
    counter.set(counter.get()+5)

def composeColor(R:int,G:int,B:int)-> str:

    return "#"\
            +(str(hex(R))[2:]).upper().zfill(2)\
            +(str(hex(G))[2:]).upper().zfill(2)\
            +(str(hex(B))[2:]).upper().zfill(2)


#View

frame = Frame(window)
frame.pack(side="left")
labelR = Label(frame, text="RED")
labelR.grid(column=0,row=0)
labelG=Label(frame,text="Green")
labelG.grid(column=0,row=1)
labelB=Label(frame,text="Blue")
labelB.grid(column=0,row=2)

buttonMinR = Button(frame, text='-',command=lambda : clickmin(counterR))
buttonMinR.grid(column=1,row=0)
labelCR=Label(frame,text="255",textvariable=counterR)
labelCR.grid(column=2,row=0)
buttonMaxR = Button(frame, text='+',command=lambda :clickmax(counterR))
buttonMaxR.grid(column=3,row=0)

buttonMinG = Button(frame, text='-',command=lambda :clickmin(counterG))
buttonMinG.grid(column=1,row=1)
labelCG=Label(frame,text="255",textvariable=counterG)
labelCG.grid(column=2,row=1)
buttonMaxG = Button(frame, text='+',command=lambda:clickmax(counterG))
buttonMaxG.grid(column=3,row=1)

buttonMinB = Button(frame, text='-',command=lambda :clickmin(counterB))
buttonMinB.grid(column=1,row=2)
labelCB=Label(frame,text="255",textvariable=counterB)
labelCB.grid(column=2,row=2)
buttonMaxB = Button(frame, text='+',command=lambda:clickmax(counterB))
buttonMaxB.grid(column=3,row=2)

buttonMix=Button(window,text="Mix",command=lambda : composeColor(255,255,255))
buttonMix.pack()

labelR.config(anchor=CENTER,font=("Helvetica",16))
labelG.config(anchor=CENTER,font=("Helvetica",16))
labelB.config(anchor=CENTER,font=("Helvetica",16))

buttonMinR.config(font=("Helvetica",16),height=2,relief=SUNKEN,anchor=CENTER)
buttonMinG.config(font=("Helvetica",16),height=2,relief=SUNKEN,anchor=CENTER)
buttonMinB.config(font=("Helvetica",16),height=2,relief=SUNKEN,anchor=CENTER)
buttonMaxR.config(font=("Helvetica",16),height=2,relief=SUNKEN,anchor=CENTER)
buttonMaxG.config(font=("Helvetica",16),height=2,relief=SUNKEN,anchor=CENTER)
buttonMaxB.config(font=("Helvetica",16),height=2,relief=SUNKEN,anchor=CENTER)
buttonMix.config(font=("Helvetica",16),width=9,height=7,relief=SUNKEN,anchor=CENTER,bg="#FFFFFF")
labelCR.config(bg="#FF0000",font=("Helvetica",16),width=8,height=2,anchor=CENTER)
labelCG.config(bg="#00FF00",font=("Helvetica",16),width=8,height=2,anchor=CENTER)
labelCB.config(bg="#0000FF",font=("Helvetica",16),width=8,height=2,anchor=CENTER)

window.mainloop()
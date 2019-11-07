from tkinter import *

window=Tk()

# Model

textoNum = StringVar()


# Controler
def añade(textoNum,texto):

    textoNum.set(textoNum.get()+texto)
    label["text"]=texto


def equals():



# View

label=Label(window,textvar=textoNum)
label.pack()

frame=Frame(window)
frame.pack()

buttonNum7=Button(frame,text="7",command=lambda:añade(textoNum,"7"))
buttonNum7.grid(column=0,row=0)
buttonNum8=Button(frame,text="8",command=lambda:añade(textoNum,"8"))
buttonNum8.grid(column=1,row=0)
buttonNum9=Button(frame,text="9",command=lambda:añade(textoNum,"9"))
buttonNum9.grid(column=2,row=0)
buttonDiv=Button(frame,text="/",command=lambda:añade(textoNum,"/"))
buttonDiv.grid(column=3,row=0)
buttonMc=Button(frame,text="Mc",command=lambda:añade(textoNum,"Mc"))
buttonMc.grid(column=4,row=0)

buttonNum4=Button(frame,text="4",command=lambda:añade(textoNum,"4"))
buttonNum4.grid(column=0,row=1)
buttonNum5=Button(frame,text="5",command=lambda:añade(textoNum,"5"))
buttonNum5.grid(column=1,row=1)
buttonNum6=Button(frame,text="6",command=lambda:añade(textoNum,"6"))
buttonNum6.grid(column=2,row=1)
buttonNumMul=Button(frame,text="*",command=lambda:añade(textoNum,"*"))
buttonNumMul.grid(column=3,row=1)
buttonMs=Button(frame,text="Ms",command=lambda:añade(textoNum,"Ms"))
buttonMs.grid(column=4,row=1)


buttonNum1=Button(frame,text="1",command=lambda:añade(textoNum,"1"))
buttonNum1.grid(column=0,row=2)
buttonNum2=Button(frame,text="2",command=lambda:añade(textoNum,"2"))
buttonNum2.grid(column=1,row=2)
buttonNum3=Button(frame,text="3",command=lambda:añade(textoNum,"3"))
buttonNum3.grid(column=2,row=2)
buttonNumRes=Button(frame,text="-",command=lambda:añade(textoNum,"-"))
buttonNumRes.grid(column=3,row=2)
buttonMr=Button(frame,text="Mr",command=lambda:añade(textoNum,"Mr"))
buttonMr.grid(column=4,row=2)


buttonNum0=Button(frame,text="0",command=lambda:añade(textoNum,"0"))
buttonNum0.grid(column=0,row=3)
buttonP=Button(frame,text=".",command=lambda:añade(textoNum,"."))
buttonP.grid(column=1,row=3)
buttonEq=Button(frame,text="=",command=lambda:añade(textoNum,"="))
buttonEq.grid(column=2,row=3)
buttonAd=Button(frame,text="+",command=lambda:añade(textoNum,"+"))
buttonAd.grid(column=3,row=3)
buttonDel=Button(frame,text="Del",command=lambda:añade(textoNum,"Del"))
buttonDel.grid(column=4,row=3)
window.mainloop()



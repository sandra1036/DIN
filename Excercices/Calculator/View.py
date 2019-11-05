from tkinter import *


if __name__=="__main__":
    window=Tk()
    label=Label(window,text="Numbers")
    label.pack()
    frame=Frame(window)
    frame.pack()
    buttonNum7=Button(frame,text="7")
    buttonNum7.grid(column=0,row=0)
    buttonNum8=Button(frame,text="8")
    buttonNum8.grid(column=1,row=0)
    buttonNum9=Button(frame,text="9")
    buttonNum9.grid(column=2,row=0)
    buttonDiv=Button(frame,text="/")
    buttonDiv.grid(column=3,row=0)
    buttonMc=Button(frame,text="Mc")
    buttonMc.grid(column=4,row=0)

    buttonNum4=Button(frame,text="4")
    buttonNum4.grid(column=0,row=1)
    buttonNum5=Button(frame,text="5")
    buttonNum5.grid(column=1,row=1)
    buttonNum6=Button(frame,text="6")
    buttonNum6.grid(column=2,row=1)
    buttonNumMul=Button(frame,text="*")
    buttonNumMul.grid(column=3,row=1)
    buttonMs=Button(frame,text="Ms")
    buttonMs.grid(column=4,row=1)


    buttonNum1=Button(frame,text="1")
    buttonNum1.grid(column=0,row=2)
    buttonNum2=Button(frame,text="2")
    buttonNum2.grid(column=1,row=2)
    buttonNum3=Button(frame,text="3")
    buttonNum3.grid(column=2,row=2)
    buttonNumRes=Button(frame,text="-")
    buttonNumRes.grid(column=3,row=2)
    buttonMr=Button(frame,text="Mr")
    buttonMr.grid(column=4,row=2)


    buttonNum0=Button(frame,text="0")
    buttonNum0.grid(column=0,row=3)
    buttonP=Button(frame,text=".")
    buttonP.grid(column=1,row=3)
    buttonEq=Button(frame,text="=")
    buttonEq.grid(column=2,row=3)
    buttonAd=Button(frame,text="+")
    buttonAd.grid(column=3,row=3)
    buttonDel=Button(frame,text="Del")
    buttonDel.grid(column=4,row=3)

window.mainloop()



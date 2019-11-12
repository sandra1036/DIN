from tkinter import *

window=Tk()
#model

text=Text(window,width=30,height=10)
text.grid(column=0,row=0)

dat=text.get("0.0",END)
letras=StringVar()
#controler
def count():
    contA=0
    contT=0
    contG=0
    contC=0

    for i in dat:

        if i=="A"or i=="a":
            contA+=1


        if i=="T" or i=="t":
            contT+=1

        if i=="G"or i=="g":
            contG+=1

        if i=="C" or i=="c":
            contC+1

    letras.set("Num As:{0} Num Ts:{1} Num Cs:{2} Num Gs:{3}".format(contA,contT,contC,contG))


#View

frame=Frame(window)
frame.pack()

button=Button(frame, text="Count", command=lambda: count())
button.grid(column=0,row=1)
label=Label(frame,textvar=letras)
label.grid(column=0,row=2)

window.mainloop()



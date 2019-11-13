from tkinter import *

window=Tk()
menubar=Menu(window)
fileMenu=Menu(menubar)
frame=Frame(window)
frame.pack()
text=Text(frame,width=30,height=10)
text.grid(column=0,row=0)



letras=StringVar()
#controler
def count():
    contA=0
    contT=0
    contG=0
    contC=0

    dat = text.get("0.0", END)#Es necesario que vaya dentro
    for i in dat:

        if i=="A"or i=="a":
            contA+=1


        if i=="T" or i=="t":
            contT+=1

        if i=="C" or i=="c":
            contC+1

        if i=="G"or i=="g":
            contG+=1



    letras.set("Num As:{0} Num Ts:{1} Num Cs:{2} Num Gs:{3}".format(contA,contT,contC,contG))

def delete(letra:str):
    borrar=text.get("1.0",END)
    text.delete("0.0",END)
    borrar=borrar.replace(letra,"")
    text.insert("0.0",borrar)



#View

frame=Frame(window)
frame.pack()
button=Button(frame, text="Count", command=lambda: count())
button.grid(column=0,row=1)
label=Label(frame,textvar=letras)
label.grid(column=0,row=2)
menubar.add_cascade(label="Borrar",menu=fileMenu)
fileMenu.add_command(label="Borra A",command=lambda: delete("a"))
fileMenu.add_command(label="Borra T",command=lambda: delete("t"))
fileMenu.add_command(label="Borra C",command=lambda: delete("c"))
fileMenu.add_command(label="Borra G",command=lambda: delete("g"))
window.config(menu=menubar)
window.mainloop()



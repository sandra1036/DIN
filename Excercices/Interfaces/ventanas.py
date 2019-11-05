import tkinter
window=tkinter.Tk()
data=tkinter.StringVar()
data.set("HOlA MUNDO!!!!!")
label = tkinter.Label(window,font=("Arial",150),textvariable=data,background="Green",foreground="white")
label.pack()
data.set("ADIOS MUNDO!!!!!!")
data2=tkinter.IntVar()

window.mainloop()

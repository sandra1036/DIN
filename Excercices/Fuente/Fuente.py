from tkinter import *
window=Tk()
act1=IntVar()
act2=IntVar()
act3=IntVar()

def font(entry,bold,coursiva,undeline):




























frame=Frame(window)
frame.pack()
entry=Entry(frame)
entry.grid(column=1,row=0)
chechboxbold=Checkbutton(frame,text="Bold",variable=act1)
chechboxbold.grid(column=0,row=3)
chechboxCursiva=Checkbutton(frame,text="Cursiva",variable=act2)
chechboxCursiva.grid(column=1,row=3)
chechboxunderline=Checkbutton(frame,text="Underline",variable=act3)
chechboxunderline.grid(column=2,row=3)
button=Button(frame,text="Update",command=lambda: font())
button.grid(column=1,row=4)
window.mainloop()

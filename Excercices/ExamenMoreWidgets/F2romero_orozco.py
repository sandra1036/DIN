from tkinter import *
from tkinter import ttk
def pref(root):
    window=Toplevel(root)
    window.title("Preferences")
    window.configure(relief="sunken",height=240,width=240)

    notebook=ttk.Notebook(window)
    notebook.pack()

    #Frame 1(LabelFrames)
    frame1=ttk.Frame(notebook,padding=(10,10,10,10))
    notebook.add(frame1,text="Label Frames")



    labelframe=ttk.Labelframe(frame1,text="LF",height=120,width=120)
    labelframe.grid(column=0,row=0)

    labelframe2=ttk.Labelframe(frame1,text="LF",height=120,width=120,labelanchor="sw")
    labelframe2.grid(column=0,row=1)

    labelframe3=ttk.Labelframe(frame1,text="LF",height=120,width=120,labelanchor="ne")
    labelframe3.grid(column=1,row=0)

    labelframe4=ttk.Labelframe(frame1,text="LF",height=120,width=120,labelanchor="se")
    labelframe4.grid(column=1,row=1)




    #Frame2
    frame2=ttk.Frame(notebook)
    notebook.add(frame2,text="Paned Windows",padding=(10,10,10,10))

    panedframe1=ttk.PanedWindow(frame2,width=200,height=100).pack()
    framepaned=ttk.Frame(panedframe1,relief="groove",padding=(10,10,10,10)).pack()
    panedframe2=ttk.PanedWindow(frame2,width=200,height=100).pack()
    framepaned2=ttk.Frame(panedframe2,relief="groove",padding=(10,10,10,10)).pack()

    style=ttk.Style()
    varlist=StringVar()
    varlist.set(style.theme_use('default'))
    style.configure('TRadiobutton',background="blue",foreground="yellow",font="helvetica 8")

    lf=Listbox(window)
    for t in style.theme_names():

        ttk.Radiobutton(lf, text=t, variable=varlist, value=t, command=lambda: style.theme_use(varlist.get())).pack()



    lf.pack()



    window.mainloop()
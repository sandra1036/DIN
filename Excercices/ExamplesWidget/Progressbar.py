from tkinter import *
from tkinter import ttk
import random

numRandom=set()

def cal():
    for i in range(25):
        numRandom.add(random.randrange(0,200))

        pvar.set(p.step(1))
    print(numRandom)
root = Tk()
c=Frame(root)
c.grid(column=0,row=0)
pvar=IntVar()
p=ttk.Progressbar(c,orient=HORIZONTAL,length=100,mode="determinate",variable=pvar)
p.grid(column=0,row=0)
button=ttk.Button(c,text="Calculate",command=cal)
button.grid(column=1,row=1)
p2=ttk.Progressbar(c,orient=HORIZONTAL,length=100,mode="indeterminate")
p2.grid(column=0,row=1)
root.mainloop()

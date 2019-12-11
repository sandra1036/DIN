import random
from tkinter import *
from tkinter import ttk
import time
#view
root = Tk()
frame = ttk.Frame(root)
frame.pack()
proI= IntVar()
p = ttk.Progressbar(frame, orient=HORIZONTAL,  variable=proI, length=200, mode='determinate', maximum=10000)
p.pack()
def enter():
    proI.set(0)
    for i in range(10000):
        print(i)

        for j in range(200):
            print(i**j)
        p.update()
        proI.set(i)

def v(j):
    proI.set(j)
root.bind('<Key>',lambda e: enter())

root.mainloop()

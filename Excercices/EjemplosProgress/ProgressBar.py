from tkinter import *
from tkinter import ttk
import random


def aPastar():
    a = []

    while len(a) < 200:
        num = random.randint(0, 199)
        p['value'] = len(a)
        p.update()
        if (num in a):
            for i in range(1,1000000):
                pass
        else:
            a.append(num)
            print(len(a))


root = Tk()
mainframe = ttk.Frame(root)
mainframe.grid()

p = ttk.Progressbar(mainframe, orient=HORIZONTAL, length=200, maximum=200, mode='determinate')
p.grid(column=0, row=0)

b = ttk.Button(mainframe, text="A pastar", command=lambda: aPastar())
b.grid(row=1, column=0)

mainframe.mainloop()

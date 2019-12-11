from tkinter import *
from tkinter import ttk
import random

window= Tk()

#CONTROLLER

def buttonCommand(button):
    button.state(['disabled'])
    fillArray()
    
def fillArray():
    allNums = []
    
    for i in range(199):
        allNums.append(i)

    for i in range(199):
        for i in range(199):
            if not i in numArray:
                numArray.append(i)
                p['value'] =  len(numArray)
                p.update()
                break
                        
            print(numArray)
            pass
    
        

#MODEL
numArray = []

#VIEW
frame = ttk.Frame(window)
frame.grid(column=0, row=0, sticky=(N,S,W,E))

label = ttk.Label(frame, text="Progress Bar example")
label.grid(column=0, row=1)

p = ttk.Progressbar(frame, orient=HORIZONTAL, length=200, mode='determinate')
p['maximum'] = 200
p.grid(column=0, row=2)

button = ttk.Button(frame, command=lambda:buttonCommand(button), text="Fill Array")
button.grid(column=0, row=3)


window.mainloop()


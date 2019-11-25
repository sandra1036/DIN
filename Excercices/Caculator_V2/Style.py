from tkinter import *
from tkinter import ttk
window=Tk()
s = ttk.Style()
butt=ttk.Button(text="prueba modelo")
butt.pack()

s.configure('Wild.TButton',
            background='black',
            foreground='white',
            highlightthickness='20',
            font=('Helvetica', 18, 'bold'))
s.map('Wild.TButton',
      foreground=[('disabled', 'yellow'),
                  ('pressed', 'red'),
                  ('active', 'blue')],
      background=[('disabled', 'magenta'),
                  ('pressed', '!focus', 'cyan'),
                  ('active', 'green')],
      highlightcolor=[('focus', 'green'),
                      ('!focus', 'red')],
      relief=[('pressed', 'groove'),
              ('!pressed', 'ridge')])
window.mainloop()
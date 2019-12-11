import tkinter as tk
from threading import Thread
from tkinter import ttk
from time import sleep


class Application(ttk.Frame):

    def bucle(self):
        for i in range(100):
            sleep(0.1)
            self.x.set(i)


    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Barra de progreso en Tk")

        self.x = tk.IntVar()
        self.x.set(0)

        self.progressbar = ttk.Progressbar(self, mode='determinate', variable = self.x)
        self.progressbar.place(x=30, y=60, width=200)

        self.start_button = ttk.Button(self, text="Start", command=lambda: Thread(target=self.bucle).start())
        self.start_button.place(x=30, y=20)

        self.place(width=300, height=200)
        main_window.geometry("300x200")

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
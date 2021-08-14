from tkinter import *
from time import strftime

root = Tk()
root.title("Clock")


def time():
    time_string = strftime("%H:%M:%S %p")
    label.config(text=time_string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

time()
mainloop()


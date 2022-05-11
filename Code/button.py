from tkinter import *
import random

root = Tk()
root.geometry("700x450")

label1 = Label(root, font = ("times", 100))

def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label1.config(text = f'{random.choice(number)}')
    label1.pack(side = LEFT)

button = Button(root, text = "Roll", command = roll)
button.place(x = 20, y = 350)

root.mainloop()

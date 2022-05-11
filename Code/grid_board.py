from tkinter import *

root = Tk()
root.title("Board")
root.geometry("900x700")

canvas = Canvas(root, width = 700, height = 700, bg = "pink")
canvas.pack()

for i in range(1, 10):
    canvas.create_line(0, 70 * i, 700, 70 * i, fill = "black", width = 3)

for j in range(1, 10):
    canvas.create_line(70 * j, 0, 70 * j, 700, fill = "black", width = 3)



root.mainloop()


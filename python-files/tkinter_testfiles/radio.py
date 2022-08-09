from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("Hallo Welt!")
root.iconbitmap('index.ico')
root.geometry("500x300")

#r = IntVar()
#r.set(2)

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom")
]

pizza = StringVar()
pizza.set("Peperoni")

for text, mode in MODES:
    Radiobutton(root,  text=text, variable=pizza, value=mode).pack()

def clicked(value):
    label = Label(root, text=value)
    label.pack()

#Radiobutton(root, text="option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="option 1", variable=r, value=2, command=lambda: clicked(r.get())).pack()

quit_button = Button(root, text="click to quit program", command=root.quit)
quit_button.pack()

root.mainloop()
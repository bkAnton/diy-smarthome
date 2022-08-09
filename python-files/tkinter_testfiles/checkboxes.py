from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Hallo Welt!")
root.iconbitmap('index.ico')
root.geometry("500x300")


def show():
    lb = Label(root, text=var.get()).pack()

var = StringVar() #StringVar()
c = Checkbutton(root, text="Check this Box", variable=var, onvalue="Pzza", offvalue="Lasagne")
c.deselect()
c.pack()

button = Button(root, text="Show selection", command=show).pack()

root.mainloop()
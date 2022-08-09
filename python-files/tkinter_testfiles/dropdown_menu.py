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
    Label(root, text=clicked.get()).pack()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = StringVar()
clicked.set(options[0])
dropdown = OptionMenu(root, clicked, *options).pack()

btn = Button(root, text="show selection", command=show).pack()
root.mainloop()
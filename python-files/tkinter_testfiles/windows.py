from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

root = Tk()
root.title("Hallo Welt!")
root.iconbitmap('index.ico')
root.geometry("500x300")


def open():
    global img
    top = Toplevel()
    top.title("second window")
    top.iconbitmap('index.ico')
    top.geometry("500x300")

    img = ImageTk.PhotoImage(Image.open("index.png"))
    label = Label(top, image=img).pack()
    Button(top, text="close window", command=top.destroy).pack()

Button(root, text="open window", command=open).pack()


root.mainloop()
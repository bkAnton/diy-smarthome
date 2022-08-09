from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

root = Tk()
root.title("Hallo Welt!")
root.iconbitmap('index.ico')
root.geometry("500x300")

def popup():
    r = messagebox.askokcancel("This is my Popup!", "Hello World!")
    Label(root, text=r).pack()

button = Button(root, text="Popup", command=popup)
button.pack()

root.mainloop()
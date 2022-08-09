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

def slide(var):
    h_label = Label(root, text=horizontal.get()).pack()

vertical = Scale(root, from_=0, to=200).pack()
horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=slide)
horizontal.pack()

button = Button(root, text="Click", command=slide).pack()
root.mainloop()
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

def open():
    global img
    files = filedialog.askopenfilename(initialdir="D://", title="Select a file", filetypes=(("png files", "*.png"),("all files", "*.*")))
    label = Label(root, text=files).pack()
    img = ImageTk.PhotoImage(Image.open(files))
    img_label = Label(image=img).pack()

btn = Button(root, text="open file", command=open).pack()

root.mainloop()
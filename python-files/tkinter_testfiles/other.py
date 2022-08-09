from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("Hallo Welt!")
root.iconbitmap('index.ico')
root.geometry("500x300")


img = ImageTk.PhotoImage(Image.open("index.png"))
label = Label(image=img)
label.pack()

quit_button = Button(root, text="click to quit program", command=root.quit)
quit_button.pack()
root.mainloop()
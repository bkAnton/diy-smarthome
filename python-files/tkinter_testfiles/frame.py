from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("Hallo Welt!")
root.iconbitmap('index.ico')
root.geometry("500x300")

frame = LabelFrame(root, text="This is ther Frame", padx=10, pady=10)
frame.pack(padx=10, pady=10)

quit_button = Button(frame, text="click to quit program", command=root.quit)
quit_button.pack()

root.mainloop()
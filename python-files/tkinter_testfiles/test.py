from tkinter import *

root = Tk()
root.geometry("500x300")

myLabel = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel1 = Label(root, text="Hello!").grid(row=1, column=1)


root.mainloop()
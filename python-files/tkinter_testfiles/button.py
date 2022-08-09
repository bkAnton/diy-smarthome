from tkinter import *

root = Tk()
root.geometry("500x300")

def myClick():
    label =Label(root, text="You clicked the Button!")
    label.pack()

button = Button(root, text="Button", padx=10, pady=10, command=myClick, fg="blue", bg="#aaaaaa")
button_d = Button(root, text="Button", state=DISABLED)
button.pack()
button_d.pack()

root.mainloop()
from tkinter import *

root = Tk()
root.title("Hallo Welt!")
#root.iconbitmap('index.ico')
root.geometry("500x300")

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter you Name: ")

def myClick():
    label =Label(root, text=f"{e.get()}")
    label.pack()

button = Button(root, text="Button", padx=10, pady=10, command=myClick, fg="black", bg="#aaaaaa")
button_d = Button(root, text="Button", state=DISABLED)
button.pack()
button_d.pack()

root.mainloop()
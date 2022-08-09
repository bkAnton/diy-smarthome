from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.title("Hallo Welt!")
root.iconbitmap('index.ico')
#root.geometry("500x300")

conn = sqlite3.connect('adress_book.db')


c = conn.cursor()

#create table
'''
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''

#submit function for database
def submit():
    #connect or create to database
    conn = sqlite3.connect('adress_book.db')
    #Set cursor
    c = conn.cursor()

    #Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city' : city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()   
            })

    #Commit changes
    conn.commit()

    #close connection
    conn.close()


    #clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query function
def query():

    conn = sqlite3.connect('adress_book.db')
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\n"

    query_label = Label(root, text=print_records).grid(row=8, column=0, columnspan=2)


    conn.commit()
    conn.close()

#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

#create Text Box Label
f_name_lb = Label(root, text=f"First name").grid(row=0, column=0)
l_name_lb = Label(root, text=f"Last name").grid(row=1, column=0)
address_lb = Label(root, text=f"address").grid(row=2, column=0)
city_lb = Label(root, text=f"City").grid(row=3, column=0)
state_lb = Label(root, text=f"state").grid(row=4, column=0)
zipcode_lb = Label(root, text=f"zipcode").grid(row=5, column=0)

#Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit).grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query).grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)



conn.commit()
conn.close()

root.mainloop()

from ast import Pass
from tkinter import *
from unicodedata import name

root = Tk()
root.geometry("750x450")
root.title("Smarthome")
root.configure(bg='#282828')

# Add Toolbar in the Bottem of the Root window
my_menu = Menu(root)
root.config(menu=my_menu)


class open_window():
    pass




# Syncs Data from Database 
def sync():
    pass

# Saves settings from the GUI program
def save_settings():
    pass

 # Add a Sensor to the Smarthome
def add_sensor():
    add_sensor_window = Toplevel(root)
    add_sensor_window.title("Add Sensor")
    add_sensor_window.geometry("400x400")
    add_sensor_window.configure(bg='#282828')

    Entry(add_sensor_window, width=20).grid(row=0, column=1)
    Label(add_sensor_window, text='Enter a Name: ').grid(row=0, column=0)
    Button(add_sensor_window, text="Save", padx=10, pady=1, command=Pass).grid(row=0, column=2)

# Add a RGB-Strip to the Smarthome
def add_rgb_strip():
    add_rgb_strip_window = Toplevel(root)
    add_rgb_strip_window.title("Add RGB Strip")
    add_rgb_strip_window.geometry("400x400")
    add_rgb_strip_window.configure(bg='#282828')

# Add a Wireless Socket to the Smarthome
def add_wireless_socket():
    add_wireless_socket_window = Toplevel(root)
    add_wireless_socket_window.title("Add Wireless Socket")
    add_wireless_socket_window.geometry("400x400")
    add_wireless_socket_window.configure(bg='#282828')

# Add a Button Panel to the Smarthome
def add_button_panel():
    add_button_panel_window = Toplevel(root)
    add_button_panel_window.title("Add Button Panel")
    add_button_panel_window.geometry("400x400")
    add_button_panel_window.configure(bg='#282828')

# Add another device to the Smarthome
def add_device():
    add_device_window = Toplevel(root)
    add_device_window.title("Add Device")
    add_device_window.geometry("400x400")
    add_device_window.configure(bg='#282828')

# Show the list of all devices
def show_devices():
    show_devices_window = Toplevel(root)
    show_devices_window.title("Add SensorDevices")
    show_devices_window.geometry("400x400")
    show_devices_window.configure(bg='#282828')

# restart the interface program to update the functions which controlls the computer
def restart_interface_program():
    pass

# open the settings 
def settings():
    show_settins_window = Toplevel(root)
    show_settins_window.title("Settings")
    show_settins_window.geometry("400x400")
    show_settins_window.configure(bg='#282828')



# Create General menu
general_menu = Menu(my_menu, tearoff=False)
general_menu.add_command(label="Save", command=save_settings)
general_menu.add_command(label="Settings", command=save_settings)
general_menu.add_command(label="Open File Location", command=Pass)

# Create interface menu
interface_menu= Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Interface', menu=interface_menu)

interface_menu.add_command(label='Save Settings', command=save_settings)
interface_menu.add_command(label='Sync', command='Sync')
interface_menu.add_command(label='Restart Interface Application', command=restart_interface_program)


# Create device menu
device_menu= Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Devices', menu=device_menu)


# Create Submenu
sub_menu = Menu(device_menu, tearoff=0)

sub_menu.add_command(label='Sensor', command=add_sensor)
sub_menu.add_command(label='RGB-Strip', command=add_rgb_strip)
sub_menu.add_command(label='Wireless Socket', command=add_wireless_socket)
sub_menu.add_command(label='Button Panel', command=add_button_panel)
sub_menu.add_command(label='Something Else', command=add_device)

device_menu.add_cascade(label='Add device', menu=sub_menu)
device_menu.add_command(label='Show device', command=show_devices)



root.mainloop()
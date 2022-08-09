from tkinter import *
from unicodedata import name

root = Tk()
root.geometry("750x450")
root.title("Smarthome")


my_menu = Menu(root)
root.config(menu=my_menu)


def sync():
    pass

def save_settings():
    pass

def add_sensor():
    add_sensor_window = Toplevel(root)
    add_sensor_window.title("Add Sensor")
    add_sensor_window.geometry("400x400")

    name = Entry(add_sensor_window, width=20)
    name.config(fg='grey')
    name.insert(0, 'name')
    name.pack()


def add_rgb_strip():
    add_rgb_strip_window = Toplevel(root)
    add_rgb_strip_window.title("Add RGB Strip")
    add_rgb_strip_window.geometry("400x400")

def add_wireless_socket():
    add_wireless_socket_window = Toplevel(root)
    add_wireless_socket_window.title("Add Wireless Socket")
    add_wireless_socket_window.geometry("400x400")

def add_button_panel():
    add_button_panel_window = Toplevel(root)
    add_button_panel_window.title("Add Button Panel")
    add_button_panel_window.geometry("400x400")

def add_device():
    add_device_window = Toplevel(root)
    add_device_window.title("Add Device")
    add_device_window.geometry("400x400")

def show_devices():
    show_devices_window = Toplevel(root)
    show_devices_window.title("Devices")
    show_devices_window.geometry("400x400")

def restart_interface_program():
    pass


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
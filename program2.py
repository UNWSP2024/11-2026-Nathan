# By Nathan Nelsen
# Written 4/17/26
# GUI Program #2

import tkinter as tk

def show_info():
    name_label.config(text="Name: Nathan")
    address_label.config(text="Address: 156 Aster Circuit, Duluth, MN 55804")

root = tk.Tk()
root.title("Information Display")
root.geometry("500x300")

name_label = tk.Label(root, text="", font=("Arial", 12))
name_label.pack(pady=10)

address_label = tk.Label(root, text="", font=("Arial", 12))
address_label.pack(pady=10)

show_button = tk.Button(root, text="Show Info", command=show_info)
show_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(pady=10)

root.mainloop()

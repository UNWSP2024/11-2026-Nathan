# By Nathan Nelsen
# Written 4/17/26
# GUI Program #1

import tkinter as tk

root = tk.Tk()
root.title("Favorite Saying")
root.geometry("300x100")

saying = "Jesus is the way, the truth, and the life."

label = tk.Label(root, text=saying, font=("Arial", 12), wraplength=300, justify="center")
label.pack(expand=True)

root.mainloop()

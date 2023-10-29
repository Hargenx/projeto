import tkinter as tk
from tkinter import Scrollbar

root = tk.Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

items = ["Item " + str(i) for i in range(1, 21)]
for item in items:
    listbox.insert(tk.END, item)

root.mainloop()

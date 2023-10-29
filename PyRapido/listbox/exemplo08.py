import tkinter as tk
from tkinter.tix import ListBox

root = tk.Tk()
listbox = ListBox(root, selectmode='multiple')
listbox.pack()

items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

root.mainloop()

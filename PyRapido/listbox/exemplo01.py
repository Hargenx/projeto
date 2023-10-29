import tkinter as tk

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack()

items = ["Item 1", "Item 2", "Item 3"]
for item in items:
    listbox.insert(tk.END, item)

root.mainloop()

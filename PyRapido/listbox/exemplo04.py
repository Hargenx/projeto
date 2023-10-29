import tkinter as tk

root = tk.Tk()
listbox = tk.Listbox(root, height=5)
listbox.pack()

items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]
for item in items:
    listbox.insert(tk.END, item)

root.mainloop()

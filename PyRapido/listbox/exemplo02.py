import tkinter as tk

root = tk.Tk()
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack()

items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

root.mainloop()
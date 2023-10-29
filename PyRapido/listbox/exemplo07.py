import tkinter as tk

root = tk.Tk()

# Variável de controle
selected_item = tk.StringVar()

listbox = tk.Listbox(root, listvariable=selected_item)
listbox.pack()

items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

selected_item.set(items[0])  # Defina o item selecionado inicialmente

root.mainloop()

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root, columns=("Nome", "Idade"))
tree.heading("#1", text="Nome")
tree.heading("#2", text="Idade")
tree.pack()

# Adicionando o item "Pessoa 1" na raiz da árvore
item_pessoa1 = tree.insert("", tk.END, text="Pessoa 1", values=("Alice", 30))

# Agora você pode adicionar subitens em "Pessoa 1" usando sua chave
tree.insert(item_pessoa1, tk.END, text="Filho 1", values=("Charlie", 5))

root.mainloop()

import tkinter as tk
from view import JogoView
from banco import banco

if __name__ == "__main__":
    # Chame a função banco() sem especificar o caminho
    conn = banco()
    root = tk.Tk()
    app = JogoView(root)
    root.mainloop()

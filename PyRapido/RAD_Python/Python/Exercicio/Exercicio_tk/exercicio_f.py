from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()
lista_times = ["Flamengo", "Vasco", "Fluminense", "Botafogo"]
Combo = ttk.Combobox(frame, values=lista_times)
Combo.set("Escolha um time")
items = StringVar()
items.set("Escolha o time")
times = OptionMenu(root, items, "Flamengo", "Vasco", "Fluminense", "Botafogo", "Madureira", "Bangu", "Volta Redonda", "Portuguesa")
times.pack()
Combo.pack(padx=5, pady=5)
root.mainloop()

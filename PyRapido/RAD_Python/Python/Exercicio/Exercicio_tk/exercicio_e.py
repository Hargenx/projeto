from tkinter import *
root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()
MenuBttn = Menubutton(frame, text="Lista de compras", relief=RAISED)
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Var4 = IntVar()
Var5 = IntVar()
Menu1 = Menu(MenuBttn, tearoff=0)
Menu1.add_checkbutton(label="Tomate", variable=Var1)
Menu1.add_checkbutton(label="Cebola", variable=Var2)
Menu1.add_checkbutton(label="Costela de porco", variable=Var3)
Menu1.add_checkbutton(label="Arroz", variable=Var4)
Menu1.add_checkbutton(label="Feijão", variable=Var5)
MenuBttn["menu"] = Menu1
MenuBttn.pack()
root.mainloop()

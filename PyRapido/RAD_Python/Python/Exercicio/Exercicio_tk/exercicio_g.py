from tkinter import *
root = Tk()
root.geometry("200x250")
minha_label = Label(root, text='Barra de rolagem', font="28")
minha_label.pack()
meu_scroll = Scrollbar(root)
meu_scroll.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=meu_scroll.set)
for line in range(1, 101):
    mylist.insert(END, "Numero: " + str(line))
mylist.pack(side=LEFT, fill=BOTH)
meu_scroll.config(command=mylist.yview)
root.mainloop()

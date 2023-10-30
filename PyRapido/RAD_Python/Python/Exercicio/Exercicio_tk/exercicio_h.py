from tkinter import *
def novajanela():
    window = Toplevel()
    window.geometry('150x150')
    newlabel = Label(window, text="Configurações")
    newlabel.pack()
root = Tk()
root.geometry('200x200')
myframe = Frame(root)
myframe.pack()
mybutton = Button(myframe, text="Configurações", command=novajanela, fg="black", font="Verdana 14 underline", bd=2, bg="blue", relief="groove")
mybutton.pack(pady=10)
root.mainloop()

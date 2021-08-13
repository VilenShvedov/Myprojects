import tkinter.colorchooser
from tkinter import *
root = Tk()
root.title('My first python GUI')
root.geometry('800x600')
root.iconbitmap('python_icon.ico')

var = IntVar()
var2 = IntVar()

def onclick():
    mylabel2 = Label(root, text=var.get())
    mylabel2.pack()
    Label(root, text=var2.get()).pack()

chk1 = Checkbutton(root, text='Check me', variable=var)
chk1.pack()
chk2 = Checkbutton(root, text='Check me too', variable=var2)
chk2.pack()


Button(root, text='Click me', command=onclick).pack()

root.mainloop()











'''choice = IntVar()
choice.set('2')
label_text = StringVar()



def onclick():
    label_text.set(choice.get())

r1 = Radiobutton(root, text='text1', value=1, variable=choice)
r1.pack()
r2 = Radiobutton(root, text='text2', value=2, variable=choice)
r2.pack()
Button(root, text='Click me', command=onclick).pack()
mylabel = Label(root, textvariable=label_text)
mylabel.pack()

root.mainloop()'''
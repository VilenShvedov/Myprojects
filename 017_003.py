import tkinter.colorchooser
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('My first python GUI')
root.geometry('800x600')
root.iconbitmap('python_icon.ico')

label_text = StringVar()
int_variable = IntVar()
entry_text = StringVar()

def ptint_message(message):
    print(message)


def onclick():
    label_text.set(entry_text.get())
    ptint_message(entry_text.get())

user_entry = Entry(root, textvariable=entry_text).pack()
mylabel = Label(root, textvariable=label_text)
mylabel.pack()

Button(root, text='CLick me',command=onclick).pack()

root.mainloop()
import tkinter.colorchooser
from tkinter import *
root = Tk()
root.title('My first python GUI')
root.geometry('400x400')
root.iconbitmap('python_icon.ico')



def onclick(number):
    user_entry.delete(0, END)
    user_entry.insert(0, int(number) ** 2)



user_entry = Entry(root, width=100,bg='green',fg='white', borderwidth=1)
user_entry.insert(0,'text')
user_entry.pack()

some_list=[[1,2], [2,2], [2,3]]

Button(root, text='Click me', fg='#F5F5F5', bg='red', padx=30, pady=20,
       command=lambda:onclick(user_entry.get())).pack()
root.mainloop()
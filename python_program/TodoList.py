# python
# todo list
from tkinter import *;
tasklist = []

mainwindow = Tk()
mainwindow.geometry('400x300')

taskTab = Listbox(
    mainwindow
).pack()

textTab = Entry(
    mainwindow
).pack()

def add_task():
    task = taskTab.get()
    print('Task Added ',task)
    taskTab.insert('end',task)
    textTab.delete()

addButton = Button(
    mainwindow,
    command= add_task
).pack()

mainwindow.mainloop()
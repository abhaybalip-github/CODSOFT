# python
# Task List GUI code

import tkinter as tk;

def button_cmd():
    None


# defining main window
main_window = tk.Tk()
main_window.title('Taks-List')
main_window.geometry('500x500')
main_window.resizable(False,False)

# Text box to enter string
textbox = tk.Text(
    main_window,
    height=2,
    width=30,
    background='lightgrey',
    borderwidth=2,
    relief='solid',
    font='aerial',
).place(relx=0.05,rely=0.2)


# button to add task
AddButton = tk.Button(
    main_window,
    height=2,
    width=2,
    background='grey',
    command= button_cmd()
).place(
    relx=0,
    rely=0.2
)


# Task display box
task_box = tk.Frame(
    main_window,
    height=300,
    width=450,
    bg='lightgrey',
    borderwidth=2,
    relief='solid'
).place(relx=0.05,rely=0.35)

# run main window
main_window.mainloop()
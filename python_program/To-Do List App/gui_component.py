# python
# Task List GUI component code
import tkinter as tk;

# main window
main_window = tk.Tk()
main_window.title('Taks-List')
main_window.geometry('500x500')
main_window.resizable(False,False)

label = tk.Label(
    main_window,
    text='Task List',
    font=("Arial", 10, "bold"),
    height=3,
    width=30,
    background='#9cd0ff',
    bd=2,
    relief='solid',
).place(relx=0.25,rely=0.05)


# Text box to enter string
textbox = tk.Text(
    main_window,
    height=2,
    width=30,
    background='lightgrey',
    borderwidth=1,
    relief='solid',
    font='aerial',
).place(relx=0.05,rely=0.2)

# button to add task
AddButton = tk.Button(
    main_window,
    text='Add-Task',
    height=3,
    width=8,
    background= '#d2c2c2'
).place(
    relx=0.8,
    rely=0.19
)

# Task display box
task_box = tk.Frame(
    main_window,
    height=300,
    width=450,
    bg='#ffe9aa',
    borderwidth=1,
    relief='solid'
).place(relx=0.05,rely=0.35)

main_window.mainloop()
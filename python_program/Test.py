from tkinter import Tk, Listbox, Button, Entry

root = Tk()
root.title("To-Do List")

# Set window size
root.geometry("400x300")


def add_task():
    task = task_entry.get()
    if task:
        task_list.insert("end", task)
        task_entry.delete(0, "end")

def remove_task():
    selected_item = task_list.curselection()
    if selected_item:
        task_list.delete(selected_item[0])

def edit_task():
    # Open a new window for editing
    edit_window = Tk()
    edit_window.title("Edit Task")

    # Create widgets for edit window
    edit_entry = Entry(edit_window)
    edit_button = Button(edit_window, text="Update", command=lambda: update_task(edit_window, edit_entry))

    # Pre-fill entry field with selected task
    selected_item = task_list.get(task_list.curselection()[0])
    edit_entry.insert(0, selected_item)

    # Arrange widgets and run edit window
    edit_entry.pack()
    edit_button.pack()
    edit_window.mainloop()

def update_task(edit_window, edit_entry):
    updated_task = edit_entry.get()
    if updated_task:
        # Update the listbox with the new task
        selected_item = task_list.curselection()[0]
        task_list.delete(selected_item)
        task_list.insert(selected_item, updated_task)
        edit_window.destroy()


task_list = Listbox(root)
task_entry = Entry(root)
add_button = Button(root, text="Add", command=add_task)
remove_button = Button(root, text="Remove", command=remove_task)
edit_button = Button(root, text="Edit", command=edit_task)

# Arrange widgets
task_list.pack(fill="both", expand=True)
task_entry.pack()
add_button.pack()
remove_button.pack()
edit_button.pack()



root.mainloop()

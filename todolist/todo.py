import tkinter as tk
from tkinter import messagebox

# Functions
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# Widgets
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Tasks", command=clear_tasks)
clear_button.pack(pady=5)

tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=10)

# Run the application
root.mainloop()

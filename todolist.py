import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Entry widget for task input
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Button to add tasks
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Button to delete selected task
        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=2, column=0, padx=10, pady=10)

    def add_task(self):
        new_task = self.task_entry.get()

        if new_task:
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, new_task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()

        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            deleted_task = self.tasks.pop(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            messagebox.showinfo("Task Deleted", f"Task '{deleted_task}' deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()

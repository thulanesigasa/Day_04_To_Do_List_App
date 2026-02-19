import tkinter as tk
from tkinter import messagebox

# Theme Constants
BG_COLOR = "#1F1C2C"
FG_COLOR = "#928DAB"
ACCENT_COLOR = "#928DAB"
FONT_FAMILY = "Arial"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 4: To-Do List App")
        self.root.geometry("400x500")
        self.root.configure(bg=BG_COLOR)

        self.tasks = []

        self.setup_ui()

    def setup_ui(self):
        # Title Label
        self.title_label = tk.Label(
            self.root,
            text="To-Do List",
            bg=BG_COLOR,
            fg=ACCENT_COLOR,
            font=(FONT_FAMILY, 20, "bold"),
            pady=20
        )
        self.title_label.pack()

        # Input Frame
        input_frame = tk.Frame(self.root, bg=BG_COLOR)
        input_frame.pack(pady=10)

        # Entry Field
        self.task_entry = tk.Entry(
            input_frame,
            font=(FONT_FAMILY, 14),
            bg=BG_COLOR,
            fg=FG_COLOR,
            insertbackground=FG_COLOR,
            width=25,
            bd=0,
            highlightthickness=1,
            highlightbackground=FG_COLOR,
            highlightcolor=ACCENT_COLOR
        )
        self.task_entry.pack(side=tk.LEFT, padx=10)
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Add Button
        self.add_button = tk.Button(
            input_frame,
            text="Add",
            command=self.add_task,
            bg=ACCENT_COLOR,
            fg=BG_COLOR,
            activebackground=ACCENT_COLOR,
            activeforeground=BG_COLOR,
            font=(FONT_FAMILY, 10, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.add_button.pack(side=tk.LEFT)

        # Listbox Frame with Scrollbar
        list_frame = tk.Frame(self.root, bg=BG_COLOR)
        list_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(
            list_frame,
            font=(FONT_FAMILY, 12),
            bg=BG_COLOR,
            fg=FG_COLOR,
            selectbackground=FG_COLOR,
            selectforeground=BG_COLOR,
            bd=0,
            highlightthickness=0,
            activestyle="none",
            yscrollcommand=self.scrollbar.set
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bg=BG_COLOR)
        buttons_frame.pack(pady=20)

        # Delete Button
        self.delete_button = tk.Button(
            buttons_frame,
            text="Delete Task",
            command=self.delete_task,
            bg=ACCENT_COLOR,
            fg=BG_COLOR,
            activebackground=ACCENT_COLOR,
            activeforeground=BG_COLOR,
            font=(FONT_FAMILY, 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=5
        )
        self.delete_button.pack(side=tk.LEFT, padx=10)

        # Clear All Button
        self.clear_button = tk.Button(
            buttons_frame,
            text="Clear All",
            command=self.clear_all_tasks,
            bg=BG_COLOR,
            fg=FG_COLOR,
            activebackground=BG_COLOR,
            activeforeground=FG_COLOR,
            font=(FONT_FAMILY, 10),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=5
        )
        self.clear_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_all_tasks(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.tasks = []
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

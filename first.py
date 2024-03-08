import tkinter as tk

def on_click(button_value):
    current = entry_var.get()
    if button_value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == "C":
        entry_var.set("")
    else:
        entry_var.set(current + str(button_value))

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=('Helvetica', 20), justify="right", bd=10, insertwidth=4, width=14)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Helvetica', 14), command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Configure row and column weights so that they expand proportionally
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

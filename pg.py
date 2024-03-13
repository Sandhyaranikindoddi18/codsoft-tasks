import tkinter as tk
from tkinter import StringVar
import secrets
import string

def generate_password():
    length = int(length_var.get())
    
    if length <= 0:
        result_var.set("Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    result_var.set(password)

# Create main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and set variables
length_var = StringVar()
length_var.set(12)  # Default password length

result_var = StringVar()

# Create and place widgets
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, textvariable=length_var, justify='center')
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the main loop
root.mainloop()

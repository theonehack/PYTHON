import tkinter as tk
from tkinter import messagebox

def generate_table():
    try:
        table_number = int(table_entry.get())
        table_limit = int(limit_entry.get())
        
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        
        for j in range(table_limit):
            result_text.insert(tk.END, f"{table_number} * {j+1} = {table_number*(j+1)}\n")
        
        result_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Multiplication Table Generator")

# Create labels
table_label = tk.Label(root, text="Enter table number:")
limit_label = tk.Label(root, text="Enter table limit:")

# Create entry fields
table_entry = tk.Entry(root)
limit_entry = tk.Entry(root)

# Create a button to generate the table
generate_button = tk.Button(root, text="Generate Table", command=generate_table)

# Create a text widget to display the result
result_text = tk.Text(root, state=tk.DISABLED, width=30, height=10)

# Pack the widgets onto the window
table_label.pack(pady=5)
table_entry.pack(pady=5)
limit_label.pack(pady=5)
limit_entry.pack(pady=5)
generate_button.pack(pady=10)
result_text.pack()

# Start the main event loop
root.mainloop()

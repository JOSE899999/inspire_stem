import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    
    # You can add more validation here if needed
    
    # For demonstration, let's just show the entered username and password
    messagebox.showinfo("Registration Successful", f"Username: {username}\nPassword: {password}")
    
# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entry fields
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Create register button
btn_register = tk.Button(root, text="Register", command=register)
btn_register.grid(row=2, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()

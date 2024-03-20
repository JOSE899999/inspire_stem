import tkinter as tk
from  tkinter import messagebox

def register ():
    username = entry_username.get()
    password = entry_password.get()
    
    messagebox.showinfo("Registratation Successful", f"Username: {username}\nPassword:{password}")

root = tk.Tk()
root.title("Registration Form")

label_username =tk.Label(root, text="username:")
label_username.pack()
entry_username =tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root,text="password")
label_password.pack()
entry_password = tk.Entry(root)
entry_password.pack()
entry_password =tk.Entry(root, show="*")
entry_password.pack()

btn_register = tk.Button(root, text='Register',command=register)
btn_register.pack()

root.mainloop


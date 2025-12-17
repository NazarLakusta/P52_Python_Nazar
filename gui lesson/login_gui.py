import tkinter as tk
import re

def logining():
    login = login_entry.get()
    password = password_entry.get()

    if login_pattern.search(login):
        if password_pattern.search(password):
            login_entry.config(bg="green")
            password_entry.config(bg="green")
        else:
            login_entry.config(bg="red")
            password_entry.config(bg="red")
    else:
        login_entry.config(bg="red")
        password_entry.config(bg="red")

login_pattern = re.compile(r"^[a-zA-Z0-9._%-]{3,30}@[a-zA-Z0-9.-]{2,20}\.[a-zA-Z]{2,6}$")
password_pattern = re.compile(r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#%^&*?]).{6,20}$")

root = tk.Tk()
root.geometry("400x250+700+350")
root.resizable(False, False)

login_label = tk.Label(root, text="Login:", font=("Arial", 14), padx=50)
password_label = tk.Label(root, text="Password:", font=("Arial", 14), padx=50)

login_entry = tk.Entry(root, font=("Arial", 12), width=20)
password_entry = tk.Entry(root, font=("Arial", 12), width=20, show="*")

login_button = tk.Button(root, text="LOGIN", font=("Arial", 16), width=12, command=logining)

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=250)

root.grid_rowconfigure(0, minsize=90)
root.grid_rowconfigure(1, minsize=90)

login_label.grid(column=0, row=0)
password_label.grid(column=0, row=1)
login_entry.grid(column=1, row=0)
password_entry.grid(column=1, row=1)

login_button.grid(column=0, row=2, columnspan=2)

root.mainloop()

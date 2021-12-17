import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.geometry("300x130")
window.title("Login")
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./gui_tkinder/ejemplo7/icon.png'))
# bloquea la modificacion de la ventana (tamaño)
window.resizable(0, 0)

# configurando la grilla primeramente
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# label 1 - box 1
# label one user
user = ttk.Label(window, text="User")
user.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)
# box one user
box_user = ttk.Entry(window, width=20, justify=tk.CENTER)
box_user.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

# label 2 - box 2
# label two password
password = ttk.Label(window, text="Password")
password.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
# box two password
box_password = ttk.Entry(window, width=20, justify=tk.CENTER, show="*")
box_password.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

# button
def login_method():
    messagebox.showinfo("Login", f"Welcome: {box_user.get()}.\nYour password is: {box_password.get()}")
    
btn_login = ttk.Button(window, text="Login", command=login_method)
btn_login.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

window.mainloop()
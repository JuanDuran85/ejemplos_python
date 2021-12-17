import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # creacion de la ventana
        self.geometry("300x130")
        self.title("Login")
        # bloquea la modificacion de la ventana (tamaño)
        self.resizable(0, 0)
        # configurando la grilla primeramente
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # se mandan a crear los componentes
        self._crear_widget()
        
        # definir el metodo crear componentes
    def _crear_widget(self):
            
        # label one user
        user = ttk.Label(self, text="User")
        user.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)
        # box one user
        self.box_user = ttk.Entry(self, width=20, justify=tk.CENTER)
        self.box_user.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        # label two password
        password = ttk.Label(self, text="Password")
        password.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
        # box two password
        self.box_password = ttk.Entry(self, width=20, justify=tk.CENTER, show="*")
        self.box_password.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        # button od wiget
        btn_login = ttk.Button(self, text="Login", command=self._login_method)
        btn_login.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

    def _login_method(self):
        messagebox.showinfo("Login", f"Welcome: {self.box_user.get()}.\nYour password is: {self.box_password.get()}")

if __name__ == "__main__":
    window = Login()
    window.mainloop()    
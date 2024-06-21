from tkinter import *   
import ttkbootstrap as tb


class App(tb.Window):
    
    def __init__(self):
        super().__init__()
        self.windows_login()
        
    def windows_login(self):
        """_summary_
        """        
        self.grid_columnconfigure(0,weight=1)

        self.frame_login=Frame(master=self)
        self.frame_login.grid(row=1,column=0,sticky=NSEW)

        lblframe_login=tb.LabelFrame(master=self.frame_login,text="Acceso")
        lblframe_login.pack(padx=10,pady=35)

        lbl_titulo=tb.Label(master=lblframe_login,text="Iniciar sesión",font=("Verdana",18))
        lbl_titulo.pack(padx=10,pady=35)

        ent_user=tb.Entry(master=lblframe_login,width=40,justify=CENTER)
        ent_user.pack(padx=10,pady=10)

        ent_password=tb.Entry(master=lblframe_login,width=40,justify=CENTER)
        ent_password.pack(padx=10,pady=10)
        ent_password.config(show="*")

        btn_access=tb.Button(master=lblframe_login,width=38,text="Login",bootstyle="success-outline")
        btn_access.pack(padx=10,pady=10)

   
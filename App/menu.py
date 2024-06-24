from tkinter import *   
import ttkbootstrap as tb

from tkinter import messagebox as ms

from conexion.user_dao import search_user,change_user_pass


class App(tb.Window,Frame):
    def __init__(self):
        super().__init__()
        self._frame = None
        self.user=None
        self.windows()

   
    def windows(self):
        """_summary_
        """      
        if self.user==None:
          if self._frame is not None:
               self._frame.delete()
               self._frame = None
          if self._frame is None:
               self.windows_login_field()
            

    def windows_login_field(self):
        """_summary_
        """        
        self.grid_columnconfigure(0,weight=1)

        self.frame_login=Frame(master=self)
        self.frame_login.grid(row=1,column=0,sticky=NSEW)

        lblframe_login=tb.LabelFrame(master=self.frame_login,text="Acceso")
        lblframe_login.pack(padx=10,pady=35)

        lbl_titulo=tb.Label(master=lblframe_login,text="Iniciar sesión",font=("Verdana",18))
        lbl_titulo.pack(padx=10,pady=35)

        lbl_user=tb.Label(master=lblframe_login,text="Usuario",font=("Verdana",18))
        lbl_user.pack(padx=10)

        self.ent_user=tb.Entry(master=lblframe_login,width=40,justify=CENTER)
        self.ent_user.pack(padx=10,pady=10)
        self.ent_user.bind ("<Return>",self.login_user)

        lbl_password=tb.Label(master=lblframe_login,text="Contraseña",font=("Verdana",18))
        lbl_password.pack(padx=10)

        self.ent_password=tb.Entry(master=lblframe_login,width=40,justify=CENTER)
        self.ent_password.pack(padx=10,pady=10)
        self.ent_password.config(show="*")
        self.ent_password.bind ("<Return>",self.login_user)
        

        btn_recover_password=tb.Button(master=lblframe_login,width=38,text="Recuperar contraseña",bootstyle="primary-outline",command=self.recover_password)
        btn_recover_password.pack(padx=10,pady=10)

        self._frame = None

    def login_user(self,event):
        name=search_user(self.ent_user.get())
        if name!=None:
            if name!=False:
                if name[1]==self.ent_password.get():
                    if name[2]=='admin':
                     self.frame_login.destroy()
                     
                    elif (name[2]=='empleado'):
                        self.frame_login.destroy()
                        
                else:
                    self.clear_login_windows()
                    ms.showerror("Datos erroneos","El usuario y la contraseña no coiciden")
                    self.clear_login_windows()
             
            else:
                ms.showerror("El usuario no existe", f"el usuario {self.ent_user} no fue creado")
                self.clear_login_windows()
        else:
            self.clear_login_windows()
    
    def recover_password(self):
        """_summary_
        """        
        self.frame_login.destroy()
        
        self.grid_columnconfigure(0,weight=1)

        self.frame_recover_password=Frame(master=self)
        self.frame_recover_password.grid(row=1,column=0,sticky=NSEW)

        lblframe_recover_password=tb.LabelFrame(master=self.frame_recover_password)
        lblframe_recover_password.pack(padx=10,pady=35)

        lbl_titulo=tb.Label(master=lblframe_recover_password,text="Recuperación",font=("Verdana",18))
        lbl_titulo.pack(padx=10,pady=35)

        lbl_user=tb.Label(master=lblframe_recover_password,text="Usuario",font=("Verdana",14))
        lbl_user.pack(padx=10)

        self.ent_user_pass=tb.Entry(master=lblframe_recover_password,width=40,justify=CENTER)
        self.ent_user_pass.pack(padx=10,pady=10)
        self.ent_user_pass.bind ("<Return>",self.check_new_password)

        lbl_new_password=tb.Label(master=lblframe_recover_password,text="Nueva Contraseña",font=("Verdana",14))
        lbl_new_password.pack(padx=10)

        self.ent_new_pass=tb.Entry(master=lblframe_recover_password,width=40,justify=CENTER)
        self.ent_new_pass.pack(padx=10,pady=10)
        self.ent_new_pass.config(show="*")
        self.ent_new_pass.bind ("<Return>",self.check_new_password)

        lbl_new_password_second=tb.Label(master=lblframe_recover_password,text="Repita Nueva Contraseña",font=("Verdana",14))
        lbl_new_password_second.pack(padx=10)
        

        self.ent_new_pass_second=tb.Entry(master=lblframe_recover_password,width=40,justify=CENTER)
        self.ent_new_pass_second.pack(padx=10,pady=10)
        self.ent_new_pass_second.config(show="*")
        self.ent_new_pass_second.bind ("<Return>",self.check_new_password)

            

        btn_back=tb.Button(master=lblframe_recover_password,width=38,text="Regresar",bootstyle="primary-outline",command=self.windows)
        btn_back.pack(padx=10,pady=10)   

        self._frame = None
   
    def check_new_password(self,event):
        
        if self.ent_new_pass_second.get() == self.ent_new_pass.get():
            if search_user(self.ent_user_pass.get()) !=False:
                change_user_pass(self.ent_user_pass.get(),self.ent_new_pass.get())
                ms.showinfo("Se cambio la contraseña","Se cambio exitosamente la contraseña.\n volveras al menu de inicio para que ingreses sessión")
                self.clear_recover_password()
                self.frame_recover_password.destroy()
                self.windows()
            else:
                ms.showerror("El usuario no existe", f"el usuario no fue creado {self.ent_user_pass.get()}")
                self.clear_recover_password()
        else:
            ms.showerror("Error al crear nueva contraseña", "las contraseñas no son iguales")
            self.clear_recover_password()
    def longin(self):
        self.frame_loginin=Frame(master=self)

    def clear_recover_password(self):
        """_summary_
        """        
        self.ent_new_pass.delete(0, tb.END)
        self.ent_new_pass_second.delete(0, tb.END)
        self.ent_user_pass.delete(0, tb.END)
        self.ent_user_pass.focus()

    def clear_login_windows(self):
        """_summary_
        """        
        self.ent_user.delete(0, tb.END)
        self.ent_password.delete(0, tb.END)
        self.ent_user.focus()
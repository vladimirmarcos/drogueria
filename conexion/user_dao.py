import sqlite3
from tkinter import messagebox as mb

from .conexiondb import ConexionDB



def search_user(user):
     """_summary_

    Args:
        user (_type_): _description_

    Returns:
        _type_: _description_
    """     
     try:     
        conexion=ConexionDB()
        sql=f""" SELECT user,password,role from users where user='{user}'"""
        conexion.cursor.execute(sql)
        user_found=conexion.cursor.fetchone()
        conexion.close()
        if user_found!=None:
            return user_found
        else:
             return False
  
     except sqlite3.OperationalError:
            mb.showerror("No se pudo acceder a la base de datos","No se ingresar a la base de datos","La base de datos esta siendo ocupada o esta dañada, intente más tarde")
            return None

def change_user_pass(user,password):
     """_summary_

    Args:
        user (_type_): _description_

    Returns:
        _type_: _description_
    """     
         
     conexion=ConexionDB()
     sql=f""" UPDATE users SET password='{password}' WHERE user='{user}'"""
     conexion.cursor.execute(sql)
     conexion.close()
        
  
     


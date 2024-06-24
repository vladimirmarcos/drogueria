from tkinter import *   
from tkinter import messagebox
import ttkbootstrap as tb




class FrameAdminWindows(Frame):
    def __init__(self):
        super().__init__()
        self.admin_windows()
        
    def admin_windows(self):
        """_summary_
        """        
        self.grid_columnconfigure(0,weight=1)

        self.frame_login=Frame(master=self)
        self.frame_login.grid(row=1,column=0,sticky=NSEW)

        lblframe_login=tb.LabelFrame(master=self.frame_login,text="Admin")
        lblframe_login.pack(padx=10,pady=35)

        
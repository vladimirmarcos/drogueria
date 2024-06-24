import tkinter as tk
from App.menu import App
import ttkbootstrap as tb

def main():
    ventana = App()
    ventana.title("asdsad")
    ventana.state("zoomed")
    tb.Style("cyborg")
    ventana.mainloop()


if __name__=='__main__':
    
    main()
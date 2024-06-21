import tkinter as tk
from menu.menu import App
import ttkbootstrap as tb

def main():
    ventana = App()
    ventana.title("Machirulo")
    ventana.state("zoomed")
    tb.Style("cyborg")

    ventana.mainloop()


if __name__=='__main__':
    
    main()
from tkinter import *
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Hoola imagen")
ventana.geometry("600x600")
imagen = PhotoImage(file="fff.png")
img = Label(ventana, image=imagen).place(x=100, y=100)


ventana.mainloop()

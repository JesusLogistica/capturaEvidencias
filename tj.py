import tkinter as tk
from tkinter import ttk
from tkinter import *
def saludar():
    Label(root, text="¡No vuelvas a presionarlo!").grid()
root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
boton =     .Button(text="¡Hola, mundo!", command=saludar)
boton.place(x=50, y=50)
root.mainloop()